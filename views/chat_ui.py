import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

class ChatUI:
    def __init__(self):
        self.set_style()

    def set_style(self):
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to right, #141e30, #243b55);
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }

        .chat-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin: 10px 0;
        }

        .user-bubble, .ai-bubble {
            max-width: 80%;
            padding: 10px 15px;
            border-radius: 15px;
            animation: fadeIn 0.4s ease;
            line-height: 1.4;
        }

        .user-bubble {
            background-color: #1e88e5;
            align-self: flex-end;
            color: white;
        }

        .ai-bubble {
            background-color: #4caf50;
            align-self: flex-start;
            color: white;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .avatar {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            margin-right: 10px;
        }

        .message-row {
            display: flex;
            align-items: flex-start;
        }
        </style>
        """, unsafe_allow_html=True)

    def show_user_message(self, message):
        st.markdown(f"""
        <div class="chat-container">
            <div class="message-row" style="justify-content: flex-end;">
                <div class="user-bubble">{message}</div>
                <img class="avatar" src="https://avatars.githubusercontent.com/u/1?v=4">
            </div>
        </div>
        """, unsafe_allow_html=True)

    def show_ai_typing(self):
        lottie_url = "https://lottie.host/60a4a984-89df-4df6-9e54-82c424f62659/GIM9QHKw3u.json"
        st_lottie(self.load_lottie_url(lottie_url), height=120, key="typing")

    def show_ai_message_typing(self, full_message, speed=0.01):
        placeholder = st.empty()
        displayed = ""
        for char in full_message:
            displayed += char
            html = f"""
            <div class="chat-container">
                <div class="message-row">
                    <img class="avatar" src="https://cdn-icons-png.flaticon.com/512/4712/4712037.png">
                    <div class="ai-bubble">{displayed}</div>
                </div>
            </div>
            """
            placeholder.markdown(html, unsafe_allow_html=True)
            time.sleep(speed)

    def load_lottie_url(self, url: str):
        try:
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        except Exception:
            return None
