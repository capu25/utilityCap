import streamlit as st
from pathlib import Path
from forms.contact import contact_form

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "docs" / "curriculumCapDef.pdf"
EMAIL = "antonio.pio25a@gmail.com"

# --- Load CSS & CV file ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

SOCIAL_MEDIA = {
    "GitHub": "https://github.com/capu25",
    "LinkedIn": "https://it.linkedin.com",
    "Twitter": "https://x.com/_tonino25_",
}

@st.dialog("Contattami da qui!")
def show_contact_form():
    contact_form()

# --- Hero Session ---
col1, col2 = st.columns(2, gap="small") #vertical_alignment="center"
with col1:
    st.image("assets/fixed.png", width=280)
with col2:
    st.title("Antonio Pio Caputo", anchor=False)
    st.write(
        "Neolaureato in Informatica e T.P.S.  🎓 💻  presso l'università degli Studi di Bari Aldo Moro."
    )
    button_col1, button_col2 = st.columns([1, 1], gap="small")
    with button_col1:
        if st.button("Contattami!"):
            show_contact_form()
    with button_col2:
        if st.download_button(
            label="Download CV",
            data=PDFbyte,
            file_name="CurriculumVitae",
            mime="application/octotet-stream",
        ):
            st.balloons()

#st.write("📬", EMAIL)
st.markdown(f"""
    <div style="margin-left: 30px; margin-bottom:10px;">
        📬 <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
    """, unsafe_allow_html=True)


st.write("---")

# --- Social Links ---
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Experience & Qualifications ---
st.subheader("Esperienze & Qualifiche", anchor=False)
st.write(
    """
    - ✅ Accademical developing 3+ years
    - ✅ Capacità di risoluzione problemi in autonomia
    - ✅ Ottima predisposizione al lavoro di gruppo
    - ✅ Ottima capacità analitica dei vari tasks assegnati
    """
)

# --- Skills ---
st.write("---")
st.subheader("Skills", anchor=False)
st.write(
    """
    - 👨‍💻 Linguaggi di programmazione: Python, Java, Js, C
    - 📊 Framework: React-Native, Streamlit, Yii-Framework
    - 📚 Databases: MySql, PostGres, FireBase
    - 📱 Sviluppo Mobile: Android nativo e cross platform
    """
)

# --- Projects ---
st.write("---")
st.subheader("Alcuni dei miei progetti", anchor=False)
st.markdown(
    """
    - 📚 [**Traduttore LIS (ML & AI)**](https://github.com/capu25/SistemiAdAgenti.git)
    - 📊 [**STL-Dashboard | medHelp (Data Analisys)**](https://github.com/capu25/medHelp.git)
    - 🧠 [**Quotes: meditation app (Mobile)**](https://github.com/capu25/Quotes.git)
    - ✏️ [**devFolio (HTML, CSS, JS)**](https://github.com/capu25/devFolio.git)
    """
)



st.write("---")
st.image("assets/experience.jpg", use_column_width=True)