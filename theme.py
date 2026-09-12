"""Visual identity and Plotly theme for Numera."""

LEDGER_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
  --navy-950: #081018;
  --navy-900: #0c151f;
  --navy-800: #121e2a;
  --navy-700: #1b2a38;
  --ink: #e7edf2;
  --muted: #91a0ad;
  --line: rgba(171, 191, 205, 0.16);
  --accent: #35c48b;
  --accent-soft: rgba(53, 196, 139, 0.14);
  --radius: 8px;
  --shadow: 0 10px 28px rgba(0, 0, 0, 0.16);
}

.stApp { background: var(--navy-950); }
html, body, [class*="css"] {
  font-family: 'DM Sans', sans-serif;
  color: var(--ink);
}
h1, h2, h3 { color: var(--ink) !important; letter-spacing: 0; }
p, label { line-height: 1.45; }

/* Sidebar */
[data-testid="stSidebar"] {
  background: var(--navy-900);
  border-right: 1px solid var(--line);
}
[data-testid="stSidebar"] * { color: var(--ink) !important; }
[data-testid="stSidebar"] input,
[data-testid="stSidebar"] textarea { color: var(--ink) !important; }
[data-testid="stSidebar"] [data-testid="stCaptionContainer"],
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] * { color: var(--muted) !important; }
[data-testid="stSidebar"] hr { border-color: var(--line) !important; margin: 1rem 0; }
[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] {
  background: transparent;
  border: 1px dashed rgba(53, 196, 139, 0.52);
  border-radius: var(--radius);
  padding: 0.7rem;
}
[data-testid="stSidebar"] [data-testid="stFileUploaderDropzoneInstructions"] {
  opacity: 0.78;
}
[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] button {
  background: var(--accent-soft) !important;
  border: 1px solid rgba(53, 196, 139, 0.35) !important;
  border-radius: 6px !important;
  color: var(--accent) !important;
}

/* Dashboard header */
.ledger-header {
  background: var(--navy-900);
  border: 1px solid var(--line);
  border-left: 3px solid var(--accent);
  border-radius: var(--radius);
  padding: 1.15rem 1.4rem;
  margin-bottom: 1.25rem;
  position: relative;
  box-shadow: var(--shadow);
}
.ledger-eyebrow {
  color: var(--accent);
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.68rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 0.25rem;
}
.ledger-header h1 {
  color: var(--ink) !important;
  font-family: 'Space Grotesk', sans-serif !important;
  font-size: 2.35rem;
  font-weight: 700;
  letter-spacing: -0.04em;
  margin: 0;
}
.ledger-tagline { color: var(--muted); font-size: 0.86rem; margin-top: 0.25rem; }
.ledger-seal {
  position: absolute;
  top: 50%;
  right: 1.35rem;
  transform: translateY(-50%);
  color: var(--accent);
  font-size: 1.3rem;
  opacity: 0.9;
}

