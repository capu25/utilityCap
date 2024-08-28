import streamlit as st
from PyPDF2 import PdfReader
import io

st.title("📄 PDF Scraper")
st.write("Carica il tuo file in formato 'PDF' e ricerca al suo interno il dato che ti serve!")
st.write("---")

uploaded_file = st.file_uploader("Seleziona un file PDF", type=["pdf"])

search_term = st.text_input("Inserisci la parola o frase da cercare")

if uploaded_file is not None and search_term:
    # Leggi il contenuto del PDF
    pdf_reader = PdfReader(uploaded_file)
    full_text = ""

    for page in pdf_reader.pages:
        full_text += page.extract_text()

    # Cerca la parola/frase
    search_results = []
    for i, page in enumerate(pdf_reader.pages):
        text = page.extract_text()
        if search_term.lower() in text.lower():
            search_results.append(f"Pagina {i + 1}: {text.lower().count(search_term.lower())} occorrenze")

    if search_results:
        st.write(f"Risultati della ricerca per '{search_term}':")
        for result in search_results:
            st.write(result)
    else:
        st.write(f"Nessuna occorrenza trovata per '{search_term}'.")

    with st.expander("Mostra il testo completo del PDF"):
        st.text_area("Testo del PDF", full_text, height=300)
else:
    st.write("Carica un file PDF per iniziare.")
