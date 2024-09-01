from pathlib import Path

import streamlit as st

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "mainStyle.css"

# --- Load CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- Page Setup ---
aboutPage = st.Page(
    page="views/aboutMe.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True, #first page we see
)
project_1_page = st.Page(
    page="views/dashboard.py",
    title="CSV Analyzer",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    page="views/chatBot.py",
    title="Echo - Dumb chatBot",
    icon=":material/smart_toy:",
)
project_3_page = st.Page(
page="views/imageEditor.py",
    title="Image Editor",
    icon=":material/image:",
)
project_4_page = st.Page(
page="views/pdfScraper.py",
    title="PDFs Scraper",
    icon=":material/description:",
)

# --- Navigation Setup ---
#pg = st.navigation(pages=[aboutPage, project_1_page, project_2_page])

# --- Navigation Setup [WITH SECTIONS] ---
pg = st.navigation(
    {
        "": [aboutPage],
        "Tool utili:": [],
        "Data manipulation": [project_1_page, project_4_page],
        "Utility": [project_3_page],
        "Dummy": [project_2_page]
    }
)

# --- Shared on all pages ---
st.logo("assets/newLogo.png")
st.sidebar.text("Made with ❤️!")

# --- Run Nav ---
pg.run()