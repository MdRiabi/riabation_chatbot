import streamlit as st

def render_background_video(video_url: str, opacity: float = 0.55):
    """
    Affiche une vidéo en arrière-plan sur Streamlit à l'aide de HTML/CSS.
    :param video_url: URL ou chemin relatif/absolu vers la vidéo MP4
    :param opacity: Opacité de la vidéo (0 à 1)
    """
    st.markdown(f"""
        <style>
        .stApp {{
            position: relative;
            min-height: 100vh;
            overflow: hidden;
        }}
        #bgvid {{
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100vw;
            min-height: 100vh;
            width: auto;
            height: auto;
            z-index: -1;
            opacity: {opacity};
            object-fit: cover;
        }}
        </style>
        <video autoplay muted loop id="bgvid">
            <source src="{video_url}" type="video/mp4">
        </video>
    """, unsafe_allow_html=True)