/* Cards and numeric hierarchy */
[data-testid="stMetric"] {
  background: var(--navy-900) !important;
  border: 1px solid var(--line);
  border-top: 2px solid var(--accent);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 0.85rem 1rem 0.75rem !important;
}
[data-testid="stMetricValue"] {
  color: var(--ink) !important;
  font-family: 'IBM Plex Mono', monospace !important;
  font-variant-numeric: tabular-nums;
  font-weight: 600 !important;
}
[data-testid="stMetricLabel"] {
  color: var(--muted) !important;
  font-size: 0.72rem !important;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

/* Shared controls */
.stButton button, [data-testid="stDownloadButton"] button {
  background: var(--navy-800) !important;
  border: 1px solid var(--line) !important;
  border-radius: var(--radius) !important;
  color: var(--ink) !important;
  font-family: 'DM Sans', sans-serif !important;
  font-weight: 500 !important;
}
.stButton button:hover, [data-testid="stDownloadButton"] button:hover {
  background: var(--navy-700) !important;
  border-color: var(--accent) !important;
}
.stButton button[kind="primary"] {
  background: var(--accent) !important;
  border-color: var(--accent) !important;
  color: var(--navy-950) !important;
}
.stButton button[kind="primary"] p, .stButton button[kind="primary"] span { color: var(--navy-950) !important; }
[data-testid="stSidebar"] button { color: var(--ink) !important; }

/* Suggested questions read as one prompt surface */
[data-testid="stHorizontalBlock"] .stButton button {
  background: var(--navy-800) !important;
  border-color: rgba(53, 196, 139, 0.2) !important;
  border-radius: 0 !important;
  color: var(--muted) !important;
  font-size: 0.82rem !important;
  min-height: 2.7rem;
}
[data-testid="stHorizontalBlock"] > div:first-child .stButton button { border-radius: var(--radius) 0 0 var(--radius) !important; }
[data-testid="stHorizontalBlock"] > div:last-child .stButton button { border-radius: 0 var(--radius) var(--radius) 0 !important; }
[data-testid="stHorizontalBlock"] .stButton button:hover { color: var(--accent) !important; }
[data-testid="stChatInput"] {
  border-color: rgba(53, 196, 139, 0.4) !important;
  border-radius: var(--radius) !important;
  background: var(--navy-900) !important;
}
[data-testid="stChatInput"] textarea { color: var(--ink) !important; font-family: 'DM Sans', sans-serif; }

/* Tabs, messages, notes and charts */
.stTabs [data-baseweb="tab"] { color: var(--muted); font-size: 0.86rem; }
.stTabs [aria-selected="true"] { color: var(--accent) !important; font-weight: 600; }
.stTabs [data-baseweb="tab-highlight"] { background: var(--accent) !important; }
[data-testid="stChatMessage"] {
  background: var(--navy-900);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  margin-bottom: 0.6rem;
}
.ledger-section-title {
  color: var(--ink);
  font-size: 1.05rem;
  font-weight: 600;
  border-bottom: 1px solid var(--accent);
  padding-bottom: 0.3rem;
  margin: 1.2rem 0 0.75rem;
  display: inline-block;
}
.ledger-note {
  background: var(--navy-900);
  border-left: 2px solid var(--accent);
  border-radius: var(--radius);
  color: var(--muted);
  font-size: 0.86rem;
  padding: 0.75rem 0.95rem;
}
.ledger-chart-card {
  background: var(--navy-900);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  margin-bottom: 1rem;
  padding: 0.45rem 0.65rem 0.1rem;
}
[data-testid="stCaptionContainer"] { color: var(--muted) !important; font-size: 0.76rem; }
[data-testid="stDataFrame"] { border: 1px solid var(--line); border-radius: var(--radius); }
</style>
"""

PLOTLY_COLORWAY = ["#35C48B", "#D5A957", "#6EA8D9", "#E17878", "#A68BD4", "#91A0AD"]


def apply_ledger_chart_theme(fig):
    """Apply Numera colors and typography to a Plotly figure."""
    ink = "#E7EDF2"
    fig.update_layout(
        colorway=PLOTLY_COLORWAY,
        paper_bgcolor="#0C151F",
        plot_bgcolor="#0C151F",
        font=dict(family="DM Sans, sans-serif", color=ink, size=13),
        title=dict(font=dict(color=ink)),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=ink, size=12)),
        margin=dict(t=30, b=20, l=10, r=10),
    )
    fig.update_xaxes(
        gridcolor="rgba(171,191,205,0.12)",
        zerolinecolor="rgba(171,191,205,0.2)",
        tickfont=dict(color=ink),
        title=dict(font=dict(color=ink)),
        linecolor="rgba(171,191,205,0.2)",
    )
    fig.update_yaxes(
        gridcolor="rgba(171,191,205,0.12)",
        zerolinecolor="rgba(171,191,205,0.2)",
        tickfont=dict(color=ink),
        title=dict(font=dict(color=ink)),
        linecolor="rgba(171,191,205,0.2)",
    )
    fig.update_traces(textfont_color="#081018", selector=dict(type="pie"))
    return fig
