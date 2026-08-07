import sys
import re

from pathlib import Path
from datetime import datetime

import pandas as pd
import streamlit as st

# ==========================================
# Root
# ==========================================

root_dir = Path(__file__).resolve().parent.parent

if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

from utils.auth import AuthManager
from services.activity_service import get_all_activities
from components.sidebar import render_sidebar
from styles.css_loader import load_css

st.markdown("""
<style>

/* ===========================
    HEADER
=========================== */

.page-title{

    font-size:34px;

    font-weight:700;

    color:white;

    margin-bottom:4px;

}

.page-subtitle{

    color:#94A3B8;

    font-size:15px;

    margin-bottom:25px;

}


/* ===========================
    KPI CARD
=========================== */

.metric-card{

    background:#111827;

    border:1px solid #232B3B;

    border-radius:18px;

    padding:20px;

    transition:.25s;

}

.metric-card:hover{

    transform:translateY(-3px);

    border-color:#3B82F6;

}

.metric-icon{

    font-size:28px;

}

.metric-value{

    color:white;

    font-size:34px;

    font-weight:700;

    margin-top:10px;

}

.metric-title{

    color:#94A3B8;

    margin-top:6px;

}


/* ===========================
      TIMELINE
=========================== */

.activity-card{

    background:#111827;

    border-radius:18px;

    padding:18px;

    margin-bottom:18px;

    border:1px solid #232B3B;

    transition:.25s;

}

.activity-card:hover{

    transform:translateY(-2px);

    border-color:#3B82F6;

}

.activity-header{

    display:flex;

    justify-content:space-between;

    align-items:center;

}

.activity-title{

    font-size:18px;

    font-weight:700;

    color:white;

}

.activity-date{

    color:#94A3B8;

    font-size:13px;

}

.activity-description{

    color:#CBD5E1;

    margin-top:12px;

    line-height:1.6;

}


/* ===========================
      BADGE
=========================== */

.badge{

    display:inline-block;

    padding:4px 10px;

    border-radius:30px;

    font-size:12px;

    font-weight:600;

    margin-top:10px;

}

.badge-lead{

    background:#052E16;

    color:#4ADE80;

}

.badge-appointment{

    background:#172554;

    color:#60A5FA;

}

.badge-conversation{

    background:#3B0764;

    color:#C084FC;

}

.badge-follow{

    background:#431407;

    color:#FB923C;

}

.badge-ai{

    background:#312E81;

    color:#A78BFA;

}


/* ===========================
      LEAD ID
=========================== */

.lead-pill{

    display:inline-block;

    padding:6px 12px;

    border-radius:25px;

    background:#1E293B;

    color:#CBD5E1;

    font-size:12px;

    margin-top:14px;

}

</style>

""",unsafe_allow_html=True)

# ==========================================
# Helpers
# ==========================================

def get_icon(activity):
    activity = activity.lower()

    if "lead" in activity:
        return "👤"

    elif "appointment" in activity:
        return "📅"

    elif "conversation" in activity:
        return "💬"

    elif "follow" in activity:
        return "📞"

    elif "ai" in activity:
        return "🤖"
    return "⚡"

from datetime import datetime
from zoneinfo import ZoneInfo

def format_time(value):
    try:
        dt = datetime.fromisoformat(value)
        # Agar database se timezone-naive UTC datetime aa raha hai
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=ZoneInfo("UTC"))
        # UTC -> IST
        dt = dt.astimezone(
            ZoneInfo("Asia/Kolkata")
        )
        return dt.strftime(
            "%d %b %Y • %I:%M %p"
        )
    except Exception:
        return value
    
# ==========================================
# Page Config
# ==========================================

st.set_page_config(
    page_title="Activity Timeline",
    page_icon="📋",
    layout="wide",
)

load_css()
render_sidebar()

if not AuthManager.is_logged_in():
    st.switch_page("Home.py")

# ==========================================
# Load Activities
# ==========================================

activities = get_all_activities() or []

for item in activities:
    for key, value in item.items():
        if isinstance(value, str):
            item[key] = re.sub(
                r"<[^>]*>",
                "",
                value
            ).strip()


