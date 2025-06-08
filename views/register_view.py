import streamlit as st
from models import user_model

def register():
    st.title("Créer un compte")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("S'inscrire"):
        user_model.create_user(username, password)
        st.success("Compte créé avec succès")
