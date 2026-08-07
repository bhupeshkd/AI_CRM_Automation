import streamlit as st
from utils.auth import AuthManager

def render_sidebar():
    """
    Renders a modern SaaS navigation sidebar with dynamic CSS injections,
    clean user profile layout, and refined navigation styles.
    """
    
    # CSS Customizations & Overrides
    st.markdown("""
    <style>
        /* Base Variables with Theme Fallbacks */
        :root {
            --brand-primary: #6366F1;
            --brand-primary-soft: rgba(99, 102, 241, 0.15);
            --border-subtle: rgba(255, 255, 255, 0.08);
            --bg-card-subtle: rgba(255, 255, 255, 0.03);
            --text-muted: #94A3B8;
        }

        /* Branding Header */
        .sidebar-brand {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 8px 4px 16px 4px;
            border-bottom: 1px solid var(--border-subtle);
            margin-bottom: 12px;
        }
        .brand-icon-box {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            background: var(--brand-primary-soft);
            border: 1px solid rgba(99, 102, 241, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.25rem;
            flex-shrink: 0;
        }
        .brand-title {
            font-size: 1.05rem;
            font-weight: 700;
            line-height: 1.2;
            color: var(--text-primary, #F8FAFC);
        }
        .brand-sub {
            font-size: 0.72rem;
            color: var(--text-muted);
            margin-top: 2px;
        }
        
        /* Section Dividers */
        .sidebar-section-label {
            font-size: 0.68rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-muted);
            margin: 18px 0px 6px 4px;
        }

        /* Streamlit Native Navigation Override */
        [data-testid="stSidebar"] [data-testid="stPageLink-NavLink"] {
            border-radius: 8px;
            transition: all 0.2s ease;
            padding: 6px 12px;
        }
        
        /* User Profile Card */
        .user-profile-card {
            background: var(--bg-card-subtle);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 10px 12px;
            display: flex;
            align-items: center;
            gap: 10px;
            margin-top: 16px;
            margin-bottom: 10px;
        }
        .user-avatar {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: var(--brand-primary);
            color: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 0.85rem;
            flex-shrink: 0;
        }
        .user-info-name {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-primary, #F8FAFC);
            line-height: 1.2;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .user-info-role {
            font-size: 0.72rem;
            color: var(--text-muted);
        }

        /* Subtle Logout Button Override */
        [data-testid="stSidebar"] button[kind="secondary"] {
            border: 1px solid var(--border-subtle);
            background: transparent;
            color: #F87171;
            transition: all 0.2s ease;
        }
        [data-testid="stSidebar"] button[kind="secondary"]:hover {
            background: rgba(239, 68, 68, 0.1);
            border-color: rgba(239, 68, 68, 0.3);
            color: #EF4444;
        }
    </style>
    """, unsafe_allow_html=True)

    # Fetch user session info
    user = st.session_state.get("current_user", {})
    username = user.get("full_name", "Bhupesh Dewangan")
    role = user.get("role", "Admin")

    initial = (
        username.strip()[0].upper()
        if username and username.strip()
        else "U"
    )

    with st.sidebar:
        # ==========================================
        # 1. Branding / App Logo Header
        # ==========================================
        st.markdown("""
        <div class="sidebar-brand">
            <div class="brand-icon-box">🤖</div>
            <div>
                <div class="brand-title">AI CRM Pro</div>
                <div class="brand-sub">Smart Sales Workspace</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ==========================================
        # 2. Main Navigation Links
        # ==========================================
        st.markdown(
            '<div class="sidebar-section-label">Main Menu</div>',
            unsafe_allow_html=True
        )

        st.page_link(
            "pages/1_Dashboard.py",
            label="Dashboard",
            icon="📊",
            use_container_width=True,
        )

        st.page_link(
            "pages/2_Leads.py",
            label="Lead Directory",
            icon="👥",
            use_container_width=True,
        )

        # ==========================================
        # 3. Operations & Activities Group
        # ==========================================
        st.markdown(
            '<div class="sidebar-section-label">Operations</div>',
            unsafe_allow_html=True
        )

        st.page_link(
            "pages/3_Appointments.py",
            label="Appointments",
            icon="📅",
            use_container_width=True,
        )

        st.page_link(
            "pages/4_FollowUps.py",
            label="Follow-ups",
            icon="📞",
            use_container_width=True,
        )

        st.page_link(
            "pages/5_Conversations.py",
            label="Conversations",
            icon="💬",
            use_container_width=True,
        )

        st.markdown(
            '<div class="sidebar-section-label">Activity Logs</div>',
            unsafe_allow_html=True
        )

        st.page_link(
            "pages/6_Activity.py",
            label="Activity",
            icon="📋",
            use_container_width=True,
        )

        # ==========================================
        # 4. User Profile & Logout Section
        # ==========================================
        st.markdown(f"""
        <div class="user-profile-card">
            <div class="user-avatar">{initial}</div>
            <div style="overflow: hidden;">
                <div class="user-info-name">{username}</div>
                <div class="user-info-role">{role}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚪 Logout", use_container_width=True, type="secondary"):
            AuthManager.logout()
            st.switch_page("Home.py")
