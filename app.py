"""
Gowtam R E — Futuristic AI Portfolio
Run: streamlit run app.py
"""

import base64, pathlib, streamlit as st
import plotly.graph_objects as go

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Gowtam R E | AI Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Asset Loader ─────────────────────────────────────────────────────────────
ASSETS = pathlib.Path(__file__).parent / "assets"

def b64(path, mime="image/jpeg"):
    try:
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f"data:{mime};base64,{data}"
    except:
        return ""

PROFILE_SRC = b64(ASSETS / "profile.png", "image/png")
RESUME_SRC  = b64(ASSETS / "Gowtam_R_E_FlowCV_Resume_2026-06-12.pdf",  "application/pdf")

# ─── Session State (page routing) ─────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ─── Global CSS ───────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
    background: #0A0A1A;
    color: #E6EDF3;
}}
.stApp {{ background: #0A0A1A; }}
#MainMenu, footer, header {{ visibility: hidden; }}
.block-container {{ padding: 0 !important; max-width: 100% !important; }}
section[data-testid="stSidebar"] {{
    background-color: #0D0D24 !important;
    border-right: 0.5px solid rgba(124,58,237,0.15) !important;
    width: 240px !important;
}}
section[data-testid="stSidebar"] > div {{
    background-color: #0D0D24 !important;
}}
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
    padding: 20px 10px !important;
}}

