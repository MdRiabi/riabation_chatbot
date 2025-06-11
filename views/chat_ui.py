import streamlit as st
import streamlit.components.v1 as components
import pyttsx3
from gtts import gTTS  # Google Text-to-Speech (cloud)
import base64

# Solution de repli si gTTS ne s'installe pas
try:
    from gtts import gTTS
    TTS_ENABLED = True
except ImportError:
    TTS_ENABLED = False

# Initialisation moteur vocal
engine = pyttsx3.init()

# ───────────── Thème dynamique sans config.toml ─────────────

def render_theme_selector():
    """Render theme selector and apply the chosen theme."""
    # Initialisation de l'état du thème
    if "theme_choice" not in st.session_state:
        st.session_state.theme_choice = "Clair"

    # Sélecteur de thème
    theme = st.sidebar.radio(
        "🌗 Choisissez le thème :",
        ["Clair", "Sombre"],
        index=0 if st.session_state.theme_choice == "Clair" else 1,
    )

    # Appliquer le thème en fonction de la sélection
    if theme != st.session_state.theme_choice:
        st.session_state.theme_choice = theme
        apply_global_theme(theme)

def apply_global_theme(theme):
    """Inject CSS styles globally based on the theme."""
    if theme == "Clair":
        css = """
        <style>
            html, body, [class*="css"] {
                background-color: #ffffff !important;
                color: #000000 !important;
            }
            .stSidebar {
                background-color: #f0f0f0 !important;
            }
            .stApp {
                background-color: #ffffff !important;
                color: #000000 !important;
            }
            .chat-message {
                background-color: #f0f2f6 !important;
                color: #000000 !important;
            }
        </style>
        """
    else:
        css = """
        <style>
            html, body, [class*="css"] {
                background-color: #111111 !important;
                color: #eeeeee !important;
            }
            .stSidebar {
                background-color: #333333 !important;
            }
            .stApp {
                background-color: #111111 !important;
                color: #eeeeee !important;
            }
            .chat-message {
                background-color: #222222 !important;
                color: #eeeeee !important;
            }
        </style>
        """
    st.markdown(css, unsafe_allow_html=True)        

def apply_dynamic_theme(theme):
    """Inject CSS styles based on the theme."""
    if theme == "Clair":
        css = """
        <style>
            html, body, [class*="css"] {
                background-color: #ffffff !important;
                color: #000000 !important;
            }
            .stSidebar {
                background-color: #f0f0f0 !important;
            }
            .chat-message {
                background-color: #f0f2f6 !important;
                color: #000000 !important;
            }
        </style>
        """
    else:
        css = """
        <style>
            html, body, [class*="css"] {
                background-color: #111111 !important;
                color: #eeeeee !important;
            }
            .stSidebar {
                background-color: #333333 !important;
            }
            .chat-message {
                background-color: #222222 !important;
                color: #eeeeee !important;
            }
        </style>
        """
    st.markdown(css, unsafe_allow_html=True)

# ───────────── Synthèse vocale ─────────────
def render_voice_toggle():
    if "voice_enabled" not in st.session_state:
        st.session_state.voice_enabled = False

    enabled = st.sidebar.checkbox("🔊 Synthèse vocale activée", value=st.session_state.voice_enabled)
    st.session_state.voice_enabled = enabled
    if not enabled:
        engine.stop()

#def speak(text):


def speak(text, lang='fr-FR'):
    """Utilise la synthèse vocale du navigateur pour lire le texte"""
    # Échapper les caractères spéciaux pour JavaScript
    safe_text = text.replace('"', '\\"').replace('\n', ' ')
    
    js_code = f"""
    <script>
    function speak() {{
        if ('speechSynthesis' in window) {{
            const utterance = new SpeechSynthesisUtterance("{safe_text}");
            utterance.lang = '{lang}';
            utterance.rate = 1.0;
            window.speechSynthesis.speak(utterance);
        }} else {{
            console.warn("Votre navigateur ne supporte pas la synthèse vocale");
        }}
    }}
    
    // Lancer quand la page est prête
    if (document.readyState === 'complete') {{
        speak();
    }} else {{
        window.addEventListener('load', speak);
    }}
    </script>
    """
    components.html(js_code, height=0, width=0)
    
    # Optionnel: Afficher une icône audio
    st.markdown(f'<div style="margin-top:-30px;margin-bottom:10px">🔊 Lecture audio...</div>', unsafe_allow_html=True)

# ───────────── IA UI ─────────────
def render_header_animation():
    animation_html = """
    <div style="text-align:center; margin-top:10px; margin-bottom:10px;">
        <img src="https://media.tenor.com/7Zyuxz9FEh0AAAAC/ai-artificial-intelligence.gif" width="300"/>
    </div>
    """
    st.markdown(animation_html, unsafe_allow_html=True)

def render_ai_neon_banner():
    neon_html = """
    <h2 style='text-align: center; font-family: "Courier New", monospace;
        color: #00f7ff; text-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 20px #0ff;'>
        🤖 Intelligence Artificielle - Chatbot Riabation
    </h2>
    """
    st.markdown(neon_html, unsafe_allow_html=True)

# ───────────── Affichage des messages ─────────────
def render_user_message(message):
    st.markdown(f"""
        <div class="chat-message" style="background-color:#007acc; padding:12px; border-radius:12px; margin:8px 0; color:white">
            <strong>🧑‍💼 Vous :</strong><br>{message}
        </div>
    """, unsafe_allow_html=True)

def render_assistant_message(message):
    st.markdown(f"""
        <div class="chat-message" style="background-color:#0f0f0f; padding:12px; border-radius:12px; margin:8px 0; color:#00f7ff;
                    font-family: 'Segoe UI', sans-serif;">
            <strong>🤖 IA :</strong><br>{message}
        </div>
    """, unsafe_allow_html=True)
