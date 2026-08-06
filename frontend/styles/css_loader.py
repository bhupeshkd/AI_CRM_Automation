from pathlib import Path
import streamlit as st

def load_css():
    """
    Injects dynamic CSS based on the active theme in session state.
    """
    # Initialize theme state if missing
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"

    is_dark = st.session_state.theme == "dark"

    # Define color palettes directly in Python
    colors = {
        "bg_main": "#0B0F19" if is_dark else "#F8FAFC",
        "bg_card": "rgba(30, 41, 59, 0.6)" if is_dark else "#FFFFFF",
        "bg_sidebar": "#0F172A" if is_dark else "#F1F5F9",
        "text_primary": "#F8FAFC" if is_dark else "#0F172A",
        "text_secondary": "#94A3B8" if is_dark else "#64748B",
        "border_color": "rgba(255, 255, 255, 0.08)" if is_dark else "rgba(0, 0, 0, 0.1)",
        "hover_bg": "rgba(255, 255, 255, 0.06)" if is_dark else "rgba(0, 0, 0, 0.05)",
    }

    # Inject dynamic CSS variables directly into stApp
    st.markdown(
        f"""
        <style>
            :root {{
                --bg-main: {colors['bg_main']};
                --bg-card: {colors['bg_card']};
                --bg-sidebar: {colors['bg_sidebar']};
                --text-primary: {colors['text_primary']};
                --text-secondary: {colors['text_secondary']};
                --border-color: {colors['border_color']};
                --hover-bg: {colors['hover_bg']};
            }}

            .stApp {{
                background-color: var(--bg-main) !important;
                color: var(--text-primary) !important;
            }}

            [data-testid="stSidebar"] {{
                background-color: var(--bg-sidebar) !important;
                border-right: 1px solid var(--border-color) !important;
            }}

            /* Headers and Text */
            h1, h2, h3, h4, h5, h6, p, label, span {{
                color: var(--text-primary) !important;
            }}

            /* Sidebar Nav links */
            [data-testid="stSidebarNav"] a {{
                color: var(--text-secondary) !important;
            }}

            [data-testid="stSidebarNav"] a:hover {{
                background-color: var(--hover-bg) !important;
                color: var(--text-primary) !important;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Load custom static overrides if custom.css exists
    css_path = Path(__file__).resolve().parent / "custom.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def render_theme_toggle():
    """
    Renders the toggle button in the sidebar.
    """
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"

    is_dark = st.session_state.theme == "dark"
    btn_label = "☀️ Light Mode" if is_dark else "🌙 Dark Mode"

    if st.button(btn_label, use_container_width=True, key="global_theme_toggle"):
        st.session_state.theme = "light" if is_dark else "dark"
        st.rerun()