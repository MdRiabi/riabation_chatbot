import streamlit as st
from models import user_model

def login():
    st.title("Se connecter")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Connexion"):
        if user_model.authenticate_user(username, password):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("Connexion réussie")
            #st.experimental_rerun()  # ← force le rechargement pour afficher le chat
            st.stop()
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect")
