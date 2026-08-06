import streamlit as st


class AuthManager:

    @staticmethod
    def save_token(token: str):

        st.session_state.access_token = token

    @staticmethod
    def get_token():

        return st.session_state.get(
            "access_token"
        )

    @staticmethod
    def is_logged_in():
        return bool(AuthManager.get_token())

    @staticmethod
    def logout():
        st.session_state.clear()

    @staticmethod
    def get_current_user():

        return st.session_state.get(
            "current_user"
        )


    @staticmethod
    def get_role():

        user = AuthManager.get_current_user()

        if not user:
            return None

        return user.get("role")