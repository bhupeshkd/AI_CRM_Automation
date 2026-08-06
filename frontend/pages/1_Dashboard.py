
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Components & Services
from components.sidebar import render_sidebar
# from components.navbar import render_navbar

from styles.css_loader import load_css
from utils.auth import AuthManager
from utils.api import APIClient

# ==========================================
# Page Configuration & Global Setup
# ==========================================

st.set_page_config(
    page_title="AI CRM Dashboard",
    page_icon="📊",
    layout="wide"
)

load_css()


# Inject Dashboard Custom UI Tweaks
st.markdown("""
<style>
    /* Metric Card Styling */
    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 4px;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Header Status Pill */
    .status-pill {
        display: inline-flex;
        align-items: center;
        background: rgba(34, 197, 94, 0.1);
        border: 1px solid rgba(34, 197, 94, 0.3);
        color: #22C55E;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# Authentication Check
# ==========================================

if not AuthManager.is_logged_in():
    st.switch_page("Home.py")

render_sidebar()
user = st.session_state.get("current_user", {})
role = user.get("role", "Sales Executive")
username = user.get("full_name", "User")

is_admin = role == "Admin"
# render_navbar()

# ==========================================
# Fetch Data Safely
# ==========================================

def fetch_data():
    data = {"leads": [], "appointments": [], "followups": [], "conversations": []}
    
    try:
        res = APIClient.get_leads()
        if res.status_code == 200: data["leads"] = res.json()
    except Exception: pass
    
    try:
        res = APIClient.get_appointments()
        if res.status_code == 200: data["appointments"] = res.json()
    except Exception: pass

    try:
        res = APIClient.get_followups()
        if res.status_code == 200: data["followups"] = res.json()
    except Exception: pass

    try:
        res = APIClient.get_conversations()
        if res.status_code == 200: data["conversations"] = res.json()
    # except Exception: pass
    except Exception:
        st.toast(
            "Unable to connect to the backend.",
            icon="⚠️"
        )

    return data

data = fetch_data()

leads = data["leads"]
appointments = data["appointments"]
followups = data["followups"]
conversations = data["conversations"]

total_leads = len(leads)
hot_leads = len([x for x in leads if x.get("qualification_status") == "Hot"])
pending_followups = len([x for x in followups if x.get("status") == "Pending"])
appointment_count = len(appointments)
conversation_count = len(conversations)

conversion = round((hot_leads / total_leads) * 100, 1) if total_leads else 0.0

# ==========================================
# Top Bar & Header Section
# ==========================================

head_left, head_right = st.columns([3, 1], vertical_alignment="center")

with head_left:
    st.title("🤖 AI CRM Dashboard")
    st.caption(f"Welcome back, **{username}** 👋")
    st.caption("Real-time telemetry and pipeline performance analytics")

with head_right:
    c_status, c_btn = st.columns([1.5, 1], vertical_alignment="center")
    with c_status:
        st.markdown('<span class="status-pill">🟢 System Healthy</span>', unsafe_allow_html=True)
    with c_btn:
        if st.button("🔄 Refresh", use_container_width=True):
            st.rerun()

st.caption(f"🕒 Last Synced: {datetime.now().strftime('%d %b %Y • %I:%M %p')}")
st.write("")

# ==========================================
# KPI Cards Section
# ==========================================

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">👥 Total Leads</div>
        <div class="metric-value">{total_leads}</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🔥 Hot Leads</div>
        <div class="metric-value" style="color: #EF4444;">{hot_leads} <span style="font-size:0.9rem; font-weight:normal; color:#94A3B8;">({conversion}%)</span></div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">📅 Appointments</div>
        <div class="metric-value">{appointment_count}</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">📞 Pending Follow-ups</div>
        <div class="metric-value" style="color: #F59E0B;">{pending_followups}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# Analytics & Charts Section
# ==========================================
if is_admin:


    if leads:
        df = pd.DataFrame(leads)

        # st.subheader("📈 Business Analytics")
        if is_admin:
            st.subheader("📋 Operational Overview")
        else:
            st.subheader("📋 Lead Workspace")
        
        tab_overview, tab_pipeline = st.tabs(["📊 Lead Breakdown", "🔀 Pipeline & Priority"])

        # Configure Plotly layout defaults
        plotly_template = "plotly_dark"
        chart_bg = "rgba(0,0,0,0)"

        with tab_overview:
            col1, col2 = st.columns(2)

            with col1:
                if "qualification_status" in df.columns:
                    fig_qual = px.pie(
                        df, 
                        names="qualification_status", 
                        title="Qualification Distribution",
                        hole=0.5,
                        color_discrete_sequence=px.colors.qualitative.Pastel
                    )
                    fig_qual.update_layout(
                        paper_bgcolor=chart_bg, 
                        plot_bgcolor=chart_bg,
                        margin=dict(t=40, b=20, l=20, r=20)
                    )
                    st.plotly_chart(fig_qual, use_container_width=True)

            with col2:
                if "lead_source" in df.columns:
                    fig_source = px.bar(
                        df, 
                        x="lead_source", 
                        title="Lead Acquisition Channels",
                        color_discrete_sequence=["#6366F1"]
                    )
                    fig_source.update_layout(
                        paper_bgcolor=chart_bg, 
                        plot_bgcolor=chart_bg,
                        margin=dict(t=40, b=20, l=20, r=20),
                        xaxis_title=None,
                        yaxis_title="Leads"
                    )
                    st.plotly_chart(fig_source, use_container_width=True)

        with tab_pipeline:
            col3, col4 = st.columns(2)

            with col3:
                if "pipeline_stage" in df.columns:
                    fig_pipe = px.bar(
                        df, 
                        x="pipeline_stage", 
                        title="Deals Stage Breakdown",
                        color_discrete_sequence=["#10B981"]
                    )
                    fig_pipe.update_layout(
                        paper_bgcolor=chart_bg, 
                        plot_bgcolor=chart_bg,
                        margin=dict(t=40, b=20, l=20, r=20),
                        xaxis_title=None,
                        yaxis_title="Count"
                    )
                    st.plotly_chart(fig_pipe, use_container_width=True)

            with col4:
                if "priority" in df.columns:
                    fig_prio = px.histogram(
                        df, 
                        x="priority", 
                        title="Lead Priority Distribution",
                        color_discrete_sequence=["#F59E0B"]
                    )
                    fig_prio.update_layout(
                        paper_bgcolor=chart_bg, 
                        plot_bgcolor=chart_bg,
                        margin=dict(t=40, b=20, l=20, r=20),
                        xaxis_title=None,
                        yaxis_title="Frequency"
                    )
                    st.plotly_chart(fig_prio, use_container_width=True)

else:

    st.markdown(f"""
    # 👋 Welcome Back, {username}

    Manage your leads, follow-ups, appointments, and customer conversations efficiently.
    """)

st.write("")

# ==========================================
# Operational Data Tables (Tabbed)
# ==========================================

# st.subheader("📋 Operational Overview").
if is_admin:
        st.subheader("📋 Operational Overview")
else:
        st.subheader("📋 Lead Workspace")

t_leads, t_appoint, t_follow = st.tabs(["🆕 Recent Leads", "📅 Appointments", "📞 Follow-ups"])

with t_leads:
    if leads:
        lead_df = pd.DataFrame(leads)
        cols = ["full_name", "phone", "city", "qualification_status", "priority"]
        avail = [c for c in cols if c in lead_df.columns]
        
        st.dataframe(
            lead_df[avail].head(10),
            use_container_width=True,
            hide_index=True,
            column_config={
                "full_name": "Lead Name",
                "phone": "Contact",
                "city": "Location",
                "qualification_status": st.column_config.SelectboxColumn("Status", help="Lead Status", options=["Hot", "Warm", "Cold"]),
                "priority": "Priority Level"
            }
        )
    else:
        st.info("No recent leads available.")

with t_appoint:
    if appointments:
        apt_df = pd.DataFrame(appointments)
        cols = ["appointment_date", "meeting_type", "status"]
        avail = [c for c in cols if c in apt_df.columns]
        
        st.dataframe(
            apt_df[avail],
            use_container_width=True,
            hide_index=True,
            column_config={
                "appointment_date": "Scheduled Date/Time",
                "meeting_type": "Type",
                "status": "Meeting Status"
            }
        )
    else:
        st.info("No upcoming appointments scheduled.")

with t_follow:
    pending = [x for x in followups if x.get("status") == "Pending"]
    if pending:
        fol_df = pd.DataFrame(pending)
        cols = ["lead_id", "follow_up_type", "scheduled_at", "status"]
        avail = [c for c in cols if c in fol_df.columns]
        
        st.dataframe(
            fol_df[avail],
            use_container_width=True,
            hide_index=True,
            column_config={
                "lead_id": "Lead ID",
                "follow_up_type": "Action Required",
                "scheduled_at": "Due Date",
                "status": "Status"
            }
        )
    else:
        st.info("No pending follow-ups.")

st.write("")

# ==========================================
# AI Insights & Footer Action
# ==========================================

st.subheader("🤖 AI Real-Time Insights")

ins_col1, ins_col2 = st.columns([3, 1])

with ins_col1:

    if is_admin:

        if hot_leads > 0:
            st.success(
                f"🔥 **High Priority:** {hot_leads} hot leads require immediate engagement.",
                icon="🔥"
            )

        if pending_followups > 0:
            st.warning(
                f"📞 **Action Needed:** You have {pending_followups} pending follow-ups.",
                icon="⚠️"
            )

        if appointment_count > 0:
            st.info(
                f"📅 **Schedule:** {appointment_count} appointments booked across your team.",
                icon="ℹ️"
            )

        if total_leads == 0:
            st.error(
                "No active leads found in database.",
                icon="🚨"
            )

    else:

        st.success(
            "🔥 **Focus:** Prioritize high-value leads to maximize conversions.",
            icon="🔥"
        )

        st.warning(
            "📞 **Reminder:** Complete your pending follow-ups on time.",
            icon="⚠️"
        )

        st.info(
            "📅 **Appointments:** Stay prepared for your upcoming customer meetings.",
            icon="ℹ️"
        )