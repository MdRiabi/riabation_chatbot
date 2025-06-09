import streamlit as st
from datetime import datetime
from services import groq_service, file_service
from models import message_model
from views import chat_ui  # 📦 Module UI/UX personnalisé
import time

def handle_user_input():
    user_input = st.session_state.user_input.strip()
    if user_input:
        with st.spinner("🤖 L'IA réfléchit..."):
            time.sleep(0.6)  # ⏳ Petite pause visuelle
            response = groq_service.ask_groq(user_input)

        timestamp = datetime.now().isoformat()
        message_model.save_message(st.session_state.username, "user", user_input, timestamp)
        message_model.save_message(st.session_state.username, "assistant", response, timestamp)

        chat_ui.speak(response)  # 🔊 Synthèse vocale

        st.session_state.user_input = ""  # Réinitialise le champ

def chat_interface(): 
    chat_ui.render_voice_toggle()

    # 🎨 Choix du thème
    chat_ui.render_theme_selector()

    # 🌌 Animation futuriste
    chat_ui.render_header_animation()
    chat_ui.render_ai_neon_banner()

    # 🔰 En-tête
    st.title("💬 Chatbot Riabation")
    st.markdown(f"👤 Connecté en tant que **{st.session_state.username}**")

    # 📝 Champ de saisie
    st.text_input(
        "Posez votre question :",
        key="user_input",
        on_change=handle_user_input,
        placeholder="Entrez votre message ici et appuyez sur Entrée"
    )

    # 🔁 Historique
    st.subheader("📜 Historique de vos échanges")
    messages = message_model.get_messages_grouped(st.session_state.username)

    for timestamp, msgs in messages.items():
        st.markdown(f"<hr><p style='color:gray'><b>📅 Session :</b> {timestamp}</p>", unsafe_allow_html=True)
        for role, content in msgs:
            if role == "user":
                chat_ui.render_user_message(content)
            elif role == "assistant":
                chat_ui.render_assistant_message(content)

    # ─────────────────────────────
    # 📁 Analyse de fichier
    st.markdown("---")
    st.subheader("📁 Analyse de fichier")

    uploaded_file = st.file_uploader("Téléchargez un fichier (.pdf, .txt, .chat)", type=["pdf", "txt", "chat"])
    extracted_text = ""

    if uploaded_file:
        extracted_text = file_service.extract_text(uploaded_file)

        st.markdown("### 📝 Contenu extrait (aperçu)")
        st.text_area("Texte extrait :", extracted_text[:2000], height=200)

        if st.button("📌 Générer un résumé"):
            prompt = f"Voici un texte extrait :\n\n{extracted_text[:5000]}\n\nFais un résumé clair, concis et structuré."
            summary = groq_service.ask_groq(prompt)
            st.success("📋 Résumé :")
            st.write(summary)
            chat_ui.speak(summary)

        if st.button("🔍 Extraire les points clés"):
            prompt = f"Voici un texte :\n\n{extracted_text[:5000]}\n\nDonne les points clés sous forme de liste claire."
            key_points = groq_service.ask_groq(prompt)
            st.success("🔑 Points clés :")
            st.markdown(key_points)
            chat_ui.speak(key_points)

    # 🔚 Déconnexion
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Se déconnecter"):
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.experimental_rerun()
