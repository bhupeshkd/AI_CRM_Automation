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

# Load global custom styles
load_css()

# Custom Inline Styling for Centered Auth Card
st.markdown("""
<style>
    /* Center container vertically */
    .block-container {
        max-width: 1000px !important;
        padding-top: 5rem !important;
    }
    
    /* Login Header Card Styling */
    .login-brand-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .login-badge {
        display: inline-block;
        background: rgba(99, 102, 241, 0.15);
        border: 1px solid rgba(99, 102, 241, 0.3);
        color: #818CF8;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 12px;
    }
    
    .login-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 8px;
    }
    
    .login-subtitle {
        color: #94A3B8;
        font-size: 0.95rem;
    }

    /* Input Form Container Card */
    div[data-testid="stForm"] {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 2.5rem 2rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# Redirect Check
# ==========================================

if AuthManager.is_logged_in():
    st.switch_page("pages/1_Dashboard.py")

# ==========================================
# Session State Initialization
# ==========================================

# if "access_token" not in st.session_state:
#     st.session_state.access_token = None

# ==========================================
# Centered Layout Setup
# ==========================================

_, center_col, _ = st.columns([1, 2, 1])

with center_col:
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
            use_container_width=True,
            type="primary"
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
                    AuthManager.save_token(
                        data["access_token"]
                    )

                    user_response = APIClient.get_current_user()
                    if user_response.status_code == 200:

                        st.session_state.current_user = (
                            user_response.json()
                        )
                        st.success(
                            "Authentication successful! Redirecting...",
                            icon="✅"
                        )
                        st.rerun()
                    else:

                        AuthManager.logout()

                        st.error(
                            "Failed to load user information.",
                            icon="🚨"
                        )
                else:
                    try:
                        err_msg = response.json().get("detail", "Invalid login credentials.")
                    except Exception:
                        err_msg = "Login failed. Please check your credentials."
                    st.error(err_msg, icon="🚨")

            except Exception as e:
                st.error(f"Connection error: Could not connect to API server. ({e})", icon="🔌")

    # Bottom Helper Caption
    st.write("")
    st.caption("🔒 Secure Enterprise Auth • 256-bit API Encryption")