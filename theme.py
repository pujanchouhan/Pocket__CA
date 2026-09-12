"""
theme.py
Pocket C.A. — bright modern fintech theme
"""

LEDGER_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

/* =========================
   MAIN COLORS
   ========================= */
:root {
    --bg: #F4F7FB;
    --surface: #FFFFFF;
    --surface-2: #EEF2F7;
    --text: #172033;
    --muted: #68758A;
    --primary: #FF4F81;
    --primary-dark: #E83D70;
    --secondary: #5B5FEF;
    --cyan: #18B7C9;
    --green: #16A878;
    --red: #E5485D;
    --border: #DDE3EC;
}

/* =========================
   APP BACKGROUND
   ========================= */
.stApp {
    background:
        radial-gradient(circle at 0% 0%, rgba(255,79,129,0.13), transparent 25%),
        radial-gradient(circle at 100% 0%, rgba(91,95,239,0.13), transparent 25%),
        #F4F7FB !important;
    color: #172033 !important;
}

[data-testid="stAppViewContainer"] {
    background: #F4F7FB !important;
}

[data-testid="stHeader"] {
    background: rgba(244,247,251,0.90) !important;
}

.block-container {
    max-width: 1400px !important;
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
}

/* =========================
   TEXT
   ========================= */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    color: #172033 !important;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #172033 !important;
}

p, label, span, div {
    color: inherit;
}

/* =========================
   SIDEBAR
   ========================= */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #171B3A 0%, #25205A 100%) !important;
    border-right: none !important;
}

[data-testid="stSidebar"] > div:first-child {
    background: transparent !important;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] input,
[data-testid="stSidebar"] textarea,
[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background: rgba(255,255,255,0.10) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255,255,255,0.18) !important;
}

/* =========================
   HEADER
   ========================= */
.ledger-header {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #FF4F81 0%, #8E55E8 52%, #5B5FEF 100%) !important;
    border: none !important;
    border-radius: 24px;
    padding: 2.4rem 2.7rem;
    margin-bottom: 1.7rem;
    box-shadow: 0 18px 45px rgba(91,95,239,0.22);
}

.ledger-header::before {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    right: -80px;
    top: -130px;
    background: rgba(255,255,255,0.16);
    border-radius: 50%;
    filter: blur(8px);
}

.ledger-header::after {
    content: "";
    position: absolute;
    width: 180px;
    height: 180px;
    left: 45%;
    bottom: -120px;
    background: rgba(255,255,255,0.10);
    border-radius: 50%;
}

.ledger-header h1,
.ledger-header p,
.ledger-eyebrow,
.ledger-tagline,
.ledger-seal {
    position: relative;
    z-index: 2;
}

.ledger-header h1 {
    color: #FFFFFF !important;
    font-size: 2.7rem;
    font-weight: 700;
    margin: 0;
}

.ledger-eyebrow {
    color: #FFE7EF !important;
    font-family: 'IBM Plex Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    font-size: 0.72rem;
    margin-bottom: 0.5rem;
}

.ledger-tagline {
    color: #FFF3F7 !important;
    margin-top: 0.6rem;
    font-size: 0.98rem;
}

.ledger-seal {
    position: absolute;
    right: 1.8rem;
    top: 1.4rem;
    width: 62px;
    height: 62px;
    border: 1px solid rgba(255,255,255,0.40);
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #FFFFFF !important;
    background: rgba(255,255,255,0.12);
}

/* =========================
   COLUMNS
   ========================= */
[data-testid="column"] {
    padding-left: 0.5rem;
    padding-right: 0.5rem;
}

/* =========================
   METRICS
   ========================= */
[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 1px solid #DDE3EC !important;
    border-top: 4px solid #FF4F81 !important;
    border-radius: 16px !important;
    padding: 1rem 1.2rem !important;
    box-shadow: 0 8px 25px rgba(23,32,51,0.07) !important;
}

[data-testid="stMetricValue"] {
    color: #172033 !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-weight: 600 !important;
}

[data-testid="stMetricLabel"] {
    color: #68758A !important;
    font-family: 'IBM Plex Mono', monospace !important;
    text-transform: uppercase;
    letter-spacing: 0.07em;
}

/* =========================
   BUTTONS
   ========================= */
.stButton > button {
    background: #FFFFFF !important;
    color: #172033 !important;
    border: 1px solid #DDE3EC !important;
    border-radius: 11px !important;
    font-weight: 600 !important;
    box-shadow: 0 5px 15px rgba(23,32,51,0.05) !important;
}

.stButton > button:hover {
    background: #FFF0F5 !important;
    color: #E83D70 !important;
    border-color: #FF4F81 !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #FF4F81, #8E55E8) !important;
    color: #FFFFFF !important;
    border: none !important;
}

.stButton > button[kind="primary"] * {
    color: #FFFFFF !important;
}

/* =========================
   INPUTS
   ========================= */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background: #FFFFFF !important;
    color: #172033 !important;
    border: 1px solid #DDE3EC !important;
    border-radius: 11px !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border-color: #FF4F81 !important;
    box-shadow: 0 0 0 1px #FF4F81 !important;
}

