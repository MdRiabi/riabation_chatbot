import streamlit as st
import streamlit.components.v1 as components
from models import user_model
import os
import base64


import streamlit as st
import os
import base64

def render_video(video_filename: str, opacity: float = 0.55):
    # 1. Obtenir le chemin absolu du fichier actuel
    current_file_path = os.path.abspath(__file__)
    
    # 2. Remonter à la racine du projet (2 niveaux au-dessus)
    project_root = os.path.dirname(os.path.dirname(current_file_path))
    
    # 3. Construire le chemin complet vers la vidéo
    video_path = os.path.join(project_root, ".streamlit", "static", video_filename)
    
    # 4. Normaliser le chemin pour corriger les barres obliques
    video_path = os.path.normpath(video_path)
    
    # 5. Vérifier si le fichier existe
    if not os.path.isfile(video_path):
        st.error(f"ERREUR: Fichier vidéo introuvable\nChemin recherché: {video_path}")
        st.error(f"Veuillez vérifier que le fichier {video_filename} existe dans le dossier .streamlit/static")
        return

    # 6. Lire et encoder la vidéo en base64
    try:
        with open(video_path, "rb") as video_file:
            video_bytes = video_file.read()
        video_base64 = base64.b64encode(video_bytes).decode("utf-8")
    except Exception as e:
        st.error(f"Erreur lors de la lecture de la vidéo: {str(e)}")
        return

    # 7. Injecter le HTML/CSS pour l'arrière-plan vidéo
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: transparent;
        }}
        #bgvid-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            overflow: hidden;
        }}
        #bgvid {{
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            object-fit: cover;
            opacity: {opacity};
        }}
        .main .block-container {{
            background-color: rgba(0, 0, 0, 0.6);
            border-radius: 10px;
            padding: 2rem;
            z-index: 1;
            position: relative;
        }}
        </style>
        
        <div id="bgvid-container">
            <video autoplay muted loop id="bgvid">
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
        </div>
        """,
        unsafe_allow_html=True
    )
def login():
    
    #from views.background_video_component import render_background_video
    # Remplace 'static/ma_video.mp4' par le chemin réel de ta vidéo
    render_video('ai.mp4', opacity=0.55)
    print(os.path.abspath("ai.mp4"))
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