# ==========================================
# Header
# ==========================================
left,right=st.columns([5,1])
with left:
    st.markdown("""

<div class="page-title">

📋 Activity Timeline

</div>

<div class="page-subtitle">

Track every automated and manual action inside your CRM.

</div>

""",unsafe_allow_html=True)

with right:

    st.button(
        "🔄 Refresh",
        use_container_width=True
    )


# ==========================================
# Search & Filter
# ==========================================

c1, c2 = st.columns([3,1])

with c1:

    search = st.text_input(
        "🔍 Search",
        placeholder="Lead ID, Activity..."
    )

with c2:

    filter_type = st.selectbox(
        "Filter",
        [
            "All",
            "Lead",
            "Appointment",
            "Conversation",
            "Follow-up",
            "AI"
        ]
    )


# ==========================================
# Filtering
# ==========================================

filtered = []
search = search.lower().strip()
for activity in activities:

    activity_type = activity.get(
        "activity_type",
        ""
    )
    if filter_type != "All":
        if filter_type.lower() not in activity_type.lower():
            continue
    if search:
        text = (
            str(activity.get("lead_id",""))
            + " "
            + activity_type
            + " "
            + str(activity.get("description",""))
        ).lower()
        if search not in text:
            continue

    filtered.append(activity)

# ==========================================
# KPI Calculation
# ==========================================

lead_events = sum(
    1
    for x in filtered
    if "lead" in x.get(
        "activity_type",
        ""
    ).lower()
)

appointment_events = sum(
    1
    for x in filtered
    if "appointment" in x.get(
        "activity_type",
        ""
    ).lower()
)

conversation_events = sum(
    1
    for x in filtered
    if "conversation" in x.get(
        "activity_type",
        ""
    ).lower()
)

followup_events = sum(
    1
    for x in filtered
    if "follow" in x.get(
        "activity_type",
        ""
    ).lower()
)

# ==========================================
# KPI
# ==========================================
k1,k2,k3,k4,k5=st.columns(5)

cards=[
("⚡",len(filtered),"Total"),
("👤",lead_events,"Leads"),
("📅",appointment_events,"Appointments"),
("💬",conversation_events,"Conversations"),
("📞",followup_events,"Follow-ups")
]

for col,data in zip(
    [k1,k2,k3,k4,k5],
    cards
):

    icon,value,title=data

    with col:

        st.markdown(f"""

<div class="metric-card">

<div class="metric-icon">

{icon}

</div>

<div class="metric-value">

{value}

</div>

<div class="metric-title">

{title}

</div>

</div>

""",unsafe_allow_html=True)
st.divider()
# ==========================================
# Timeline
# ==========================================

if not filtered:

    st.info("No activities found.")

    st.stop()


st.subheader("🕒 Activity Feed")

st.caption(
    "Latest system events in chronological order."
)

# Latest first
filtered.sort(
    key=lambda x: x.get("created_at", ""),
    reverse=True
)

for activity in filtered:

    icon = get_icon(
        activity.get(
            "activity_type",
            ""
        )
    )

    activity_type = activity.get(
        "activity_type",
        "-"
    )

    created = format_time(
        activity.get(
            "created_at",
            "-"
        )
    )

    description = activity.get(
        "description",
        "No Description"
    )

    lead_id = activity.get(
        "lead_id",
        "-"
    )

    with st.container(border=True):

        left, right = st.columns(
            [8,2]
        )

        with left:

            st.markdown(
                f"### {icon} {activity_type}"
            )

            st.caption(created)

            st.write(description)

        with right:

            st.caption("Lead ID")

            st.code(
                lead_id
            )

        with st.expander(
            "📄 View Details"
        ):

            st.markdown(
                f"**Activity Type** : {activity_type}"
            )

            st.markdown(
                f"**Lead ID** : `{lead_id}`"
            )

            st.markdown(
                f"**Created At** : {created}"
            )

            st.markdown(
                "### Description"
            )

            st.write(description)

    st.write("")