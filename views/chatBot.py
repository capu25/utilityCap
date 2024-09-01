import streamlit as st
import openai

st.title("💬 EchoBot")
st.write("Deprecati metodi API da parte di openAI >> il bot ripete a pappagallo! 🦜")
st.write("---")
#openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display chat messages from history on app rerun ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- React to user input ---
if prompt := st.chat_input("What is up?"):
    #show user messages
    with st.chat_message("user"):
        st.markdown(prompt)
    #add messages to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"

    with st.chat_message("assistant"):
       st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})