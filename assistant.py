"""
assistant.py
This is the "prompt engineering + AI integration" core of Pocket C.A.

Uses Google Gemini (free tier, no credit card needed) instead of a paid API.
Get a free key at https://aistudio.google.com/apikey

Design choices worth highlighting in your project write-up:
1. A tight system prompt that defines role, scope, and guardrails.
2. Grounded generation: before every reply, we compute real statistics from
   the uploaded data in plain Python (data_utils.py) and inject them into the
   prompt as a "DATA CONTEXT" block. The model is instructed to only state
   numbers that appear in that block, never to invent figures. This is the
   same idea as retrieval-augmented generation (RAG), just with computed
   stats instead of retrieved documents.
3. Conversation history is passed on every turn so the assistant remembers
   context within a session.
"""

import json
import os
from google import genai
from google.genai import types

import data_utils as du

DEFAULT_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash")

SYSTEM_PROMPT = """You are Pocket C.A., a friendly and precise AI accounting assistant \
built to help everyday users understand their personal finances and general \
accounting concepts.

Scope and style:
- You help with: explaining accounting/finance concepts, analyzing the user's \
uploaded transactions, spotting spending patterns, and giving practical budgeting tips.
- You are NOT a licensed financial advisor, accountant, or tax professional. \
For anything involving legal, tax-filing, or investment decisions, give general \
educational information and clearly recommend the user consult a qualified professional.
- Never invent numbers. Every reply you get includes a "DATA CONTEXT" block \
containing real, pre-computed figures from the user's transactions. You MUST \
base every number you state only on that block. If the block says no data was \
uploaded, or doesn't contain what's needed to answer, say so plainly instead \
of guessing.
- Be concise. Use short paragraphs or bullet points for breakdowns. Always show \
currency amounts formatted like $1,234.56 (or the currency implied by the data).
- If a user's question is ambiguous (e.g. "my spending" without a time period), \
make a reasonable assumption (e.g. default to all available data) and say what \
assumption you made.
"""


def get_model(api_key: str, model_name: str = DEFAULT_MODEL):
    """
    Return a (client, model_name) pair bound to the given API key.
    Kept as a tuple so app.py doesn't need to know SDK internals.
    """
    client = genai.Client(api_key=api_key)
    return client, model_name


def _build_data_context(df, user_message: str) -> dict:
    """
    Compute a snapshot of real statistics from the transactions, grounded to
    whatever the user is asking about. This replaces model-side function
    calling with plain, reliable Python — the model never has to "decide" to
    fetch data, it always receives the numbers it might need.
    """
    if df is None or df.empty:
        return {"note": "No transaction data has been uploaded yet."}

    context = {
        "all_time_summary": du.compute_summary(df),
        "available_months": sorted(df["month"].unique().tolist()),
        "monthly_trend": du.compute_trend(df).to_dict(orient="records"),
        "top_merchants": du.top_merchants(df, n=8),
    }

    latest_month = sorted(df["month"].unique())[-1]
    context["most_recent_month_summary"] = du.compute_summary(df, month=latest_month)

    # If the question mentions a specific month, category, or keyword-like
    # word, pull matching transactions too, so specific questions ("show me
    # my Swiggy orders") can be answered precisely.
    words = [w.strip(".,?!").lower() for w in user_message.split() if len(w) > 3]
    matches = []
    for w in words:
        found = du.search_transactions(df, keyword=w, limit=10)
        if found:
            matches.extend(found)
    if matches:
        seen = set()
        unique_matches = []
        for m in matches:
            key = (m["date"], m["description"], m["amount"])
            if key not in seen:
                seen.add(key)
                unique_matches.append(m)
        context["possibly_relevant_transactions"] = unique_matches[:15]

    return context


def ask_pocket_ca(model, conversation: list, df) -> str:
    """
    model: (client, model_name) tuple from get_model().
    conversation: list of {"role": "user"|"assistant", "content": str} - prior turns
                  (the LAST item is the new user message).
    df: the uploaded transactions DataFrame (or None).
    Returns the assistant's final text reply.
    """
    client, model_name = model

    history = []
    for m in conversation[:-1]:
        role = "user" if m["role"] == "user" else "model"
        history.append({"role": role, "parts": [{"text": m["content"]}]})

    user_message = conversation[-1]["content"]
    context = _build_data_context(df, user_message)

    augmented_message = (
        f"DATA CONTEXT (real, pre-computed — use only these numbers for factual claims):\n"
        f"{json.dumps(context, default=str)}\n\n"
        f"USER QUESTION:\n{user_message}"
    )

    config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
    chat = client.chats.create(model=model_name, config=config, history=history)
    response = chat.send_message(augmented_message)
    return response.text.strip()


def generate_report_narrative(model, summary: dict, trend: list, top_merch: list) -> str:
    """Ask Gemini to write a short, plain-English narrative summary from pre-computed stats."""
    client, model_name = model
    prompt = f"""Write a short (150-200 word) financial summary report for a user, based ONLY on this data. \
Do not invent any numbers not present below. Use a warm, encouraging, professional tone. Structure it as \
2-3 short paragraphs: overall picture, notable spending patterns, one practical suggestion.

Summary stats: {json.dumps(summary, default=str)}
Monthly trend: {json.dumps(trend, default=str)}
Top merchants by spend: {json.dumps(top_merch, default=str)}
"""
    config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
    response = client.models.generate_content(model=model_name, contents=prompt, config=config)
    return response.text.strip()
