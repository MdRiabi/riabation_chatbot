from views import login_view, register_view
from models import user_model
import streamlit as st

def auth_flow():
    choice = st.sidebar.selectbox("Menu", ["Se connecter", "Créer un compte"])
    if choice == "Se connecter":
        login_view.login()
    else:
        register_view.register()
