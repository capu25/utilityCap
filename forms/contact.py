import re
import requests
import streamlit as st

WEBHOOK_URL = ""

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Nome")
        email = st.text_input("E-mail")
        message = st.text_area("Il tuo messaggio:")
        submit_button = st.form_submit_button("Invia")

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Il servizio mail è momentaneamente disabilitato, riprova più tardi", icon="📧")
                st.stop()
            if not name:
                st.error("Inserisci il tuo nome.", icon="🧑")
                st.stop()
            if not email:
                st.error("Inserisci un indirizzo mail.", icon="📨")
                st.stop()
            if not is_valid_email(email):
                st.error("Inserisci un indirizzo mail valido.", icon="📨")
                st.stop()
            if not message:
                st.error("Inserisci il tuo messaggio.", icon="💬")
                st.stop()

            # --- Payload ---
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Il tuo messaggio è stato inviato con successo! 🎉", icon="🚀")
                st.balloons()
            else:
                st.error("C'è stato un errore nell'invio del messaggio.", icon="😨")