import streamlit as st
from models import user_model

def register():
    from views.background_video_component import render_background_video
    # Remplace 'static/ma_video.mp4' par le chemin réel de ta vidéo
    render_background_video('assets/ai.mp4', opacity=0.55)
    st.title("Créer un compte")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("S'inscrire"):
        if not username or not password:
             st.warning("Veuillez remplir tous les champs")
             return
        try:

              user_model.create_user(username, password)
              st.success("Compte créé avec succès")

        except Exception as e:
             st.error(f"❌ Erreur : {str(e)}")
