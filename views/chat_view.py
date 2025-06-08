import streamlit as st
from datetime import datetime
from services import groq_service
from services import file_service
from models import message_model

def handle_user_input():
    user_input = st.session_state.user_input.strip()
    if user_input:
        response = groq_service.ask_groq(user_input)
        timestamp = datetime.now().isoformat()
        message_model.save_message(st.session_state.username, "user", user_input, timestamp)
        message_model.save_message(st.session_state.username, "assistant", response, timestamp)

        # vider après traitement (via reinitialisation automatique dans callback)
        st.session_state.user_input = ""  # autorisé ici car exécuté avant rendu du widget

def chat_interface():
    st.title("💬 Chatbot Riabation")
    st.markdown(f"👤 Connecté en tant que **{st.session_state.username}**")

    # ✅ Text input avec on_change
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
                st.markdown(f"""<div style="background-color:#e0f7fa; padding:10px; border-radius:10px; margin:5px 0">
                    <strong>🧑‍💼 Vous :</strong><br>{content}</div>""", unsafe_allow_html=True)
            elif role == "assistant":
                st.markdown(f"""<div style="background-color:#f1f8e9; padding:10px; border-radius:10px; margin:5px 0">
                    <strong>🤖 IA :</strong><br>{content}</div>""", unsafe_allow_html=True)

    # ... (reste du code : analyse fichier, déconnexion, etc.)


    # ─────────────────────────────
    # 📁 Analyse de fichier (si connecté)
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

        if st.button("🔍 Extraire les points clés"):
            prompt = f"Voici un texte :\n\n{extracted_text[:5000]}\n\nDonne les points clés sous forme de liste claire."
            key_points = groq_service.ask_groq(prompt)
            st.success("🔑 Points clés :")
            st.markdown(key_points)

    # 🔚 Bouton de déconnexion
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Se déconnecter"):
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.experimental_rerun()
