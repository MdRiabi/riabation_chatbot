import streamlit as st
from services import groq_service, file_service
from models import message_model

def chat_interface():
    st.title("Chatbot Riabation")
    user_input = st.text_input("Posez votre question :")
    if st.button("Envoyer"):
        response = groq_service.ask_groq(user_input)
        st.write(f"Réponse : {response}")
        # Sauvegarder les messages
        message_model.save_message(st.session_state.username, "user", user_input)
        message_model.save_message(st.session_state.username, "bot", response)

    st.subheader("Historique des conversations")
    messages = message_model.get_messages(st.session_state.username)
    for role, content in messages:
        st.write(f"{role}: {content}")

    st.subheader("Analyse de fichiers")
    uploaded_file = st.file_uploader("Téléchargez un fichier", type=["pdf", "txt"])
    if uploaded_file:
        text = file_service.extract_text(uploaded_file)
        st.text_area("Contenu extrait", text)
        if st.button("Résumer"):
            summary = groq_service.summarize_text(text)
            st.write(f"Résumé : {summary}")
