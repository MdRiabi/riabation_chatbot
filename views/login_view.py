import streamlit as st
import streamlit.components.v1 as components
from models import user_model
from views.background_video_component import render_background_video

def render_background_video(video_url: str, opacity: float = 0.55):
    """Afficher une vidéo en arrière-plan avec HTML/CSS."""
    components.html(f"""
        <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; overflow: hidden;">
            <video autoplay muted loop style="width: 100%; height: 100%; object-fit: cover; opacity: {opacity};">
                <source src="{video_url}" type="video/mp4">
            </video>
        </div>
    """, height=0)

def login():
    
    #from views.background_video_component import render_background_video
    # Remplace 'static/ma_video.mp4' par le chemin réel de ta vidéo
    render_background_video('../assets/ai.mp4', opacity=0.55)
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
