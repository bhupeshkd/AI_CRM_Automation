import sys
import pandas as pd
import streamlit as st
from pathlib import Path
from st_aggrid import (
    AgGrid,
    GridOptionsBuilder,
    GridUpdateMode,
    DataReturnMode
)

# Root directory configuration
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

from utils.auth import AuthManager
from services.appointment_service import get_all_appointments
from components.dialogs import add_appointment_dialog
from components.lead_details import render_appointment_details
from components.sidebar import render_sidebar
from styles.css_loader import load_css

# ==========================================
# Page Config & Custom Styling
# ==========================================

st.set_page_config(
    page_title="Appointments | AI CRM",
    page_icon="📅",
    layout="wide",
)

load_css()
render_sidebar()
role = AuthManager.get_role()


st.markdown("""
<style>
    /* KPI Card Styling */
    .appt-kpi-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .appt-kpi-label {
        font-size: 0.78rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-weight: 600;
    }
    .appt-kpi-value {
        font-size: 1.85rem;
        font-weight: 700;
        margin-top: 4px;
        color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# Authentication Check
# ==========================================

if not AuthManager.is_logged_in():
    st.switch_page("Home.py")

# ==========================================
# Load Data & Clean HTML Tags
# ==========================================

import re

def clean_value(val):
    if isinstance(val, str):
        return re.sub(r'<[^>]*>', '', val).strip()
    return val

raw_appointments = get_all_appointments() or []

appointments = []
for item in raw_appointments:
    clean_item = item.copy() if isinstance(item, dict) else {}
    if "status" in clean_item:
        clean_item["status"] = clean_value(clean_item["status"])
    appointments.append(clean_item)

# ==========================================
# Header & Action Buttons
# ==========================================

title_col, action_col = st.columns([3, 1], vertical_alignment="center")

with title_col:
    st.title("📅 Appointment Management")
    st.caption("Schedule, track, and manage all client consultations and meetings.")

with action_col:
    act1, act2 = st.columns(2)
    with act1:
        if st.button("🔄 Refresh", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
    with act2:
        if st.button("➕ Appointment", type="primary", use_container_width=True):
            add_appointment_dialog()

st.write("")

# ==========================================
# Top Controls: Search, Selectbox & Export CSV
# ==========================================

with st.container():
    f_col1, f_col2, f_col3 = st.columns([3, 2, 1], vertical_alignment="bottom")

    with f_col1:
        search = st.text_input(
            "🔍 Search Lead ID",
            placeholder="Search by Lead ID...",
            label_visibility="visible"
        )

    with f_col2:
        status = st.selectbox(
            "Status",
            ["All", "Scheduled", "Completed", "Cancelled", "Missed"],
            index=0
        )

    with f_col3:
        if appointments:
            csv_data = pd.DataFrame(appointments).to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Export CSV",
                data=csv_data,
                file_name="appointments.csv",
                mime="text/csv",
                use_container_width=True
            )

# ==========================================
# Filtering Logic
# ==========================================

filtered = []
search_query = search.strip().lower()

for item in appointments:
    raw_status = str(item.get("status", ""))
    
    if status != "All" and status != raw_status:
        continue

    if search_query and search_query not in str(item.get("lead_id", "")).lower():
        continue

    filtered.append(item)

st.write("")

# ==========================================
# KPI Cards Section
# ==========================================

scheduled_cnt = sum(1 for x in filtered if str(x.get("status")) == "Scheduled")
completed_cnt = sum(1 for x in filtered if str(x.get("status")) == "Completed")
missed_cnt = sum(1 for x in filtered if str(x.get("status")) == "Missed")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="appt-kpi-card">
        <div class="appt-kpi-label">📅 Total Filtered</div>
        <div class="appt-kpi-value">{len(filtered)}</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="appt-kpi-card">
        <div class="appt-kpi-label">🕒 Scheduled</div>
        <div class="appt-kpi-value" style="color: #3B82F6;">{scheduled_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="appt-kpi-card">
        <div class="appt-kpi-label">✅ Completed</div>
        <div class="appt-kpi-value" style="color: #10B981;">{completed_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="appt-kpi-card">
        <div class="appt-kpi-label">🚨 Missed</div>
        <div class="appt-kpi-value" style="color: #EF4444;">{missed_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# AgGrid Table Rendering (Plain Text Clean View)
# ==========================================

grid = None
selected_appointment = None

if filtered:
    df = pd.DataFrame(filtered)

    target_cols = [
        "lead_id",
        "appointment_date",
        "meeting_type",
        "status",
    ]

    available_cols = [
        c for c in target_cols
        if c in df.columns
    ]

    display_df = df[available_cols].copy()

    display_df.columns = [
        "Lead ID",
        "Appointment Date",
        "Meeting Type",
        "Status",
    ]

    gb = GridOptionsBuilder.from_dataframe(display_df)
    gb.configure_default_column(
        sortable=True,
        filter=True,
        resizable=True,
    )
    gb.configure_selection(
        selection_mode="single",
        use_checkbox=True,
    )
    gb.configure_pagination(
        enabled=True,
        paginationPageSize=10,
    )

    grid = AgGrid(
        display_df,
        gridOptions=gb.build(),
        height=420,
        theme="streamlit",
        fit_columns_on_grid_load=True,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    )
else:
    st.warning("No Appointments Found.")

# ==========================================
# Selection & Details
# ==========================================

if filtered and grid:
    selected_rows = grid.get("selected_rows", [])

    if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
        lead_id = selected_rows.iloc[0]["Lead ID"]
        selected_appointment = next(
            (x for x in filtered if x.get("lead_id") == lead_id), None
        )
    elif isinstance(selected_rows, list) and len(selected_rows) > 0:
        lead_id = selected_rows[0].get(
    "Lead ID"
)
        selected_appointment = next(
            (x for x in filtered if x.get("lead_id") == lead_id), None
        )

if selected_appointment:
    st.write("")
    render_appointment_details(selected_appointment)

