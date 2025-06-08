import streamlit as st
from services import groq_service
from models import message_model
from datetime import datetime

def chat_interface():
    st.title("💬 Chatbot Riabation")
    st.markdown(f"👤 Connecté en tant que **{st.session_state.username}**")

    # Entrée utilisateur
    user_input = st.text_input("Posez votre question :", key="user_input")
    if st.button("Envoyer") and user_input.strip():
        # Appel Groq
        response = groq_service.ask_groq(user_input)

        # Sauvegarde avec horodatage (timestamp = session)
        timestamp = datetime.now().isoformat()
        message_model.save_message(st.session_state.username, "user", user_input, timestamp)
        message_model.save_message(st.session_state.username, "assistant", response, timestamp)

        st.success("✅ Réponse générée !")
        st.text_input("Posez votre question :", value="", key="user_input", disabled=True)

    # Affichage historique groupé
    st.subheader("📜 Historique de vos échanges")
    messages = message_model.get_messages_grouped(st.session_state.username)

    last_session = None
    for timestamp, msgs in messages.items():
        # Séparateur de session
        st.markdown(f"<hr><p style='color:gray'><b>📅 Session :</b> {timestamp}</p>", unsafe_allow_html=True)

        for role, content in msgs:
            if role == "user":
                st.markdown(
                    f"""
                    <div style="background-color:#e0f7fa; padding:10px; border-radius:10px; margin:5px 0">
                        <strong>🧑‍💼 Vous :</strong><br>{content}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif role == "assistant":
                st.markdown(
                    f"""
                    <div style="background-color:#f1f8e9; padding:10px; border-radius:10px; margin:5px 0">
                        <strong>🤖 IA :</strong><br>{content}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


