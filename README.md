# 💰 Pocket C.A. — AI-Powered Accounting Assistant

An intelligent, conversational accounting assistant built with **Streamlit** and powered by **Google's free Gemini API**. Pocket C.A. goes beyond a basic Q&A bot — it grounds every answer in real, computed numbers from your uploaded transactions, auto-generates visual financial reports, and writes AI narrative summaries. All of it runs at **zero cost**, with no credit card required anywhere in the stack.

🔗 **Live Demo:** https://pocketca-qj966hoxr8mxtykgaxvs3w.streamlit.app
🔗 **GitHub Repo:** https://github.com/niteshtiwari2444/pocket_ca

---

## ✨ Features

| Feature | Description |
|---|---|
| 💬 **Grounded AI chat** | Ask natural-language questions about your finances — every numeric answer is backed by real computed data, never guessed |
| 📊 **Reports dashboard** | Category breakdown (donut chart), monthly income/expense trend, and top-merchants chart, filterable by period |
| 🧠 **AI narrative summaries** | One click generates a plain-English financial summary, downloadable as Markdown |
| 📁 **CSV/XLSX upload** | Upload your own transactions, or click "Use sample data" to demo instantly |
| 🏷️ **Auto-categorization** | Keyword-based categorization (groceries, dining, transport, rent, etc.) when no category column is provided |
| 🎨 **Custom ledger-themed UI** | Hand-built visual identity (custom CSS, themed charts, custom chat avatars) instead of default Streamlit styling |
| 🔒 **Secure key handling** | API key lives only in Streamlit Secrets or a runtime input — never hard-coded or committed |
| 🛡️ **Robust error handling** | Friendly messages for missing data, invalid keys, and API/model errors |

## 🏗️ Architecture

```
User Input (Streamlit chat_input / file_uploader)
        │
        ▼
Transaction DataFrame (st.session_state.df) ──► data_utils.py
        │                                        (pandas: summary, trend,
        │                                         categorization, search)
        ▼
Real computed stats injected as "DATA CONTEXT" ──► assistant.py
        │                                          (system prompt + context)
        ▼
Google Gemini API (google-genai SDK) ──► Grounded natural-language response
        │
        ▼
Rendered in Chat tab / Reports tab (Plotly charts + AI narrative)
```

## 🧰 Tech Stack

- **Frontend:** Streamlit with custom CSS (ledger-style theme, themed charts, custom chat avatars)
- **LLM Backend:** Google Gemini API (`google-genai` SDK) — free tier, no billing required
- **Model:** `gemini-3.5-flash` (configurable via `GEMINI_MODEL`)
- **Data processing:** pandas for all financial calculations
- **Charts:** Plotly (donut, line, bar), custom-themed to match the app

## 📂 Project Structure

```
pocket_ca/
├── app.py                       # Main Streamlit application (UI, tabs, chat, reports)
├── assistant.py                 # System prompt, Gemini calls, grounded-context builder
├── data_utils.py                 # Transaction loading, categorization, summary/trend math
├── theme.py                      # Custom CSS theme + Plotly chart styling
├── requirements.txt              # Python dependencies
├── .streamlit/
│   ├── config.toml               # Pinned light theme (prevents dark-mode rendering issues)
│   └── secrets.toml.example      # Template showing required secrets
├── .gitignore
└── README.md
```

## ⚙️ Run Locally

```bash
git clone https://github.com/niteshtiwari2444/pocket_ca.git
cd pocket_ca
pip install -r requirements.txt
streamlit run app.py
```

Get a **free** Gemini API key (no billing required) at https://aistudio.google.com/apikey, then paste it into the sidebar when the app opens (or set it as `GEMINI_API_KEY` in your environment).

---

## 🧠 How It Works

1. **Data loading** – Uploaded CSV/XLSX is parsed in `data_utils.py`; missing categories are auto-assigned via keyword matching, and dates are bucketed into months.
2. **Grounded context, not guesswork** – Before every chat reply, `_build_data_context()` in `assistant.py` runs real pandas calculations (totals, category breakdown, monthly trend, top merchants, and any transactions matching keywords in the question) and packages them as JSON.
3. **Prompt construction** – That JSON is injected into the prompt as a "DATA CONTEXT" block, and the system prompt explicitly instructs Gemini to only state numbers that appear in it — this is the same idea as retrieval-augmented generation (RAG), just with computed stats instead of retrieved documents.
4. **Conversation history** – Prior turns are passed to `client.chats.create()` on every call so the assistant stays coherent across a multi-turn conversation.
5. **Reports tab** – The same `data_utils.py` functions power the Reports tab's KPI cards and Plotly charts, and a separate one-shot Gemini call turns the pre-computed stats into a short narrative summary.
6. **Custom theming** – `theme.py` injects CSS (ledger-style palette, custom fonts, themed cards) and a Plotly styling helper (`apply_ledger_chart_theme`) so charts match the rest of the UI instead of using Streamlit/Plotly defaults.

## 🔒 Security Notes

- The API key is read from `st.secrets` / environment variables, or entered at runtime into a password-masked sidebar field — never hard-coded.
- `.streamlit/secrets.toml` (the file with the real key) is excluded via `.gitignore`; only the harmless `secrets.toml.example` template is committed.
- Uploaded transaction data lives only in `st.session_state` for the current session — nothing is persisted to a database or written to disk.

## 🚀 Future Enhancements

- PDF export for reports (currently Markdown only)
- Multi-currency support
- Budget-setting with proactive overspending alerts
- Persistent storage of transactions across sessions
- Bank-statement PDF parsing

## 👤 Author

**Name:** Nitesh Tiwari &nbsp;|&nbsp; **Course:** Generative AI &nbsp;|&nbsp; **Submission Date:** 27 july 2026

## 📄 License

Created for academic/educational purposes as part of a Generative AI course.
