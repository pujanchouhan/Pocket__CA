"""
theme.py
Visual identity for Pocket C.A. — a "ledger / passbook" aesthetic instead of
default Streamlit gray boxes. Grounded in the subject: deep ledger-green +
aged paper cream + brass accents, a serif display face for headings, and a
monospace face for numbers (like an old accounting ledger book).
"""

LEDGER_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

:root {
  --paper: #F6F1E4;
  --paper-dark: #EDE6D3;
  --ink: #1C2321;
  --ledger-green: #0F3D2E;
  --ledger-green-light: #1B5E45;
  --brass: #C9A227;
  --debit-red: #A63D40;
  --credit-green: #2E7D52;
}

.stApp {
  background-color: var(--paper);
}

/* ---------- Typography ---------- */
html, body, [class*="css"] {
  font-family: 'Inter', sans-serif;
  color: var(--ink);
}
h1, h2, h3 {
  font-family: 'Fraunces', serif !important;
  color: var(--ledger-green) !important;
  letter-spacing: -0.01em;
}

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] {
  background-color: var(--ledger-green);
}
[data-testid="stSidebar"] * {
  color: var(--paper) !important;
}
[data-testid="stSidebar"] input,
[data-testid="stSidebar"] textarea {
  color: var(--ink) !important;
}
[data-testid="stSidebar"] hr {
  border-color: rgba(246,241,228,0.2) !important;
}
[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] {
  background-color: rgba(246,241,228,0.06);
  border: 1px dashed rgba(201,162,39,0.5);
}

/* ---------- Ledger header banner ---------- */
.ledger-header {
  background: linear-gradient(135deg, var(--ledger-green) 0%, var(--ledger-green-light) 100%);
  border-radius: 14px;
  padding: 2.2rem 2.6rem;
  margin-bottom: 1.6rem;
  position: relative;
  overflow: hidden;
}
.ledger-header::after {
  content: "";
  position: absolute;
  inset: 0;
  background-image: repeating-linear-gradient(
    transparent, transparent 27px, rgba(201,162,39,0.09) 28px
  );
  pointer-events: none;
}
.ledger-eyebrow {
  font-family: 'IBM Plex Mono', monospace;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  font-size: 0.72rem;
  color: var(--brass);
  margin-bottom: 0.5rem;
  position: relative;
}
.ledger-header h1 {
  color: var(--paper) !important;
  font-family: 'Fraunces', serif !important;
  font-size: 2.7rem;
  font-weight: 700;
  margin: 0;
  position: relative;
}
.ledger-tagline {
  font-family: 'Inter', sans-serif;
  color: rgba(246,241,228,0.75);
  margin-top: 0.6rem;
  font-size: 0.98rem;
  max-width: 44rem;
  position: relative;
}
.ledger-seal {
  position: absolute;
  top: 1.4rem;
  right: 1.8rem;
  width: 62px;
  height: 62px;
  border: 2px solid var(--brass);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transform: rotate(-8deg);
  font-size: 1.7rem;
  background: rgba(201,162,39,0.08);
}

/* ---------- Metric cards ---------- */
[data-testid="stMetric"] {
  background: var(--paper-dark) !important;
  border: 1px solid rgba(15,61,46,0.15);
  border-top: 3px solid var(--brass);
  border-radius: 10px;
  padding: 1rem 1.2rem 0.9rem 1.2rem !important;
}
[data-testid="stMetricValue"] {
  font-family: 'IBM Plex Mono', monospace !important;
  color: var(--ledger-green) !important;
  font-weight: 600 !important;
}
[data-testid="stMetricLabel"] {
  font-family: 'IBM Plex Mono', monospace !important;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.72rem !important;
  opacity: 0.7;
}

/* ---------- Buttons ---------- */
.stButton button,
.stButton button p,
.stButton button span {
  font-family: 'Inter', sans-serif !important;
  color: var(--ledger-green) !important;
}
.stButton button {
  background: var(--paper-dark) !important;
  border: 1px solid rgba(15,61,46,0.25) !important;
  border-radius: 8px !important;
  font-weight: 500 !important;
}
.stButton button:hover {
  border-color: var(--brass) !important;
  background: #ffffff !important;
}
.stButton button[kind="primary"],
.stButton button[kind="primary"] p,
.stButton button[kind="primary"] span {
  color: var(--paper) !important;
}
.stButton button[kind="primary"] {
  background: var(--ledger-green) !important;
  border: none !important;
}
.stButton button[kind="primary"]:hover {
  background: var(--ledger-green-light) !important;
}
/* Sidebar's blanket text-color rule otherwise overrides button text
   (it targets every descendant element, including the <p>/<span> inside
   buttons, with higher priority than inherited color) — these selectors
   are more specific so sidebar buttons stay readable. */
