"""
data_utils.py
Handles loading transaction data and computing financial statistics.
Keeping all "math" here (not in the LLM) means the AI assistant's answers
about numbers are always grounded in real, verifiable calculations.
"""

import pandas as pd
from datetime import datetime


REQUIRED_COLUMNS = ["date", "description", "amount"]

# Very small keyword-based auto-categorizer, used only when the uploaded
# file has no "category" column. Keeps the demo useful out of the box.
CATEGORY_KEYWORDS = {
    "Groceries": ["grocery", "supermarket", "mart", "walmart", "kroger", "reliance fresh", "bigbasket"],
    "Food & Dining": ["restaurant", "cafe", "coffee", "swiggy", "zomato", "starbucks", "mcdonald", "kfc", "pizza"],
    "Transport": ["uber", "ola", "lyft", "fuel", "petrol", "gas station", "metro", "taxi"],
    "Utilities": ["electricity", "water bill", "internet", "broadband", "mobile recharge", "phone bill"],
    "Rent": ["rent"],
    "Entertainment": ["netflix", "spotify", "prime video", "movie", "cinema", "hotstar"],
    "Shopping": ["amazon", "flipkart", "myntra", "mall", "clothing"],
    "Health": ["pharmacy", "hospital", "clinic", "doctor", "medical"],
    "Income": ["salary", "payroll", "deposit", "refund", "interest credit"],
    "Transfer": ["transfer", "upi", "neft", "imps"],
}


def _guess_category(description: str) -> str:
    desc = str(description).lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(k in desc for k in keywords):
            return category
    return "Other"


def load_transactions(file) -> pd.DataFrame:
    """
    Load a CSV/Excel file of transactions.
    Expected columns (case-insensitive): date, description, amount, [category]
    Positive amount = income/credit, negative amount = expense/debit.
    """
    if hasattr(file, "name") and file.name.lower().endswith((".xlsx", ".xls")):
        df = pd.read_excel(file)
    else:
        df = pd.read_csv(file)

    df.columns = [c.strip().lower() for c in df.columns]

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(
            f"Missing required column(s): {', '.join(missing)}. "
            f"Your file needs at least: date, description, amount."
        )

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["date", "amount"])

    if "category" not in df.columns:
        df["category"] = df["description"].apply(_guess_category)
    else:
        df["category"] = df["category"].fillna("Other")

    df["month"] = df["date"].dt.to_period("M").astype(str)
    return df.sort_values("date").reset_index(drop=True)


def load_sample_data() -> pd.DataFrame:
    from io import StringIO
    sample_csv = StringIO(SAMPLE_CSV_TEXT)
    return load_transactions(sample_csv)


def compute_summary(df: pd.DataFrame, month: str = None) -> dict:
    """Compute a headline financial summary, optionally filtered to one month (YYYY-MM)."""
    data = df if month is None else df[df["month"] == month]
    if data.empty:
        return {"error": f"No transactions found for {month or 'the given period'}."}

    income = data.loc[data["amount"] > 0, "amount"].sum()
    expenses = -data.loc[data["amount"] < 0, "amount"].sum()
    net = income - expenses

    by_category = (
        data.loc[data["amount"] < 0]
        .groupby("category")["amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
    )

    return {
        "period": month or "all time",
        "total_income": round(float(income), 2),
        "total_expenses": round(float(expenses), 2),
        "net_savings": round(float(net), 2),
        "savings_rate_pct": round(float(net / income * 100), 1) if income > 0 else None,
        "top_categories": [
            {"category": cat, "amount": round(float(amt), 2)}
            for cat, amt in by_category.head(5).items()
        ],
        "transaction_count": int(len(data)),
    }


def compute_trend(df: pd.DataFrame) -> pd.DataFrame:
    """Monthly income vs expenses, for trend charting."""
    grouped = df.groupby("month").apply(
        lambda g: pd.Series({
            "income": g.loc[g["amount"] > 0, "amount"].sum(),
            "expenses": -g.loc[g["amount"] < 0, "amount"].sum(),
        })
    ).reset_index()
    grouped["net"] = grouped["income"] - grouped["expenses"]
    return grouped.sort_values("month")


def search_transactions(df: pd.DataFrame, keyword: str = None, category: str = None, limit: int = 20) -> list:
    """Filter transactions by keyword and/or category, for the assistant to inspect specifics."""
    data = df.copy()
    if keyword:
        data = data[data["description"].str.contains(keyword, case=False, na=False)]
    if category:
        data = data[data["category"].str.lower() == category.lower()]
    data = data.sort_values("date", ascending=False).head(limit)
    return [
        {
            "date": row["date"].strftime("%Y-%m-%d"),
            "description": row["description"],
            "amount": round(float(row["amount"]), 2),
            "category": row["category"],
        }
        for _, row in data.iterrows()
    ]


def top_merchants(df: pd.DataFrame, n: int = 5) -> list:
    expenses = df[df["amount"] < 0].copy()
    expenses["amount"] = expenses["amount"].abs()
    grouped = (
        expenses.groupby("description")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )
    return [{"merchant": m, "total": round(float(a), 2)} for m, a in grouped.items()]


SAMPLE_CSV_TEXT = """date,description,amount
2026-05-01,Salary Deposit,52000
2026-05-02,Reliance Fresh Grocery,-2200
2026-05-03,Swiggy Order,-450
2026-05-04,Uber Ride,-320
2026-05-05,Netflix Subscription,-499
2026-05-07,Electricity Bill,-1800
2026-05-09,Amazon Shopping,-3200
2026-05-10,Rent Payment,-15000
2026-05-12,Starbucks Coffee,-380
2026-05-15,Mobile Recharge,-599
2026-05-18,Zomato Order,-650
2026-05-20,Pharmacy Purchase,-720
2026-05-22,Petrol Station,-2500
2026-05-25,Flipkart Shopping,-1800
2026-05-28,Movie Cinema,-600
2026-06-01,Salary Deposit,52000
2026-06-02,Reliance Fresh Grocery,-2400
2026-06-03,Swiggy Order,-500
2026-06-05,Netflix Subscription,-499
2026-06-06,Uber Ride,-410
2026-06-08,Electricity Bill,-1950
2026-06-10,Rent Payment,-15000
2026-06-11,Amazon Shopping,-2100
2026-06-14,Starbucks Coffee,-420
2026-06-16,Mobile Recharge,-599
2026-06-19,Zomato Order,-700
2026-06-21,Petrol Station,-2700
2026-06-23,Pharmacy Purchase,-540
2026-06-26,Flipkart Shopping,-2600
2026-06-29,Movie Cinema,-600
2026-07-01,Salary Deposit,53000
2026-07-02,Reliance Fresh Grocery,-2500
2026-07-03,Swiggy Order,-480
2026-07-05,Netflix Subscription,-499
2026-07-06,Uber Ride,-390
2026-07-08,Electricity Bill,-2000
2026-07-10,Rent Payment,-15000
2026-07-12,Amazon Shopping,-4200
2026-07-14,Starbucks Coffee,-450
2026-07-16,Mobile Recharge,-599
2026-07-18,Interest Credit,300
2026-07-19,Zomato Order,-620
2026-07-21,Petrol Station,-2600
2026-07-23,Pharmacy Purchase,-680
"""
