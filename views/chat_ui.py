import streamlit as st
import streamlit.components.v1 as components
import pyttsx3

# ⏺️ Initialisation moteur vocal
engine = pyttsx3.init()

# ─────────────────────────────
# 🎨 Thème clair / sombre
def render_theme_selector():
    """Render theme selector and apply the chosen theme."""
    # Définir une valeur par défaut si elle n'existe pas
    if "theme_choice" not in st.session_state:
        st.session_state.theme_choice = "Clair"  # Default theme

    # Utiliser directement le widget pour gérer l'état
    theme = st.sidebar.radio("🌗 Choisissez le thème :", ["Clair", "Sombre"], index=0 if st.session_state.theme_choice == "Clair" else 1)

    # Appliquer le thème en fonction de la sélection
    if theme == "Clair":
        inject_css(light=True)
    else:
        inject_css(light=False)

    # Mettre à jour la session state uniquement si nécessaire
    st.session_state.theme_choice = theme


def inject_css(light=True):
    if light:
        st.markdown("""
            <style>
                html, body, [class*="css"] {
                    background-color: #ffffff !important;
                    color: #000000 !important;
                }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                html, body, [class*="css"] {
                    background-color: #111111 !important;
                    color: #eeeeee !important;
                }
            </style>
        """, unsafe_allow_html=True)

# ─────────────────────────────
# 🔊 Synthèse vocale activable
def render_voice_toggle():
    """Toggle synthèse vocale."""
    if "voice_enabled" not in st.session_state:
        st.session_state.voice_enabled = False
    enabled = st.sidebar.checkbox("🔊 Synthèse vocale activée", value=st.session_state.voice_enabled)
    st.session_state.voice_enabled = enabled

    # Arrêter la synthèse vocale si désactivée
    if not enabled:
        engine.stop()
        
def speak(text):
    if st.session_state.get("voice_enabled", False):
        try:
            engine.stop()  # Arrête toute lecture précédente
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            st.warning(f"Erreur synthèse vocale : {e}")

# ─────────────────────────────
# 🌌 Animation IA
def render_header_animation():
    animation_html = """
    <div style="text-align:center; margin-top:10px; margin-bottom:10px;">
        <img src="https://media.tenor.com/7Zyuxz9FEh0AAAAC/ai-artificial-intelligence.gif" width="300"/>
    </div>
    """
    st.markdown(animation_html, unsafe_allow_html=True)

# ─────────────────────────────
# 🌟 Bannière futuriste
def render_ai_neon_banner():
    neon_html = """
    <h2 style='text-align: center; font-family: "Courier New", monospace;
        color: #00f7ff; text-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 20px #0ff;'>
        🤖 Intelligence Artificielle - Chatbot Riabation
    </h2>
    """
    st.markdown(neon_html, unsafe_allow_html=True)

# ─────────────────────────────
# 💬 Affichage des messages
def render_user_message(message):
    st.markdown(f"""
        <div style="background-color:#007acc; padding:12px; border-radius:12px; margin:8px 0; color:white">
            <strong>🧑‍💼 Vous :</strong><br>{message}
        </div>
    """, unsafe_allow_html=True)

def render_assistant_message(message):
    st.markdown(f"""
        <div style="background-color:#0f0f0f; padding:12px; border-radius:12px; margin:8px 0; color:#00f7ff;
                    font-family: 'Segoe UI', sans-serif;">
            <strong>🤖 IA :</strong><br>{message}
        </div>
    """, unsafe_allow_html=True)