::-webkit-scrollbar {{ width: 3px; }}
::-webkit-scrollbar-track {{ background: #0A0A1A; }}
::-webkit-scrollbar-thumb {{ background: #7C3AED; border-radius: 2px; }}

/* ── Layout shell ── */
.shell {{
    display: flex;
    min-height: 100vh;
    background: #0A0A1A;
}}

/* ── Sidebar ── */
.sidebar {{
    width: 200px; flex-shrink: 0;
    background: #0D0D24;
    border-right: 0.5px solid rgba(124,58,237,0.15);
    display: flex; flex-direction: column;
    padding: 24px 0;
    position: fixed; top: 0; left: 0; height: 100vh; z-index: 100;
    overflow-y: auto;
}}
.sb-logo {{
    font-family: 'Inter', sans-serif; font-size: 22px; font-weight: 900;
    padding: 0 20px 24px;
    background: linear-gradient(135deg, #7C3AED, #A78BFA);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; letter-spacing: -0.02em;
}}
.sb-nav {{ flex: 1; display: flex; flex-direction: column; gap: 2px; padding: 0 12px; }}
.sb-item {{
    display: flex; align-items: center; gap: 10px;
    padding: 10px 12px; border-radius: 8px; cursor: pointer;
    font-size: 13px; color: rgba(230,237,243,0.45);
    transition: all .2s; text-decoration: none; border: none;
    background: transparent; width: 100%; text-align: left;
    font-family: 'Inter', sans-serif;
}}
.sb-item:hover {{ background: rgba(124,58,237,0.1); color: #E6EDF3; }}
.sb-item.active {{
    background: rgba(124,58,237,0.18);
    color: #A78BFA; font-weight: 500;
    border: 0.5px solid rgba(124,58,237,0.25);
}}
.sb-icon {{ font-size: 14px; width: 18px; text-align: center; }}
.sb-bottom {{ padding: 16px 20px; display: flex; gap: 12px; }}
.sb-social {{
    font-size: 14px; color: rgba(230,237,243,0.35);
    cursor: pointer; text-decoration: none; transition: color .2s;
}}
.sb-social:hover {{ color: #7C3AED; }}
.dark-toggle {{
    padding: 8px 20px; font-size: 11px;
    color: rgba(230,237,243,0.3);
    font-family: 'JetBrains Mono', monospace;
    display: flex; align-items: center; gap: 6px; margin-bottom: 8px;
}}

/* ── Main content ── */
.main {{
    flex: 1; padding: 24px;
    min-height: 100vh;
    background: #0A0A1A;
}}

/* ── Cards ── */
.card {{
    background: #0D0D24;
    border: 0.5px solid rgba(124,58,237,0.15);
    border-radius: 14px; padding: 20px;
    transition: border-color .25s;
}}
.card:hover {{ border-color: rgba(124,58,237,0.35); }}

/* ── Section headers ── */
.sh {{
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 16px;
}}
.sh-title {{
    display: flex; align-items: center; gap: 8px;
    font-size: 14px; font-weight: 600; color: #E6EDF3;
}}
.sh-icon {{ font-size: 16px; }}
.sh-link {{
    font-size: 11px; color: rgba(124,58,237,0.8);
    font-family: 'JetBrains Mono', monospace;
    cursor: pointer; text-decoration: none;
    display: flex; align-items: center; gap: 4px;
}}

/* ── Hero section ── */
.hero-role-tag {{
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(124,58,237,0.1); border: 0.5px solid rgba(124,58,237,0.25);
    color: rgba(230,237,243,0.6); font-size: 11px; font-family: 'JetBrains Mono', monospace;
    padding: 5px 14px; border-radius: 20px; margin-bottom: 14px;
}}
.hero-hi {{ font-size: 16px; color: rgba(230,237,243,0.55); margin-bottom: 4px; }}
.hero-name {{
    font-size: 40px; font-weight: 900; letter-spacing: -0.04em;
    line-height: 1.0; margin-bottom: 8px;
    background: linear-gradient(135deg, #A78BFA 0%, #7C3AED 40%, #C084FC 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}}
.hero-sub {{ font-size: 13px; color: rgba(230,237,243,0.5); margin-bottom: 20px; line-height: 1.6; }}
.hero-btns {{ display: flex; gap: 10px; margin-bottom: 24px; flex-wrap: wrap; }}
.btn-primary {{
    background: linear-gradient(135deg, #7C3AED, #6D28D9);
    color: #fff; font-size: 12px; font-weight: 500; padding: 10px 20px;
    border-radius: 8px; border: none; cursor: pointer; font-family: 'Inter', sans-serif;
    display: inline-flex; align-items: center; gap: 6px; text-decoration: none;
    transition: opacity .2s;
}}
.btn-primary:hover {{ opacity: .85; color: #fff; }}
.btn-outline {{
    background: transparent; color: #E6EDF3; font-size: 12px; font-weight: 500;
    padding: 10px 20px; border-radius: 8px;
    border: 0.5px solid rgba(124,58,237,0.4);
    cursor: pointer; font-family: 'Inter', sans-serif;
    display: inline-flex; align-items: center; gap: 6px; text-decoration: none;
}}
.hero-socials {{ display: flex; gap: 10px; }}
.social-btn {{
    width: 34px; height: 34px; border-radius: 50%;
    background: rgba(255,255,255,0.05);
    border: 0.5px solid rgba(255,255,255,0.1);
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; cursor: pointer; text-decoration: none;
    color: rgba(230,237,243,0.5); transition: all .2s;
}}
.social-btn:hover {{
    background: rgba(124,58,237,0.2);
    border-color: rgba(124,58,237,0.4); color: #A78BFA;
}}

/* ── Profile photo ── */
.profile-wrap {{
    position: relative; width: 200px; height: 200px;
    margin: 0 auto;
}}
.profile-glow {{
    width: 200px; height: 200px; border-radius: 50%;
    background: conic-gradient(from 0deg, #7C3AED, #A78BFA, #C084FC, #7C3AED);
    padding: 3px;
    box-shadow: 0 0 40px rgba(124,58,237,0.5), 0 0 80px rgba(124,58,237,0.2);
    animation: spin 8s linear infinite;
}}
@keyframes spin {{
    from {{ transform: rotate(0deg); }}
    to {{ transform: rotate(360deg); }}
}}
.profile-inner {{
    width: 100%; height: 100%; border-radius: 50%;
    overflow: hidden; background: #0D0D24;
}}
.profile-img {{
    width: 100%; height: 100%; object-fit: cover;
    object-position: top center; border-radius: 50%;
}}

/* ── Stats bar ── */
.stats-bar {{
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 12px; margin-top: 16px;
}}
.stat-box {{
    background: rgba(124,58,237,0.08);
    border: 0.5px solid rgba(124,58,237,0.2);
    border-radius: 10px; padding: 12px 10px; text-align: center;
}}
.stat-num {{
    font-size: 20px; font-weight: 700; color: #A78BFA;
    font-family: 'JetBrains Mono', monospace; line-height: 1;
}}
.stat-lbl {{ font-size: 9px; color: rgba(230,237,243,0.4); margin-top: 3px; }}

/* ── About bullets ── */
.about-item {{
    display: flex; align-items: center; gap: 10px;
    padding: 7px 0; border-bottom: 0.5px solid rgba(255,255,255,0.04);
    font-size: 12px; color: rgba(230,237,243,0.65);
}}
.about-dot {{
    width: 7px; height: 7px; border-radius: 50%;
    flex-shrink: 0;
}}

/* ── Skill tabs ── */
.skill-tabs {{ display: flex; gap: 6px; margin-bottom: 16px; flex-wrap: wrap; }}
.skill-tab {{
    font-size: 10px; padding: 5px 12px; border-radius: 20px;
    cursor: pointer; font-family: 'JetBrains Mono', monospace;
    border: 0.5px solid rgba(255,255,255,0.1);
    background: transparent; color: rgba(230,237,243,0.45);
    transition: all .2s;
}}
.skill-tab.active {{
    background: rgba(124,58,237,0.2);
    border-color: rgba(124,58,237,0.45); color: #A78BFA;
}}

/* ── Circular skill ── */
.skill-circles {{
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 10px; margin-bottom: 10px;
}}
.circ-wrap {{ text-align: center; }}
.circ-label {{ font-size: 10px; color: rgba(230,237,243,0.55); margin-top: 5px; }}

/* ── Project cards ── */
.proj-card {{
    background: #0D0D24;
    border: 0.5px solid rgba(124,58,237,0.15);
    border-radius: 12px; overflow: hidden; transition: all .25s;
}}
.proj-card:hover {{
    border-color: rgba(124,58,237,0.45);
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(124,58,237,0.15);
}}
.proj-img {{
    width: 100%; height: 120px; object-fit: cover;
    background: linear-gradient(135deg, #1a0a3e, #0a1a3e);
    display: flex; align-items: center; justify-content: center;
    font-size: 32px;
}}
.proj-body {{ padding: 14px; }}
.proj-name {{ font-size: 12px; font-weight: 600; margin-bottom: 5px; }}
.proj-desc {{ font-size: 10px; color: rgba(230,237,243,0.45); line-height: 1.55; margin-bottom: 10px; }}
.proj-footer {{ display: flex; gap: 6px; flex-wrap: wrap; }}
.proj-btn {{
    font-size: 9px; padding: 4px 10px; border-radius: 4px;
    border: 0.5px solid rgba(124,58,237,0.3); color: #A78BFA;
    background: rgba(124,58,237,0.08); cursor: pointer; font-family: 'JetBrains Mono', monospace;
    text-decoration: none; transition: background .2s;
}}
.proj-btn:hover {{ background: rgba(124,58,237,0.18); }}

/* ── Timeline ── */
.timeline-item {{
    display: flex; gap: 14px; margin-bottom: 16px; align-items: flex-start;
}}
.tl-year {{
    font-family: 'JetBrains Mono', monospace; font-size: 12px;
    color: #7C3AED; font-weight: 600; width: 36px; flex-shrink: 0; padding-top: 2px;
}}
.tl-dot-col {{
    display: flex; flex-direction: column; align-items: center; gap: 0;
    flex-shrink: 0;
}}
.tl-dot {{
    width: 10px; height: 10px; border-radius: 50%;
    background: #7C3AED; border: 2px solid rgba(124,58,237,0.3);
    flex-shrink: 0;
}}
.tl-line {{ width: 1px; background: rgba(124,58,237,0.2); flex: 1; min-height: 30px; }}
.tl-content {{ flex: 1; }}
.tl-title {{ font-size: 12px; font-weight: 600; margin-bottom: 2px; }}
.tl-desc {{ font-size: 10px; color: rgba(230,237,243,0.45); line-height: 1.55; }}

/* ── Tech stack constellation ── */
.tech-node {{
    position: absolute; background: rgba(124,58,237,0.12);
    border: 0.5px solid rgba(124,58,237,0.3); border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 10px; font-family: 'JetBrains Mono', monospace;
    color: #A78BFA; font-weight: 500; transition: all .2s; cursor: default;
}}

/* ── Cert cards ── */
.cert-card {{
    background: #0D0D24; border: 0.5px solid rgba(124,58,237,0.12);
    border-radius: 10px; padding: 14px; text-align: center;
    transition: all .2s; min-width: 0;
}}
.cert-card:hover {{ border-color: rgba(124,58,237,0.35); }}
.cert-logo {{
    font-size: 22px; margin-bottom: 8px; display: block;
}}
.cert-name {{ font-size: 10px; font-weight: 500; margin-bottom: 3px; line-height: 1.4; }}
.cert-org {{ font-size: 9px; color: rgba(230,237,243,0.35); font-family: 'JetBrains Mono', monospace; }}
.cert-date {{ font-size: 8px; color: rgba(124,58,237,0.6); margin-top: 4px; }}

/* ── GitHub analytics ── */
.gh-stat {{
    background: rgba(255,255,255,0.03); border: 0.5px solid rgba(255,255,255,0.06);
    border-radius: 7px; padding: 10px 8px; text-align: center;
}}
.gh-num {{
    font-size: 18px; font-weight: 700; color: #A78BFA;
    font-family: 'JetBrains Mono', monospace;
}}
.gh-lbl {{ font-size: 9px; color: rgba(230,237,243,0.35); margin-top: 2px; }}
.contrib-grid {{
    display: grid;
    grid-template-columns: repeat(26, 1fr);
    gap: 2px; margin-top: 10px;
}}
.contrib-cell {{
    width: 100%; aspect-ratio: 1;
    border-radius: 2px;
}}

/* ── AI Assistant ── */
.ai-chat {{ max-height: 180px; overflow-y: auto; margin-bottom: 10px; }}
.ai-msg {{
    font-size: 11px; color: rgba(230,237,243,0.7);
    background: rgba(124,58,237,0.08); border-radius: 8px;
    padding: 8px 12px; margin-bottom: 6px; line-height: 1.55;
}}
.ai-suggestion {{
    font-size: 10px; color: rgba(230,237,243,0.45);
    background: rgba(255,255,255,0.03); border: 0.5px solid rgba(255,255,255,0.08);
    border-radius: 6px; padding: 6px 10px; cursor: pointer;
    margin-bottom: 5px; transition: all .2s; display: block;
    width: 100%; text-align: left; font-family: 'Inter', sans-serif;
}}
.ai-suggestion:hover {{
    background: rgba(124,58,237,0.1); border-color: rgba(124,58,237,0.3);
    color: #A78BFA;
}}

/* ── Contact ── */
.contact-item {{
    display: flex; align-items: center; gap: 10px; padding: 10px 0;
    border-bottom: 0.5px solid rgba(255,255,255,0.04); font-size: 12px;
    color: rgba(230,237,243,0.65);
}}
.contact-icon {{
    width: 30px; height: 30px; border-radius: 7px;
    background: rgba(124,58,237,0.1); border: 0.5px solid rgba(124,58,237,0.2);
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; flex-shrink: 0;
}}

/* ── Resume preview ── */
.resume-dl {{
    display: block; text-align: center;
    background: linear-gradient(135deg, #7C3AED, #6D28D9);
    color: #fff; font-size: 13px; font-weight: 500;
    padding: 12px 0; border-radius: 10px;
    text-decoration: none; margin-bottom: 10px;
    font-family: 'Inter', sans-serif; transition: opacity .2s;
}}
.resume-dl:hover {{ opacity: .85; color: #fff; }}

/* ── Achievement badges ── */
.ach-card {{
    background: rgba(124,58,237,0.08); border: 0.5px solid rgba(124,58,237,0.2);
    border-radius: 10px; padding: 16px; text-align: center;
}}
.ach-num {{
    font-size: 28px; font-weight: 700;
    background: linear-gradient(135deg, #A78BFA, #7C3AED);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; font-family: 'JetBrains Mono', monospace;
}}
.ach-lbl {{ font-size: 10px; color: rgba(230,237,243,0.5); margin-top: 4px; line-height: 1.4; }}

/* ── Pulsing live dot ── */
.live-dot {{
    width: 7px; height: 7px; border-radius: 50%; background: #34D399;
    box-shadow: 0 0 8px #34D399; display: inline-block;
    animation: pulse 2s infinite;
}}
@keyframes pulse {{ 0%,100%{{opacity:1}} 50%{{opacity:.25}} }}

/* ── Lang badges ── */
.lang-b {{
    font-size: 9px; padding: 3px 9px; border-radius: 3px;
    font-family: 'JetBrains Mono', monospace; border: 0.5px solid;
}}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  DATA
# ═══════════════════════════════════════════════════════════════════════════════
NAV_ITEMS = [
    ("🏠", "Home"), ("👤", "About"), ("⚡", "Skills"), ("📁", "Projects"),
    ("🏆", "Certifications"), ("💼", "Experience"), ("📊", "Analytics"),
    ("📄", "Resume"), ("✉️", "Contact"),
]

SKILLS_ALL = {
    "All": {
        "Python": 95, "Java": 75, "Machine Learning": 90, "Digital Image Processing": 80,
        "FastAPI": 85, "SQL/MySQL": 80, "ESP32/IoT": 85, "Streamlit": 90,
    },
    "AI/ML": {"Python": 95, "Scikit-learn": 88, "OpenCV": 85, "NumPy": 90, "Matplotlib": 82},
    "Languages": {"Python": 95, "Java": 75, "HTML5": 85, "CSS3": 85},
    "Tools & IDEs": {"VS Code": 90, "PyCharm": 85, "Jupyter Notebook": 88, "Google Colab": 85, "Git/GitHub": 88},
    "Core Concepts": {"Machine Learning": 90, "Data Preprocessing": 88, "Data Visualization": 85, "Digital Image Processing": 80},
}

PROJECTS = [
    {"icon": "☀️", "name": "SolarTrack Pro", "badge": "IoT · ML",
     "desc": "ESP32 dual-axis solar tracker with React, FastAPI, MongoDB, and ML-based angle prediction.", 
     "tags": ["ESP32","React","FastAPI","MongoDB"], "color": "#1a2a4e"},
    {"icon": "🌊", "name": "Wastewater Dashboard", "badge": "IoT",
     "desc": "Real-time IoT monitoring with ESP32 + WebSockets and Random Forest anomaly detection.",
     "tags": ["ESP32","Node.js","WebSockets","RF"], "color": "#0a2a1e"},
    {"icon": "🏥", "name": "MedAI Clinical System", "badge": "Healthcare AI",
     "desc": "FastAPI + SQLite healthcare platform with AI medicine recommendations and risk analysis.",
     "tags": ["Python","FastAPI","SQLite","ML"], "color": "#2a0a1e"},
    {"icon": "🎬", "name": "Netflix EDA Notebook", "badge": "Data",
     "desc": "Comprehensive EDA on Netflix dataset — trends, content distribution, and visualised insights.",
     "tags": ["Pandas","Seaborn","Colab"], "color": "#1a0a2e"},
    {"icon": "💊", "name": "Medicine Recommender", "badge": "ML",
     "desc": "Multi-classifier pipeline with FastAPI REST layer and safety rules engine on synthetic data.",
     "tags": ["Python","Scikit-learn","FastAPI"], "color": "#2a1a0a"},
    {"icon": "🏦", "name": "Banking Application", "badge": "Python · SQL",
     "desc": "Full-featured banking system with account management and relational SQL backend.",
     "tags": ["Python","SQL","OOP"], "color": "#0a1a2a"},
]

TIMELINE = [
    {"year": "2026", "title": "Bachelor of Computer Science (AI)", "desc": "Completing Bachelor of Computer Science in Artificial Intelligence at B.S. Abdur Rahman Crescent Institute of Science and Technology, Chennai"},
    {"year": "2025", "title": "Lenovo India Internship", "desc": "Production & Quality Control Associate — hardware assembly and testing in Pondicherry"},
    {"year": "2024", "title": "AI/ML Projects & Internship", "desc": "Built SolarTrack Pro, Wastewater Dashboard, MedAI system. AI/ML Intern at Pluto Academy."},
    {"year": "2023", "title": "Started AI Studies", "desc": "Joined B.S. Abdur Rahman Crescent Institute of Science and Technology — began AI, Python, ML, and data engineering journey"},
]

CERTS = [
    {"icon": "🔵", "name": "Web Development Fundamentals", "org": "IBM SkillsBuild", "date": "Mar 2025", "color": "#001a3e"},
    {"icon": "🔵", "name": "AI Fundamentals", "org": "IBM SkillsBuild", "date": "2025", "color": "#001a3e"},
    {"icon": "🔵", "name": "Project Management Fundamentals", "org": "IBM SkillsBuild", "date": "2025", "color": "#001a3e"},
    {"icon": "🍃", "name": "MongoDB Basics for Students", "org": "MongoDB University", "date": "Jul 2025", "color": "#00200e"},
    {"icon": "🌐", "name": "HTML Essentials", "org": "Cisco Networking Academy", "date": "Apr 2025", "color": "#001e28"},
    {"icon": "🌐", "name": "CSS Essentials", "org": "Cisco Networking Academy", "date": "Apr 2025", "color": "#001e28"},
    {"icon": "🎓", "name": "ESP32 for IoT — Real World", "org": "Udemy", "date": "Mar 2026", "color": "#1a0a28"},
    {"icon": "🔴", "name": "Oracle Certified Foundations", "org": "Oracle University", "date": "2025", "color": "#200a00"},
]

# ═══════════════════════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def circular_chart(value, label, color="#7C3AED", size=100):
    """SVG circular progress indicator."""
    r = 36; cx = cy = 50
    circumference = 2 * 3.14159 * r
    fill = circumference * (1 - value / 100)
    return f"""
    <div style="text-align:center;width:{size}px;display:inline-block;">
      <svg viewBox="0 0 100 100" width="{size}" height="{size}">
        <circle cx="{cx}" cy="{cy}" r="{r}"
          fill="none" stroke="rgba(124,58,237,0.1)" stroke-width="7"/>
        <circle cx="{cx}" cy="{cy}" r="{r}"
          fill="none" stroke="{color}" stroke-width="7"
          stroke-dasharray="{circumference}"
          stroke-dashoffset="{fill}"
          stroke-linecap="round"
          transform="rotate(-90 {cx} {cy})"/>
        <text x="{cx}" y="{cy+5}" text-anchor="middle"
          font-size="16" font-weight="700" fill="{color}"
          font-family="JetBrains Mono, monospace">{value}%</text>
      </svg>
      <div style="font-size:10px;color:rgba(230,237,243,0.55);margin-top:3px;">{label}</div>
    </div>
    """

def contrib_heatmap():
    """Generate a GitHub-style contribution heatmap."""
    import random
    random.seed(42)
    cells = ""
    months = ["Jan","Feb","Mar","Apr","May","Jun"]
    for week in range(26):
        for day in range(5):
            intensity = random.choices(
                [0,1,2,3,4], weights=[30,20,20,15,15])[0]
            colors = {
                0: "rgba(255,255,255,0.04)",
                1: "rgba(124,58,237,0.2)",
                2: "rgba(124,58,237,0.4)",
                3: "rgba(124,58,237,0.65)",
                4: "rgba(124,58,237,0.9)",
            }
            cells += f'<div style="width:9px;height:9px;border-radius:2px;background:{colors[intensity]};"></div>'
    return cells

# ═══════════════════════════════════════════════════════════════════════════════
#  RENDER
# ═══════════════════════════════════════════════════════════════════════════════

page = st.session_state.page

from streamlit_option_menu import option_menu

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sb-logo" style="text-align: center; margin-bottom: 20px;">Gowtam R E</div>', unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,
        options=[item[1] for item in NAV_ITEMS],
        icons=["house", "person", "lightning", "folder", "trophy", "briefcase", "bar-chart", "file-earmark", "envelope"],
        menu_icon=None,
        default_index=[item[1] for item in NAV_ITEMS].index(page),
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "rgba(230,237,243,0.45)", "font-size": "14px"}, 
            "nav-link": {
                "font-size": "13px",
                "text-align": "left",
                "margin": "4px 0px",
                "color": "rgba(230,237,243,0.45)",
                "font-family": "Inter, sans-serif",
                "padding": "10px 12px",
                "border-radius": "8px",
            },
            "nav-link-selected": {
                "background-color": "rgba(124,58,237,0.18)",
                "color": "#A78BFA",
                "border": "0.5px solid rgba(124,58,237,0.25)",
                "font-weight": "500",
            },
        }
    )
    
    if selected != page:
        st.session_state.page = selected
        st.rerun()
        
    st.markdown('<div style="height: 60px;"></div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="padding: 20px 0 10px 0; display: flex; justify-content: center; gap: 15px; border-top: 0.5px solid rgba(124,58,237,0.15);">
        <a class="sb-social" href="https://www.linkedin.com/in/gowtam-r-e-26a7a2296/" target="_blank" style="font-size: 16px;">in</a>
        <a class="sb-social" href="https://github.com/Gowtam3016" target="_blank" style="font-size: 16px;">⌥</a>
        <a class="sb-social" href="mailto:regowtam@gmail.com" style="font-size: 16px;">✉</a>
    </div>
    """, unsafe_allow_html=True)

# ── Main wrapper ──────────────────────────────────────────────────────────────
st.markdown('<div class="main">', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  HOME PAGE
# ══════════════════════════════════════════════════════════════════════════════
if page == "Home":

    # Row 1: Hero | About Me | Skills (3 cols)
    c1, c2, c3 = st.columns([1.1, 1, 1], gap="small")

    with c1:
        st.markdown(f"""
        <div class="card" style="height:100%;">
          <div class="hero-role-tag">AI Engineer | Data Engineer | Full Stack Developer</div>
          <div class="hero-hi">Hi, I'm</div>
          <div class="hero-name">Gowtam R E</div>
          <div class="hero-sub">Building intelligent solutions<br>with AI and modern technologies</div>
          <div class="hero-btns">
            <a class="btn-primary" href="{RESUME_SRC}" download="Gowtam_R_E_Resume.pdf">⬇ Download Résumé</a>
            <a class="btn-outline" href="#">🚀 View Projects</a>
          </div>
          <div class="hero-socials">
            <a class="social-btn" href="https://www.linkedin.com/in/gowtam-r-e-26a7a2296/" target="_blank">in</a>
            <a class="social-btn" href="https://github.com/Gowtam3016" target="_blank">⌥</a>
            <a class="social-btn" href="#">🐦</a>
            <a class="social-btn" href="mailto:regowtam@gmail.com">✉</a>
          </div>
          <div class="stats-bar">
            <div class="stat-box"><div class="stat-num">6+</div><div class="stat-lbl">Projects</div></div>
            <div class="stat-box"><div class="stat-num">8</div><div class="stat-lbl">Certifications</div></div>
            <div class="stat-box"><div class="stat-num">15+</div><div class="stat-lbl">Technologies</div></div>
            <div class="stat-box"><div class="stat-num">2</div><div class="stat-lbl">Internships</div></div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        # Profile photo + about
        st.markdown(f"""
        <div class="card" style="text-align:center;padding-bottom:16px;">
          <div style="display:flex;justify-content:center;margin-bottom:16px;">
            <div class="profile-glow">
              <div class="profile-inner">
                <img class="profile-img" src="{PROFILE_SRC}" alt="Gowtam R E"/>
              </div>
            </div>
          </div>
          <div class="sh-title" style="justify-content:flex-start;margin-bottom:10px;">
            <span>👤</span><span>About Me</span>
          </div>
          <div style="text-align:left;">
            <div class="about-item">
              <div class="about-dot" style="background:#7C3AED;"></div>AI/ML Enthusiast — Bachelor of Computer Science in AI, Crescent Institute
            </div>
            <div class="about-item">
              <div class="about-dot" style="background:#A78BFA;"></div>Machine Learning &amp; Data Engineering
            </div>
            <div class="about-item">
              <div class="about-dot" style="background:#60A5FA;"></div>IoT &amp; Embedded Systems (ESP32)
            </div>
            <div class="about-item">
              <div class="about-dot" style="background:#34D399;"></div>Full Stack Development
            </div>
            <div class="about-item">
              <div class="about-dot" style="background:#F59E0B;"></div>2 Internships · Lenovo India, Pluto Academy
            </div>
            <div style="margin-top:12px;display:flex;flex-wrap:wrap;gap:5px;">
              <span class="lang-b" style="background:rgba(245,158,11,.08);border-color:rgba(245,158,11,.25);color:#F59E0B;">Tamil</span>
              <span class="lang-b" style="background:rgba(124,58,237,.08);border-color:rgba(124,58,237,.25);color:#A78BFA;">English</span>
              <span class="lang-b" style="background:rgba(59,130,246,.08);border-color:rgba(59,130,246,.25);color:#60A5FA;">Français</span>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        skills_tab = st.session_state.get("skill_tab", "All")
        sk_data = SKILLS_ALL.get(skills_tab, SKILLS_ALL["All"])
        items = list(sk_data.items())[:8]

        circles_html = '<div class="skill-circles">'
        colors = ["#7C3AED","#A78BFA","#60A5FA","#34D399","#F59E0B","#F87171","#C084FC","#818CF8"]
        for i, (name, val) in enumerate(items):
            circles_html += circular_chart(val, name, colors[i % len(colors)], size=90)
        circles_html += '</div>'

        tab_btns = ""
        for t in SKILLS_ALL.keys():
            active = "active" if t == skills_tab else ""
            tab_btns += f'<span class="skill-tab {active}">{t}</span>'

        st.markdown(f"""
        <div class="card" style="height:100%;">
          <div class="sh">
            <div class="sh-title"><span>⚡</span><span>Skills</span></div>
            <a class="sh-link" href="#">View All →</a>
          </div>
          <div class="skill-tabs">{tab_btns}</div>
          {circles_html}
        </div>
        """, unsafe_allow_html=True)
        for t in SKILLS_ALL.keys():
            if st.button(t, key=f"sktab_{t}"):
                st.session_state.skill_tab = t
                st.rerun()

    st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)

    # Row 2: Projects | Timeline | Tech Stack | GitHub Analytics
    c4, c5, c6, c7 = st.columns([1.4, 1, 0.8, 0.9], gap="small")

    with c4:
        proj_html = '<div class="sh"><div class="sh-title"><span>📁</span><span>Projects</span></div><a class="sh-link" href="#">View All Projects →</a></div>'
        proj_html += '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;">'
        for p in PROJECTS[:3]:
            tags_html = "".join(f'<span style="font-size:8px;color:rgba(230,237,243,0.3);background:rgba(124,58,237,0.08);padding:2px 6px;border-radius:3px;font-family:JetBrains Mono,monospace;">{t}</span>' for t in p["tags"][:2])
            proj_html += f"""
            <div class="proj-card">
              <div class="proj-img" style="background:linear-gradient(135deg,{p['color']},#0a0a1a);height:90px;">
                <span style="font-size:28px;">{p['icon']}</span>
              </div>
              <div class="proj-body">
                <div class="proj-name">{p['name']}</div>
                <div class="proj-desc">{p['desc'][:70]}...</div>
                <div class="proj-footer">
                  <a class="proj-btn" href="https://github.com/Gowtam3016" target="_blank">⌥ GitHub</a>
                  <a class="proj-btn" href="#">▶ Demo</a>
                </div>
              </div>
            </div>"""
        proj_html += '</div>'
        st.markdown(f'<div class="card">{proj_html}</div>', unsafe_allow_html=True)

    with c5:
        tl_html = '<div class="sh"><div class="sh-title"><span>📅</span><span>Experience Timeline</span></div></div>'
        for i, t in enumerate(TIMELINE):
            is_last = (i == len(TIMELINE)-1)
            tl_html += f"""
            <div class="timeline-item">
              <div class="tl-year">{t['year']}</div>
              <div class="tl-dot-col">
                <div class="tl-dot"></div>
                {'<div class="tl-line"></div>' if not is_last else ''}
              </div>
              <div class="tl-content">
                <div class="tl-title">{t['title']}</div>
                <div class="tl-desc">{t['desc']}</div>
              </div>
            </div>"""
        st.markdown(f'<div class="card">{tl_html}</div>', unsafe_allow_html=True)

    with c6:
        # Tech Stack constellation (plotly)
        nodes = [
            ("Python", 0, 0, 22, "#7C3AED"),
            ("AI/ML", 0, -1.3, 14, "#A78BFA"),
            ("SQL", -1.2, -0.4, 12, "#60A5FA"),
            ("IoT", 1.2, -0.4, 12, "#34D399"),
            ("FastAPI", -1.0, 0.9, 11, "#F59E0B"),
            ("Web Dev", 1.0, 0.9, 11, "#F87171"),
            ("Streamlit", 0, 1.4, 11, "#C084FC"),
        ]
        edges = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,4),(2,4),(3,5)]
        fig = go.Figure()
        for a, b in edges:
            fig.add_trace(go.Scatter(
                x=[nodes[a][1], nodes[b][1]], y=[nodes[a][2], nodes[b][2]],
                mode="lines", line=dict(color="rgba(124,58,237,0.2)", width=1),
                hoverinfo="none", showlegend=False))
        for name, x, y, size, color in nodes:
            fig.add_trace(go.Scatter(
                x=[x], y=[y], mode="markers+text",
                marker=dict(size=size, color=color, opacity=0.9),
                text=[name], textposition="top center",
                textfont=dict(size=9, color=color, family="JetBrains Mono"),
                hoverinfo="text", showlegend=False))
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=5,r=5,t=5,b=5), height=240,
            xaxis=dict(visible=False, range=[-1.9,1.9]),
            yaxis=dict(visible=False, range=[-1.8,2.0]))
        st.markdown('<div class="card"><div class="sh-title" style="margin-bottom:8px;"><span>🔗</span><span>Tech Stack</span></div>', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
        st.markdown('<a class="sh-link" style="display:flex;justify-content:center;padding:4px 0;" href="#">View Full Tech Stack →</a></div>', unsafe_allow_html=True)

    with c7:
        contrib_cells = contrib_heatmap()
        st.markdown(f"""
        <div class="card">
          <div class="sh-title" style="margin-bottom:12px;"><span>📊</span><span>GitHub Analytics</span></div>
          <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:7px;margin-bottom:14px;">
            <div class="gh-stat"><div class="gh-num">12+</div><div class="gh-lbl">Repositories</div></div>
            <div class="gh-stat"><div class="gh-num">200+</div><div class="gh-lbl">Contributions</div></div>
            <div class="gh-stat"><div class="gh-num">45+</div><div class="gh-lbl">Stars</div></div>
            <div class="gh-stat"><div class="gh-num">15+</div><div class="gh-lbl">Followers</div></div>
          </div>
          <div style="font-size:10px;color:rgba(230,237,243,0.3);margin-bottom:6px;font-family:'JetBrains Mono',monospace;">Contribution Activity</div>
          <div style="display:grid;grid-template-columns:repeat(26,1fr);gap:2px;">
            {contrib_cells}
          </div>
          <div style="margin-top:10px;">
            <div style="font-size:10px;color:rgba(230,237,243,0.3);margin-bottom:6px;font-family:'JetBrains Mono',monospace;">Top Languages</div>
            <div style="display:flex;align-items:center;gap:4px;flex-wrap:wrap;font-size:9px;font-family:'JetBrains Mono',monospace;color:rgba(230,237,243,0.5);">
              <span style="color:#3572A5;">Python</span> 45%
              <span style="color:#F1E05A;margin-left:6px;">JS</span> 20%
              <span style="color:#E34C26;margin-left:6px;">HTML</span> 15%
              <span style="margin-left:6px;">Others</span> 20%
            </div>
            <div style="height:6px;border-radius:3px;background:rgba(255,255,255,0.06);margin-top:5px;overflow:hidden;">
              <div style="height:100%;width:45%;background:#3572A5;border-radius:3px;display:inline-block;"></div>
              <div style="height:100%;width:20%;background:#F1E05A;border-radius:3px;display:inline-block;"></div>
              <div style="height:100%;width:15%;background:#E34C26;border-radius:3px;display:inline-block;"></div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)

    # Row 3: Certifications | Achievements | AI Assistant | Contact
    c8, c9, c10, c11 = st.columns([1.5, 0.9, 1, 0.9], gap="small")

    with c8:
        cert_html = '<div class="sh"><div class="sh-title"><span>🏆</span><span>Certifications</span></div><a class="sh-link" href="#">View All →</a></div>'
        cert_html += '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;">'
        for c in CERTS[:4]:
            cert_html += f"""
            <div class="cert-card" style="background:rgba(13,13,36,1);border-color:rgba(124,58,237,0.15);">
              <div class="cert-logo" style="font-size:20px;">{c['icon']}</div>
              <div class="cert-name">{c['name']}</div>
              <div class="cert-org">{c['org']}</div>
              <div class="cert-date">{c['date']}</div>
            </div>"""
        cert_html += '</div><div style="display:flex;justify-content:center;gap:6px;margin-top:8px;">'
        for i in range(4):
            cert_html += f'<div style="width:{"20px" if i==0 else "8px"};height:4px;border-radius:2px;background:{"#7C3AED" if i==0 else "rgba(124,58,237,0.2)"};"></div>'
        cert_html += '</div>'
        st.markdown(f'<div class="card">{cert_html}</div>', unsafe_allow_html=True)

    with c9:
        st.markdown("""
        <div class="card">
          <div class="sh-title" style="margin-bottom:12px;"><span>🥇</span><span>Achievements</span></div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
            <div class="ach-card">
              <div class="ach-num">6+</div>
              <div class="ach-lbl">Projects Completed</div>
            </div>
            <div class="ach-card">
              <div class="ach-num">8</div>
              <div class="ach-lbl">Certifications Earned</div>
            </div>
            <div class="ach-card">
              <div class="ach-num">15+</div>
              <div class="ach-lbl">Technologies Mastered</div>
            </div>
            <div class="ach-card">
              <div class="ach-num">2</div>
              <div class="ach-lbl">Internships Done</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with c10:
        if "ai_messages" not in st.session_state:
            st.session_state.ai_messages = ["👋 Hi! I'm Gowtam's AI Assistant. Ask me anything about him."]

        msgs_html = "".join(f'<div class="ai-msg">{m}</div>' for m in st.session_state.ai_messages[-3:])
        st.markdown(f"""
        <div class="card">
          <div class="sh-title" style="margin-bottom:10px;"><span>🤖</span><span>AI Assistant</span></div>
          <div class="ai-chat">{msgs_html}</div>
          <div style="font-size:10px;color:rgba(230,237,243,0.28);margin-bottom:6px;font-family:'JetBrains Mono',monospace;">Suggested questions:</div>
        </div>
        """, unsafe_allow_html=True)
        qs = ["What projects has Gowtam built?", "What are his skills?", "Tell me about his experience"]
        for q in qs:
            if st.button(q, key=f"ai_{q[:20]}", use_container_width=True):
                answers = {
                    "What projects has Gowtam built?": "Gowtam built SolarTrack Pro (IoT solar tracker), Wastewater Dashboard, MedAI Clinical System, Netflix EDA Notebook, Medicine Recommender, and a Banking Application.",
                    "What are his skills?": "Python (95%), ML/AI (90%), FastAPI (85%), Streamlit (90%), SQL (80%), ESP32/IoT (80%), Node.js (80%), and more.",
                    "Tell me about his experience": "Gowtam interned at Lenovo India (Production QC, Jun 2025, Pondicherry) and Pluto Academy (AI/ML — Movie Recommender + Heart Disease Predictor)."
                }
                st.session_state.ai_messages.append(f"You: {q}")
                st.session_state.ai_messages.append(answers.get(q, "Great question! Let me think..."))
                st.rerun()
        user_q = st.text_input("Ask a question...", key="ai_input", label_visibility="collapsed", placeholder="Ask a question...")
        if user_q:
            st.session_state.ai_messages.append(f"You: {user_q}")
            st.session_state.ai_messages.append("That's a great question about Gowtam! He's an AI engineer based in Chennai, passionate about building intelligent systems.")
            st.rerun()

    with c11:
        st.markdown(f"""
        <div class="card">
          <div class="sh-title" style="margin-bottom:12px;"><span>✉️</span><span>Contact Me</span></div>
          <div class="contact-item">
            <div class="contact-icon">📧</div>
            <div><div style="font-size:9px;color:rgba(230,237,243,0.35);">Email</div>regowtam@gmail.com</div>
          </div>
          <div class="contact-item">
            <div class="contact-icon">💼</div>
            <div><div style="font-size:9px;color:rgba(230,237,243,0.35);">LinkedIn</div>
            <a href="https://www.linkedin.com/in/gowtam-r-e-26a7a2296/" style="color:#A78BFA;font-size:11px;">linkedin.com/in/gowtam-r-e</a></div>
          </div>
          <div class="contact-item">
            <div class="contact-icon">⌥</div>
            <div><div style="font-size:9px;color:rgba(230,237,243,0.35);">GitHub</div>
            <a href="https://github.com/Gowtam3016" style="color:#A78BFA;font-size:11px;">github.com/Gowtam3016</a></div>
          </div>
          <div class="contact-item">
            <div class="contact-icon">📞</div>
            <div><div style="font-size:9px;color:rgba(230,237,243,0.35);">Phone</div>+91 79041 14369</div>
          </div>
          <div class="contact-item" style="border:none;">
            <div class="contact-icon">📍</div>
            <div><div style="font-size:9px;color:rgba(230,237,243,0.35);">Location</div>Chennai, India</div>
          </div>
          <div style="margin-top:12px;">
            <div style="display:flex;align-items:center;gap:6px;font-size:11px;color:rgba(52,211,153,0.8);">
              <div class="live-dot"></div>
              Available for opportunities
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PROJECTS PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Projects":
    st.markdown('<div class="card" style="margin-bottom:16px;"><div class="sh-title" style="font-size:20px;"><span>📁</span><span style="font-size:22px;font-weight:700;">All Projects</span></div></div>', unsafe_allow_html=True)
    cols = st.columns(3, gap="small")
    for i, p in enumerate(PROJECTS):
        with cols[i % 3]:
            tags_html = "".join(f'<span style="font-size:9px;color:rgba(230,237,243,0.3);background:rgba(124,58,237,0.08);padding:2px 6px;border-radius:3px;font-family:JetBrains Mono,monospace;margin-right:4px;">{t}</span>' for t in p["tags"])
            st.markdown(f"""
            <div class="proj-card" style="margin-bottom:14px;">
              <div class="proj-img" style="background:linear-gradient(135deg,{p['color']},#0a0a1a);height:110px;display:flex;align-items:center;justify-content:center;">
                <span style="font-size:36px;">{p['icon']}</span>
              </div>
              <div class="proj-body">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;">
                  <div class="proj-name">{p['name']}</div>
                  <span style="font-size:8px;background:rgba(124,58,237,0.12);color:#A78BFA;padding:2px 7px;border-radius:3px;font-family:JetBrains Mono,monospace;">{p['badge']}</span>
                </div>
                <div class="proj-desc">{p['desc']}</div>
                <div style="margin-bottom:8px;">{tags_html}</div>
                <div class="proj-footer">
                  <a class="proj-btn" href="https://github.com/Gowtam3016" target="_blank">⌥ GitHub</a>
                  <a class="proj-btn" href="#">▶ Live Demo</a>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  CERTIFICATIONS PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Certifications":
    st.markdown('<div class="card" style="margin-bottom:16px;"><div class="sh-title" style="font-size:20px;"><span>🏆</span><span style="font-size:22px;font-weight:700;">All Certifications</span></div></div>', unsafe_allow_html=True)
    cols = st.columns(4, gap="small")
    for i, c in enumerate(CERTS):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="cert-card" style="margin-bottom:12px;">
              <div class="cert-logo">{c['icon']}</div>
              <div class="cert-name">{c['name']}</div>
              <div class="cert-org">{c['org']}</div>
              <div class="cert-date">{c['date']}</div>
            </div>
            """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  RESUME PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Resume":
    c1, c2 = st.columns([2, 1], gap="small")
    with c1:
        st.markdown(f"""
        <div class="card">
          <div class="sh-title" style="margin-bottom:14px;"><span>📄</span><span>Resume Preview</span></div>
          <iframe src="{RESUME_SRC}" width="100%" height="600"
            style="border:none;border-radius:8px;background:#fff;">
          </iframe>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        highlights = [
            "Bachelor of Computer Science in AI — B.S. Abdur Rahman Crescent, Chennai (2023–2026)",
            "Internship: Lenovo India — Production QC Associate, Pondicherry",
            "Internship: Pluto Academy — AI/ML Internship",
            "6+ projects: IoT, ML, Full Stack, Data Analysis",
            "8 certifications from IBM, Cisco, MongoDB, Oracle, Udemy",
            "Languages: English · Tamil · French",
        ]
        hl_html = "".join(f'<div style="font-size:11px;color:rgba(230,237,243,0.55);padding:7px 0;border-bottom:0.5px solid rgba(255,255,255,0.04);display:flex;gap:8px;"><span style="color:#34D399;">✓</span>{h}</div>' for h in highlights)
        st.markdown(f"""
        <div class="card">
          <div class="sh-title" style="margin-bottom:14px;"><span>⚡</span><span>Quick Highlights</span></div>
          {hl_html}
          <div style="margin-top:16px;">
            <a class="resume-dl" href="{RESUME_SRC}" download="Gowtam_R_E_Resume_2026.pdf">
              ⬇ Download PDF
            </a>
            <a href="https://www.linkedin.com/in/gowtam-r-e-26a7a2296/" target="_blank"
               style="display:block;text-align:center;background:transparent;color:#E6EDF3;font-size:12px;padding:10px;border-radius:9px;border:0.5px solid rgba(230,237,243,0.12);text-decoration:none;font-family:Inter,sans-serif;">
               View LinkedIn Profile ↗
            </a>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  SKILLS PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Skills":
    st.markdown('<div class="card" style="margin-bottom:16px;"><div class="sh-title" style="font-size:20px;"><span>⚡</span><span style="font-size:22px;font-weight:700;">Skills & Technologies</span></div></div>', unsafe_allow_html=True)
    colors = ["#7C3AED","#A78BFA","#60A5FA","#34D399","#F59E0B","#F87171","#C084FC","#818CF8"]
    for cat, skills in SKILLS_ALL.items():
        if cat == "All":
            continue
        st.markdown(f'<div class="card" style="margin-bottom:14px;"><div class="sh-title" style="margin-bottom:12px;"><span>▸</span><span>{cat}</span></div><div style="display:flex;flex-wrap:wrap;gap:8px;">', unsafe_allow_html=True)
        circles = "".join(circular_chart(v, k, colors[i % len(colors)], 90) for i, (k, v) in enumerate(skills.items()))
        st.markdown(f'{circles}</div></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  EXPERIENCE PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Experience":
    st.markdown('<div class="card" style="margin-bottom:16px;"><div class="sh-title" style="font-size:22px;font-weight:700;">💼 Experience & Timeline</div></div>', unsafe_allow_html=True)
    exps = [
        {"role": "Production & Quality Control Associate", "company": "Lenovo India Pvt. Ltd", "type": "Internship",
         "date": "Jun 2025 · Pondicherry", "color": "#001a3e",
         "bullets": ["Gained hands-on experience in assembling and testing laptops and desktop PCs.",
                     "Collaborated with hardware teams to ensure quality control, system functionality, and performance standards during the production process."]},
        {"role": "AI/ML Intern", "company": "Pluto Academy", "type": "Internship",
         "date": "2024 · Remote", "color": "#0a1a00",
         "bullets": ["Developed a Movie Recommendation System using Machine Learning for personalised content suggestions.",
                     "Built a Heart Disease Prediction System using predictive analytics and classification algorithms.",
                     "Worked on data preprocessing, model training, evaluation, and deployment using Python and ML tools."]},
    ]
    for e in exps:
        bullets_html = "".join(f'<div class="expb">{b}</div>' for b in e["bullets"])
        st.markdown(f"""
        <div class="card" style="margin-bottom:14px;border-left:3px solid #7C3AED;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:4px;">
            <div style="font-size:16px;font-weight:600;">{e['role']}</div>
            <div style="font-size:11px;font-family:JetBrains Mono,monospace;color:rgba(230,237,243,0.35);">{e['date']}</div>
          </div>
          <div style="font-size:12px;color:#A78BFA;font-family:JetBrains Mono,monospace;margin-bottom:12px;">{e['company']} — {e['type']}</div>
          {bullets_html}
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  CONTACT PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Contact":
    c1, c2 = st.columns([1.2, 1], gap="small")
    with c1:
        st.markdown(f"""
        <div class="card">
          <div class="sh-title" style="font-size:22px;font-weight:700;margin-bottom:20px;">✉️ Get In Touch</div>
          <div style="font-size:14px;color:rgba(230,237,243,0.55);margin-bottom:24px;line-height:1.75;">
            Open to full-time roles, internships, and freelance projects in AI, ML, data engineering, and IoT.
          </div>
          <div class="contact-item">
            <div class="contact-icon" style="width:40px;height:40px;font-size:16px;">📧</div>
            <div><div style="font-size:11px;color:rgba(230,237,243,0.35);margin-bottom:2px;">Email</div>
            <a href="mailto:regowtam@gmail.com" style="color:#A78BFA;font-size:13px;">regowtam@gmail.com</a></div>
          </div>
          <div class="contact-item">
            <div class="contact-icon" style="width:40px;height:40px;font-size:16px;">📞</div>
            <div><div style="font-size:11px;color:rgba(230,237,243,0.35);margin-bottom:2px;">Phone</div>
            <span style="font-size:13px;">+91 79041 14369</span></div>
          </div>
          <div class="contact-item">
            <div class="contact-icon" style="width:40px;height:40px;font-size:16px;">💼</div>
            <div><div style="font-size:11px;color:rgba(230,237,243,0.35);margin-bottom:2px;">LinkedIn</div>
            <a href="https://www.linkedin.com/in/gowtam-r-e-26a7a2296/" target="_blank" style="color:#A78BFA;font-size:13px;">linkedin.com/in/gowtam-r-e-26a7a2296</a></div>
          </div>
          <div class="contact-item" style="border:none;">
            <div class="contact-icon" style="width:40px;height:40px;font-size:16px;">⌥</div>
            <div><div style="font-size:11px;color:rgba(230,237,243,0.35);margin-bottom:2px;">GitHub</div>
            <a href="https://github.com/Gowtam3016" target="_blank" style="color:#A78BFA;font-size:13px;">github.com/Gowtam3016</a></div>
          </div>
          <div style="margin-top:16px;display:flex;align-items:center;gap:8px;font-size:12px;color:rgba(52,211,153,0.8);">
            <div class="live-dot"></div>Available for opportunities · Chennai, India
          </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card"><div class="sh-title" style="margin-bottom:16px;"><span>💬</span><span>Send a Message</span></div>""", unsafe_allow_html=True)
        name = st.text_input("Your Name", placeholder="Enter your name")
        email = st.text_input("Your Email", placeholder="your@email.com")
        msg = st.text_area("Message", placeholder="Write your message here...", height=120)
        if st.button("🚀 Send Message", use_container_width=True):
            if name and email and msg:
                st.success(f"Thanks {name}! Message sent. Gowtam will reply to {email} soon.")
            else:
                st.warning("Please fill in all fields.")
        st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  ANALYTICS PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Analytics":
    st.markdown('<div class="card" style="margin-bottom:16px;"><div class="sh-title" style="font-size:22px;font-weight:700;">📊 Analytics & Insights</div></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2, gap="small")
    with c1:
        skill_names = list(SKILLS_ALL["All"].keys())
        skill_vals  = list(SKILLS_ALL["All"].values())
        fig = go.Figure(go.Bar(
            x=skill_vals, y=skill_names, orientation='h',
            marker=dict(
                color=skill_vals,
                colorscale=[[0,"rgba(124,58,237,0.4)"], [1,"rgba(124,58,237,1)"]],
                showscale=False),
            text=[f"{v}%" for v in skill_vals], textposition="outside",
            textfont=dict(color="rgba(230,237,243,0.6)", size=10)))
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(13,13,36,1)",
            height=280, margin=dict(l=10,r=40,t=10,b=10),
            xaxis=dict(range=[0,105], gridcolor="rgba(255,255,255,0.04)",
                       tickfont=dict(color="rgba(230,237,243,0.3)", size=9)),
            yaxis=dict(gridcolor="rgba(255,255,255,0.04)",
                       tickfont=dict(color="rgba(230,237,243,0.6)", size=10)))
        st.markdown('<div class="card"><div class="sh-title" style="margin-bottom:10px;"><span>⚡</span><span>Skill Proficiency</span></div>', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        cats = ["Python/ML", "IoT/Embedded", "Data Analysis", "Web/API", "Databases", "DevOps"]
        vals = [90, 80, 87, 75, 73, 78]
        fig2 = go.Figure(go.Scatterpolar(
            r=vals+[vals[0]], theta=cats+[cats[0]],
            fill="toself", fillcolor="rgba(124,58,237,0.15)",
            line=dict(color="#7C3AED", width=2),
            marker=dict(size=5, color="#A78BFA")))
        fig2.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            polar=dict(bgcolor="rgba(13,13,36,1)",
                       radialaxis=dict(visible=True, range=[0,100],
                           tickfont=dict(color="rgba(230,237,243,0.2)", size=8),
                           gridcolor="rgba(255,255,255,0.05)"),
                       angularaxis=dict(tickfont=dict(color="rgba(230,237,243,0.6)", size=10,
                                                       family="JetBrains Mono"),
                                        gridcolor="rgba(255,255,255,0.05)")),
            margin=dict(l=40,r=40,t=20,b=20), height=280)
        st.markdown('<div class="card"><div class="sh-title" style="margin-bottom:10px;"><span>🎯</span><span>Proficiency Radar</span></div>', unsafe_allow_html=True)
        st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  ABOUT PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "About":
    c1, c2 = st.columns([1, 1.5], gap="small")
    with c1:
        st.markdown(f"""
        <div class="card" style="text-align:center;">
          <div style="display:flex;justify-content:center;margin-bottom:16px;">
            <div class="profile-glow">
              <div class="profile-inner">
                <img class="profile-img" src="{PROFILE_SRC}" alt="Gowtam R E"/>
              </div>
            </div>
          </div>
          <div style="font-size:22px;font-weight:700;margin-bottom:4px;">Gowtam R E</div>
          <div style="font-family:JetBrains Mono,monospace;font-size:12px;color:#A78BFA;margin-bottom:12px;">AI Engineer · Data Engineer · Full Stack Developer</div>
          <div style="display:flex;justify-content:center;flex-wrap:wrap;gap:5px;margin-bottom:14px;">
            <span class="lang-b" style="background:rgba(245,158,11,.08);border-color:rgba(245,158,11,.25);color:#F59E0B;">Tamil</span>
            <span class="lang-b" style="background:rgba(124,58,237,.08);border-color:rgba(124,58,237,.25);color:#A78BFA;">English</span>
            <span class="lang-b" style="background:rgba(59,130,246,.08);border-color:rgba(59,130,246,.25);color:#60A5FA;">Français</span>
          </div>
          <div style="display:flex;justify-content:center;gap:10px;">
            <a class="social-btn" href="https://www.linkedin.com/in/gowtam-r-e-26a7a2296/" target="_blank">in</a>
            <a class="social-btn" href="https://github.com/Gowtam3016" target="_blank">⌥</a>
            <a class="social-btn" href="mailto:regowtam@gmail.com">✉</a>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card">
          <div class="sh-title" style="font-size:18px;font-weight:700;margin-bottom:14px;">Who am I?</div>
          <div style="font-size:13px;color:rgba(230,237,243,0.6);line-height:1.85;margin-bottom:18px;">
            I'm a motivated and detail-oriented AI/ML engineer currently completing my final year of
            Bachelor of Computer Science in Artificial Intelligence at B.S. Abdur Rahman Crescent Institute of Science and Technology
            in Chennai, graduating in 2026.
            <br><br>
            I have intermediate knowledge in Python, Java, HTML5, and CSS3, along with hands-on exposure
            to Machine Learning, IoT systems, and Full Stack Development. I'm passionate about solving
            real-world problems through intelligent systems — from ESP32-powered IoT dashboards to
            FastAPI-backed ML pipelines.
            <br><br>
            I completed internships at Lenovo India (hardware QC) and Pluto Academy (AI/ML development),
            and hold 8 certifications from IBM, Cisco, MongoDB, Oracle, and Udemy.
          </div>
          <div class="stats-bar">
            <div class="stat-box"><div class="stat-num">6+</div><div class="stat-lbl">Projects</div></div>
            <div class="stat-box"><div class="stat-num">3</div><div class="stat-lbl">Languages</div></div>
            <div class="stat-box"><div class="stat-num">8</div><div class="stat-lbl">Certs</div></div>
            <div class="stat-box"><div class="stat-num">2</div><div class="stat-lbl">Internships</div></div>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ── Close main ────────────────────────────────────────────────────────────────
st.markdown('</div>', unsafe_allow_html=True)
