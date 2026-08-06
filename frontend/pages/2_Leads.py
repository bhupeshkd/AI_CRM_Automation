import sys
from pathlib import Path
import re
import streamlit as st
import pandas as pd
from st_aggrid import (
    AgGrid,
    GridOptionsBuilder,
    GridUpdateMode,
    DataReturnMode
)

# Ensure root directory (frontend/) is in Python module search path
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

from components.lead_details import render_lead_details
from components.dialogs import add_lead_dialog
from services.lead_service import get_all_leads
from utils.auth import AuthManager
from components.sidebar import render_sidebar
from styles.css_loader import load_css

# ==========================================
# Page Configuration & Styling
# ==========================================

st.set_page_config(
    page_title="Lead Directory | AI CRM",
    page_icon="👥",
    layout="wide"
)

load_css()
render_sidebar()
role = AuthManager.get_role()

st.markdown("""
<style>
    .lead-kpi-card {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .lead-kpi-card:hover {
        border-color: rgba(99, 102, 241, 0.4);
        transform: translateY(-2px);
    }
    .lead-kpi-label {
        font-size: 0.78rem;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-weight: 600;
    }
    .lead-kpi-value {
        font-size: 1.85rem;
        font-weight: 700;
        margin-top: 4px;
        color: var(--text-primary);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# Helper Function: Strip HTML Tags
# ==========================================

def clean_html(raw_html):
    """HTML tags like <span style="..."> clean karke sirf inner text extract karta hai."""
    if not raw_html or not isinstance(raw_html, str):
        return str(raw_html) if raw_html is not None else ""
    return re.sub(r'<[^>]*>', '', raw_html).strip()

# ==========================================
# Authentication Check
# ==========================================

if not AuthManager.is_logged_in():
    st.switch_page("Home.py")

# ==========================================
# Data Fetching & Cleaning
# ==========================================

raw_leads = get_all_leads() or []
leads = []

for item in raw_leads:
    clean_item = item.copy() if isinstance(item, dict) else {}

    # Har text field se HTML tags completely remove kar rahe hain
    for key, value in clean_item.items():
        if isinstance(value, str):
            clean_item[key] = clean_html(value)

    leads.append(clean_item)
# ==========================================
# Header & Actions Toolbar
# ==========================================

title_col, action_col = st.columns([3, 1], vertical_alignment="center")

with title_col:
    st.title("👥 Lead Directory")
    st.caption("Filter, analyze, and manage customer leads across pipeline stages.")

with action_col:
    act1, act2 = st.columns(2)
    with act1:
        if st.button("🔄 Refresh", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
    with act2:
        if st.button("➕ Add Lead", type="primary", use_container_width=True):
            add_lead_dialog()

st.write("")

# ==========================================
# Search & Filter Controls
# ==========================================

with st.container():
    f_col1, f_col2, f_col3 = st.columns([3, 2, 1], vertical_alignment="bottom")

    with f_col1:
        search = st.text_input(
            "🔍 Search Leads",
            placeholder="Search by Name, Email, or Phone...",
            label_visibility="visible"
        )

    with f_col2:
        qualification = st.selectbox(
            "Qualification Status",
            ["All", "Hot", "Warm", "Cold"],
            index=0
        )

    with f_col3:
        if leads:
            df_export = pd.DataFrame(leads)
            csv_data = df_export.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Export CSV",
                data=csv_data,
                file_name="leads_export.csv",
                mime="text/csv",
                use_container_width=True
            )

# Filter logic
filtered_leads = []
query = search.strip().lower()

for lead in leads:
    if qualification != "All" and lead.get("qualification_status") != qualification:
        continue

    full_name = str(lead.get("full_name", "")).lower()
    email = str(lead.get("email", "")).lower()
    phone = str(lead.get("phone", "")).lower()

    if not query or (query in full_name or query in email or query in phone):
        filtered_leads.append(lead)

st.write("")

# ==========================================
# KPI Summary Cards
# ==========================================

hot_count = sum(1 for x in filtered_leads if x.get("qualification_status") == "Hot")
warm_count = sum(1 for x in filtered_leads if x.get("qualification_status") == "Warm")
high_priority = sum(1 for x in filtered_leads if x.get("priority") == "High")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="lead-kpi-card">
        <div class="lead-kpi-label">👥 Total Filtered</div>
        <div class="lead-kpi-value">{len(filtered_leads)}</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="lead-kpi-card">
        <div class="lead-kpi-label">🔥 Hot Leads</div>
        <div class="lead-kpi-value" style="color: #EF4444;">{hot_count}</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="lead-kpi-card">
        <div class="lead-kpi-label">🟡 Warm Leads</div>
        <div class="lead-kpi-value" style="color: #F59E0B;">{warm_count}</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="lead-kpi-card">
        <div class="lead-kpi-label">🚨 High Priority</div>
        <div class="lead-kpi-value" style="color: #EC4899;">{high_priority}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# AgGrid Lead Table (Clean Actual Data)
# ==========================================

if filtered_leads:
    df = pd.DataFrame(filtered_leads)

    target_cols = [
        "full_name", "phone", "city", "vehicle_interest", 
        "lead_score", "qualification_status", "priority", "lead_source"
    ]
    available_cols = [c for c in target_cols if c in df.columns]

    display_df = df[available_cols].copy()
    
    col_rename_map = {
        "full_name": "Name",
        "phone": "Phone",
        "city": "City",
        "vehicle_interest": "Vehicle Interest",
        "lead_score": "Score",
        "qualification_status": "Qualification",
        "priority": "Priority",
        "lead_source": "Source"
    }
    display_df.rename(columns=col_rename_map, inplace=True)

    gb = GridOptionsBuilder.from_dataframe(display_df)

    gb.configure_default_column(
        sortable=True,
        filter=True,
        resizable=True,
    )

    gb.configure_pagination(
        enabled=True,
        paginationPageSize=10,
    )

    gb.configure_selection(
        selection_mode="single",
        use_checkbox=True,
    )

    grid_response = AgGrid(
        display_df,
        gridOptions=gb.build(),
        height=420,
        theme="streamlit",
        fit_columns_on_grid_load=True,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED
    )

    selected_rows = grid_response.get("selected_rows", [])
    selected_lead = None

    if selected_rows is not None:
        if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
            selected_name = selected_rows.iloc[0].get("Name")
        elif isinstance(selected_rows, list) and len(selected_rows) > 0:
            selected_name = selected_rows[0].get("Name")
        else:
            selected_name = None

        if selected_name:
            selected_lead = next(
                (l for l in filtered_leads if l.get("full_name") == selected_name),
                None
            )

    if selected_lead:
        st.write("")
        st.subheader(f"📄 Details: {selected_lead.get('full_name')}")
        render_lead_details(selected_lead)

else:
    st.write("")
    st.warning("🔍 No leads match your filter criteria.", icon="ℹ️")