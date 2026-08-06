import streamlit as st
from utils.auth import AuthManager

def render_sidebar():
    """
    Renders a modern SaaS navigation sidebar with active page 
    highlighting, theme switcher, user profile info, and logout controls.
    """
    
    # Dynamic CSS injection relying on CSS Variables from custom.css
    st.markdown("""
    <style>
        /* App Branding Header */
        .sidebar-brand {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 8px 4px 16px 4px;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 16px;
        }
        .brand-icon {
            font-size: 1.8rem;
            background: rgba(99, 102, 241, 0.2);
            padding: 8px;
            border-radius: 10px;
            border: 1px solid rgba(99, 102, 241, 0.4);
        }
        .brand-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-primary);
            line-height: 1.2;
        }
        .brand-sub {
            font-size: 0.75rem;
            color: var(--text-secondary);
        }
        
        /* Section Headers */
        .sidebar-section-label {
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-secondary);
            margin: 16px 0px 8px 4px;
        }
        
        /* User Profile Footer Card */
        .user-profile-card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 10px 12px;
            display: flex;
            align-items: center;
            gap: 10px;
            margin-top: 16px;
            margin-bottom: 12px;
        }
        .user-avatar {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: #6366F1;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 0.85rem;
        }
        .user-info-name {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-primary);
        }
        .user-info-role {
            font-size: 0.72rem;
            color: var(--text-secondary);
        }
    </style>
    """, unsafe_allow_html=True)

    user = st.session_state.get("current_user", {})

    username = user.get("full_name", "Unknown User")
    role = user.get("role", "Sales Executive")

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
            <div class="brand-icon">🤖</div>
            <div>
                <div class="brand-title">AI CRM Pro</div>
                <div class="brand-sub">Smart Sales Workspace</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        # ==========================================
        # 3. Main Navigation Links
        # ==========================================
        st.markdown(
            '<div class="sidebar-section-label">Main Menu</div>',
            unsafe_allow_html=True
        )

        st.page_link(
            "pages/1_Dashboard.py",
            label="📊 Dashboard",
            use_container_width=True,
        )

        st.page_link(
            "pages/2_Leads.py",
            label="👥 Lead Directory",
            use_container_width=True,
        )

        # ==========================================
        # 4. Operations & Activities Group
        # ==========================================
        st.markdown(
            '<div class="sidebar-section-label">Operations</div>',
            unsafe_allow_html=True
        )

        st.page_link(
            "pages/3_Appointments.py",
            label="📅 Appointments",
            use_container_width=True,
        )

        st.page_link(
            "pages/4_Followups.py",
            label="📞 Follow-ups",
            use_container_width=True,
        )

        st.page_link(
            "pages/5_Conversations.py",
            label="💬 Conversations",
            use_container_width=True,
        )

        # ==========================================
        # 5. User Profile & Logout Section
        # ==========================================

        st.markdown(f"""
        <div class="user-profile-card">
            <div class="user-avatar">{initial}</div>
            <div>
                <div class="user-info-name">{username}</div>
                <div class="user-info-role">{role}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚪 Logout", use_container_width=True, type="primary"):
            AuthManager.logout()
            st.switch_page("Home.py")
