import sys
from pathlib import Path
import streamlit as st

# Ensure root directory (frontend/) is in Python path for sub-folder imports
root_dir = Path(__file__).resolve().parent
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

from utils.api import APIClient
from utils.auth import AuthManager
from styles.css_loader import load_css

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI CRM Pro | Authentication",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_css()

# Modern Compact CSS Injection
st.markdown("""
<style>
    /* Hide top header bar */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Restrict max width of main container */
    .block-container {
        padding-top: 4rem !important;
        padding-bottom: 2rem !important;
    }

    /* Form Container Max Width Fix */
    div[data-testid="stForm"] {
        max-width: 420px !important;
        margin: 0 auto !important;
        background: #161b22 !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 16px !important;
        padding: 2rem 1.8rem !important;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.6) !important;
    }

    /* Header styling */
    .login-brand-header {
        text-align: center;
        max-width: 420px;
        margin: 0 auto 1.5rem auto;
    }
    
    .login-badge {
        display: inline-block;
        background: rgba(99, 102, 241, 0.12);
        border: 1px solid rgba(99, 102, 241, 0.25);
        color: #818CF8;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 600;
        margin-bottom: 12px;
    }
    
    .login-title {
        font-size: 2.1rem;
        font-weight: 800;
        color: #F8FAFC;
        letter-spacing: -0.02em;
        margin-bottom: 6px;
    }
    
    .login-subtitle {
        color: #94A3B8;
        font-size: 0.88rem;
    }

    /* Form Input Fields */
    div[data-testid="stForm"] input {
        background-color: #0d1117 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: #F8FAFC !important;
        border-radius: 8px !important;
    }

    /* Submit Button styling */
    div[data-testid="stForm"] button {
        background: #6366F1 !important;
        color: #FFFFFF !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 0.6rem 1rem !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3) !important;
        transition: all 0.2s ease !important;
    }
    
    div[data-testid="stForm"] button:hover {
        background: #4F46E5 !important;
        box-shadow: 0 6px 16px rgba(99, 102, 241, 0.45) !important;
    }

    .footer-caption {
        text-align: center;
        max-width: 420px;
        margin: 1.5rem auto 0 auto;
        color: #64748B;
        font-size: 0.78rem;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# Redirect Check
# ==========================================

if AuthManager.is_logged_in():
    st.switch_page("pages/1_Dashboard.py")

# ==========================================
# Grid Columns for Center Alignment
# ==========================================

col_left, col_center, col_right = st.columns([1, 1.2, 1])

with col_center:
    # Brand Header
    st.markdown("""
    <div class="login-brand-header">
        <span class="login-badge">🤖 AI-Powered CRM Suite</span>
        <div class="login-title">Welcome Back</div>
        <div class="login-subtitle">Sign in to access your customer intelligence portal</div>
    </div>
    """, unsafe_allow_html=True)

    # Login Card Form
    with st.form("login_form", clear_on_submit=False):
        email = st.text_input(
            "📧 Email Address",
            placeholder="name@company.com"
        )

        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="••••••••••••"
        )

        st.write("")

        login_btn = st.form_submit_button(
            "Sign In to Workspace →",
            use_container_width=True
        )

    # Authentication Processing
    if login_btn:
        if not email.strip() or not password.strip():
            st.warning("Please enter both email and password.", icon="⚠️")
        else:
            try:
                with st.spinner("Authenticating credentials..."):
                    response = APIClient.login(
                        email=email.strip(),
                        password=password
                    )

                if response.status_code == 200:
                    data = response.json()
                    AuthManager.save_token(data["access_token"])

                    user_response = APIClient.get_current_user()
                    if user_response.status_code == 200:
                        st.session_state.current_user = user_response.json()
                        st.success("Authentication successful! Redirecting...", icon="✅")
                        st.rerun()
                    else:
                        AuthManager.logout()
                        st.error("Failed to load user information.", icon="🚨")
                else:
                    try:
                        err_msg = response.json().get("detail", "Invalid login credentials.")
                    except Exception:
                        err_msg = "Login failed. Please check your credentials."
                    st.error(err_msg, icon="🚨")

            except Exception as e:
                st.error(f"Connection error: Could not connect to API server. ({e})", icon="🔌")

    # Footer
    st.markdown("""
    <div class="footer-caption">
        🔒 Secure Enterprise Auth • 256-bit API Encryption
    </div>
    """, unsafe_allow_html=True)