[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    color: #172033 !important;
    border-color: #DDE3EC !important;
    border-radius: 11px !important;
}

/* Dropdown text */
[data-baseweb="select"] * {
    color: #172033 !important;
}

/* =========================
   TABS
   ========================= */
.stTabs [data-baseweb="tab-list"] {
    background: #FFFFFF !important;
    border: 1px solid #DDE3EC !important;
    border-radius: 13px !important;
    padding: 0.3rem;
    gap: 0.25rem;
}

.stTabs [data-baseweb="tab"] {
    color: #68758A !important;
    border-radius: 9px;
    font-family: 'IBM Plex Mono', monospace;
}

.stTabs [aria-selected="true"] {
    background: #FFF0F5 !important;
    color: #E83D70 !important;
}

.stTabs [data-baseweb="tab-highlight"] {
    background: #FF4F81 !important;
}

/* =========================
   CHAT
   ========================= */
[data-testid="stChatMessage"] {
    background: #FFFFFF !important;
    border: 1px solid #DDE3EC !important;
    border-radius: 15px !important;
    box-shadow: 0 7px 20px rgba(23,32,51,0.06) !important;
}

[data-testid="stChatInput"] textarea {
    background: #FFFFFF !important;
    color: #172033 !important;
}

/* =========================
   CUSTOM CARDS
   ========================= */
.ledger-section-title {
    display: flex;
    align-items: center;
    gap: 0.55rem;
    color: #172033 !important;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.25rem;
    font-weight: 600;
    border-bottom: 1px solid #DDE3EC;
    padding-bottom: 0.5rem;
    margin: 1.4rem 0 0.9rem;
}

.ledger-section-title::before {
    content: "";
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #FF4F81;
    box-shadow: 0 0 12px rgba(255,79,129,0.45);
}

.ledger-note {
    background: #FFF4F7 !important;
    color: #172033 !important;
    border: 1px solid #FFD1DE !important;
    border-left: 4px solid #FF4F81 !important;
    border-radius: 10px;
    padding: 0.9rem 1.1rem;
}

.ledger-chart-card {
    background: #FFFFFF !important;
    border: 1px solid #DDE3EC !important;
    border-radius: 16px;
    padding: 0.6rem 0.8rem;
    box-shadow: 0 8px 25px rgba(23,32,51,0.06);
}

/* =========================
   EXPANDER / DATAFRAME
   ========================= */
[data-testid="stExpander"] {
    background: #FFFFFF !important;
    border: 1px solid #DDE3EC !important;
    border-radius: 13px !important;
}

[data-testid="stDataFrame"] {
    border: 1px solid #DDE3EC !important;
    border-radius: 12px;
    overflow: hidden;
}

/* =========================
   FILE UPLOADER
   ========================= */
[data-testid="stFileUploaderDropzone"] {
    background: #FFFFFF !important;
    border: 1px dashed #FF4F81 !important;
    border-radius: 13px !important;
}

[data-testid="stFileUploaderDropzone"]:hover {
    background: #FFF4F7 !important;
}

/* =========================
   DIVIDERS
   ========================= */
hr {
    border-color: #DDE3EC !important;
}

/* =========================
   MOBILE
   ========================= */
@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .ledger-header {
        padding: 1.7rem;
        border-radius: 18px;
    }

    .ledger-header h1 {
        font-size: 2.1rem;
    }

    .ledger-seal {
        display: none;
    }

    [data-testid="column"] {
        padding-left: 0;
        padding-right: 0;
    }
}
</style>
"""

PLOTLY_COLORWAY = [
    "#FF4F81",
    "#5B5FEF",
    "#18B7C9",
    "#16A878",
    "#E5485D",
    "#8E55E8",
]

def apply_ledger_chart_theme(fig):
    fig.update_layout(
        colorway=PLOTLY_COLORWAY,
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(
            family="DM Sans, sans-serif",
            color="#172033",
            size=13,
        ),
        title=dict(
            font=dict(
                family="Space Grotesk, sans-serif",
                color="#172033",
                size=18,
            )
        ),
        legend=dict(
            bgcolor="rgba(255,255,255,0)",
            font=dict(
                family="IBM Plex Mono, monospace",
                color="#68758A",
                size=11,
            ),
        ),
        margin=dict(t=40, b=30, l=20, r=20),
        hoverlabel=dict(
            bgcolor="#172033",
            bordercolor="#FF4F81",
            font=dict(
                family="DM Sans, sans-serif",
                color="#FFFFFF",
            ),
        ),
    )

    fig.update_xaxes(
        gridcolor="#E8ECF2",
        zerolinecolor="#DDE3EC",
        tickfont=dict(
            color="#68758A",
            family="IBM Plex Mono, monospace",
        ),
        linecolor="#DDE3EC",
    )

    fig.update_yaxes(
        gridcolor="#E8ECF2",
        zerolinecolor="#DDE3EC",
        tickfont=dict(
            color="#68758A",
            family="IBM Plex Mono, monospace",
        ),
        linecolor="#DDE3EC",
    )

    return fig