[data-testid="stSidebar"] .stButton button,
[data-testid="stSidebar"] .stButton button p,
[data-testid="stSidebar"] .stButton button span {
  color: var(--ledger-green) !important;
}
[data-testid="stSidebar"] .stButton button[kind="primary"],
[data-testid="stSidebar"] .stButton button[kind="primary"] p,
[data-testid="stSidebar"] .stButton button[kind="primary"] span {
  color: var(--paper) !important;
}
/* Catch-all: any button in the sidebar (including the file uploader's
   "Browse files" button, which isn't a .stButton) stays readable. */
[data-testid="stSidebar"] button,
[data-testid="stSidebar"] button p,
[data-testid="stSidebar"] button span {
  color: var(--ledger-green) !important;
}

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab"] {
  font-family: 'IBM Plex Mono', monospace;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  font-size: 0.78rem;
  color: var(--ink);
}
.stTabs [aria-selected="true"] {
  color: var(--ledger-green) !important;
  font-weight: 600;
}
.stTabs [data-baseweb="tab-highlight"] {
  background-color: var(--brass) !important;
}

/* ---------- Chat ---------- */
[data-testid="stChatMessage"] {
  border-radius: 10px;
  border: 1px solid rgba(15,61,46,0.12);
  background: #ffffff;
}
[data-testid="stChatInput"] textarea {
  font-family: 'Inter', sans-serif;
}

/* ---------- Section headers (ledger-style rule) ---------- */
.ledger-section-title {
  font-family: 'Fraunces', serif;
  color: var(--ledger-green);
  font-size: 1.3rem;
  font-weight: 600;
  border-bottom: 2px solid var(--brass);
  padding-bottom: 0.3rem;
  margin: 1.4rem 0 0.9rem 0;
  display: inline-block;
}

/* ---------- Ledger callout (empty states / info) ---------- */
.ledger-note {
  background: var(--paper-dark);
  border-left: 3px solid var(--brass);
  border-radius: 6px;
  padding: 0.9rem 1.1rem;
  font-size: 0.92rem;
  color: var(--ink);
}

/* ---------- Chart card wrapper ---------- */
.ledger-chart-card {
  background: #ffffff;
  border: 1px solid rgba(15,61,46,0.15);
  border-radius: 10px;
  padding: 0.6rem 0.8rem 0.2rem 0.8rem;
  margin-bottom: 1rem;
}
</style>
"""

# Shared Plotly styling so charts match the ledger palette instead of default
# Plotly colors.
PLOTLY_COLORWAY = ["#0F3D2E", "#C9A227", "#A63D40", "#1B5E45", "#6B8F71", "#8C6D1F"]


def apply_ledger_chart_theme(fig):
    """
    Apply the ledger palette/fonts to a Plotly figure. Sets colors explicitly
    on every text element (not just the global font) because Streamlit's
    built-in Plotly theme overlay (and dark-mode) otherwise overrides unset
    properties. IMPORTANT: pass theme=None to st.plotly_chart() when using
    this, or Streamlit will re-apply its own theme on top and wash colors out.
    """
    ink = "#1C2321"
    fig.update_layout(
        colorway=PLOTLY_COLORWAY,
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(family="IBM Plex Mono, monospace", color=ink, size=13),
        title=dict(font=dict(color=ink)),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=ink, size=12)),
        margin=dict(t=30, b=20, l=10, r=10),
    )
    fig.update_xaxes(
        gridcolor="rgba(15,61,46,0.10)",
        zerolinecolor="rgba(15,61,46,0.2)",
        tickfont=dict(color=ink),
        title=dict(font=dict(color=ink)),
        linecolor="rgba(15,61,46,0.2)",
    )
    fig.update_yaxes(
        gridcolor="rgba(15,61,46,0.10)",
        zerolinecolor="rgba(15,61,46,0.2)",
        tickfont=dict(color=ink),
        title=dict(font=dict(color=ink)),
        linecolor="rgba(15,61,46,0.2)",
    )
    fig.update_traces(textfont_color="#ffffff", selector=dict(type="pie"))
    return fig
