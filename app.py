import streamlit as st
from controllers import auth_controller, chat_controller
from db.schema import init_db

def main():
    init_db()
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        auth_controller.auth_flow()
    else:
        chat_controller.chat_flow()

if __name__ == "__main__":
    main()
