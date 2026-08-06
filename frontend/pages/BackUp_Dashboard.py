import streamlit as st
import pandas as pd
import plotly.express as px
from components.sidebar import render_sidebar
from utils.style import load_css

from utils.auth import AuthManager
from utils.api import APIClient
# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)
load_css()

# ==========================================
# Authentication Check
# ==========================================


if not AuthManager.is_logged_in():
    st.switch_page("Home.py")

render_sidebar()

# ==========================================
# Load Dashboard Data
# ==========================================

leads = []
appointments = []
followups = []
conversations = []

try:
    response = APIClient.get_leads()
    if response.status_code == 200:
        leads = response.json()
except:
    pass

try:
    response = APIClient.get_appointments()
    if response.status_code == 200:
        appointments = response.json()
except:
    pass

try:
    response = APIClient.get_followups()
    if response.status_code == 200:
        followups = response.json()
except:
    pass

try:
    response = APIClient.get_conversations()
    if response.status_code == 200:
        conversations = response.json()
except:
    pass

total_leads = len(leads)

hot_leads = len(
    [
        x for x in leads
        if x["qualification_status"] == "Hot"
    ]
)

pending_followups = len(
    [
        x for x in followups
        if x["status"] == "Pending"
    ]
)

conversation_count = len(conversations)
appointment_count = len(appointments)

# ==========================================
# Dashboard UI
# ==========================================

st.title("🤖 AI CRM Dashboard")

st.caption(
    "AI Powered Customer Relationship Management System"
)

st.success("Welcome back! Here's your business overview.")

st.divider()


c1, c2, c3 = st.columns(3)

with c1:
    st.metric("👥 Total Leads", total_leads)

with c2:
    st.metric("🔥 Hot Leads", hot_leads)

with c3:
    st.metric("📅 Appointments", appointment_count)

c4, c5, c6 = st.columns(3)

with c4:
    st.metric("📞 Pending Follow-ups", pending_followups)

with c5:
    st.metric("💬 Conversations", conversation_count)

with c6:
    conversion = round(
        (hot_leads / total_leads) * 100,
        1
    ) if total_leads else 0

    st.metric(
        "⭐ Hot Lead %",
        f"{conversion}%"
    )


st.divider()

if leads:

    df = pd.DataFrame(leads)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        fig = px.pie(
            df,
            names="qualification_status",
            title="Lead Qualification"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        fig = px.bar(
            df,
            x="lead_source",
            title="Lead Sources"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            df,
            x="pipeline_stage",
            title="Pipeline Stage"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        fig = px.histogram(
            df,
            x="priority",
            title="Priority Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.divider()

st.subheader("🆕 Recent Leads")

if leads:

    lead_df = pd.DataFrame(leads)

    cols = [
        "full_name",
        "phone",
        "city",
        "qualification_status",
        "priority",
    ]

    available = [
        c
        for c in cols
        if c in lead_df.columns
    ]

    st.dataframe(
        lead_df[available].head(10),
        use_container_width=True,
        hide_index=True,
    )

st.divider()

st.subheader("📅 Upcoming Appointments")

if appointments:

    appointment_df = pd.DataFrame(appointments)

    cols = [
        "appointment_date",
        "meeting_type",
        "status",
    ]

    available = [
        c
        for c in cols
        if c in appointment_df.columns
    ]

    st.dataframe(
        appointment_df[available],
        use_container_width=True,
        hide_index=True,
    )
st.divider()

st.subheader("📞 Pending Follow-ups")

pending = [
    x for x in followups
    if x["status"] == "Pending"
]

if pending:

    followup_df = pd.DataFrame(pending)

    columns = [
        "lead_id",
        "follow_up_type",
        "scheduled_at",
        "status",
    ]

    # Sirf wahi columns dikhao jo available hain
    available_columns = [
        col
        for col in columns
        if col in followup_df.columns
    ]

    st.dataframe(
        followup_df[available_columns],
        use_container_width=True,
        hide_index=True,
    )

else:

    st.info("No pending follow-ups.")



st.divider()

st.subheader("🤖 AI Insights")

if hot_leads > 0:
    st.success(f"🔥 {hot_leads} hot leads need immediate attention.")

if pending_followups > 0:
    st.warning(f"📞 {pending_followups} follow-ups are pending.")

if appointment_count > 0:
    st.info(f"📅 {appointment_count} appointments are scheduled.")

if total_leads == 0:
    st.error("No leads available in CRM.")


st.divider()

if st.button(
    "Logout",
    use_container_width=True
):

    AuthManager.logout()

    st.switch_page("Home.py")