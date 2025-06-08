import streamlit as st
from controllers import auth_controller, chat_controller
from db.schema import init_db

def main():
    init_db()

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        print("🔐 Initialisation de l'état de session (non authentifié)")

    if st.session_state.authenticated:
        print(f"✅ Utilisateur connecté : {st.session_state.username}")
        st.write(f"🔁 Bascule vers la page de chat pour : {st.session_state.username}")
        chat_controller.chat_flow()
    else:
        print("🔐 Affichage du contrôleur d'authentification")
        st.write("🟡 Attente de connexion...")
        auth_controller.auth_flow()

if __name__ == "__main__":
    main()
