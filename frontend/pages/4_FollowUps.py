import sys
import re
from pathlib import Path
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

from utils.auth import AuthManager
from services.followup_service import get_all_followups
from services.lead_service import get_all_leads
from components.dialogs import add_followup_dialog
from components.lead_details import render_followup_details
from components.sidebar import render_sidebar
from styles.css_loader import load_css

# ==========================================
# Page Configuration & Custom Styles
# ==========================================

st.set_page_config(
    page_title="Follow Ups | AI CRM",
    page_icon="📞",
    layout="wide",
)

# Inject custom CSS styles globally and render custom sidebar
load_css()
render_sidebar()
role = AuthManager.get_role()

st.markdown("""
<style>
    /* Metric KPI Card Styling */
    .fol-kpi-card {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .fol-kpi-card:hover {
        border-color: rgba(99, 102, 241, 0.4);
        transform: translateY(-2px);
    }
    .fol-kpi-label {
        font-size: 0.78rem;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-weight: 600;
    }
    .fol-kpi-value {
        font-size: 1.85rem;
        font-weight: 700;
        margin-top: 4px;
        color: var(--text-primary);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# Helper Function: Extract Exact Text from HTML
# ==========================================

def clean_html(raw_html):
    """Strips HTML tags like <span style="..."> from string data and gets plain text."""
    if not raw_html or not isinstance(raw_html, str):
        return str(raw_html) if raw_html is not None else ""
    cleaned = re.sub(r'<[^>]*>', '', raw_html).strip()
    return cleaned

# ==========================================
# Authentication Check
# ==========================================

if not AuthManager.is_logged_in():
    st.switch_page("Home.py")

# ==========================================
# Data Fetching & Enrichment
# ==========================================

raw_followups = get_all_followups() or []
leads = get_all_leads() or []

# Lead ID -> Lead Name Lookup Map
lead_map = {str(l.get("id", "")): l.get("full_name", "Unknown Lead") for l in leads if l.get("id")}

followups = []

for item in raw_followups:
    clean_item = item.copy() if isinstance(item, dict) else {}

    # Clean HTML from status explicitly
    if "status" in clean_item:
        clean_item["status"] = clean_html(clean_item.get("status"))

    # Clean HTML from other text fields
    for k in clean_item:
        if isinstance(clean_item[k], str):
            clean_item[k] = clean_html(clean_item[k])

    # Resolve Lead Name from Lead ID
    lead_id_str = str(clean_item.get("lead_id", ""))
    clean_item["lead_name"] = lead_map.get(lead_id_str, lead_id_str[:8] if lead_id_str else "Unknown")

    # Format Timestamps
    raw_scheduled = clean_item.get("scheduled_at")
    if raw_scheduled:
        try:
            clean_item["formatted_scheduled"] = pd.to_datetime(raw_scheduled).strftime("%b %d, %Y • %I:%M %p")
        except Exception:
            clean_item["formatted_scheduled"] = str(raw_scheduled)
    else:
        clean_item["formatted_scheduled"] = "N/A"

    followups.append(clean_item)

# ==========================================
# Header & Top Actions
# ==========================================

title_col, action_col = st.columns([3, 1], vertical_alignment="center")

with title_col:
    st.title("📞 Follow-up Management")
    st.caption("Track, schedule, and complete pending lead follow-ups.")

with action_col:
    act1, act2 = st.columns(2)
    with act1:
        if st.button("🔄 Refresh", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
    with act2:
        if st.button("➕ Follow-up", type="primary", use_container_width=True):
            add_followup_dialog()

st.write("")

# ==========================================
# Search & Filter Controls
# ==========================================

with st.container():
    f_col1, f_col2, f_col3 = st.columns([3, 2, 1], vertical_alignment="bottom")

    with f_col1:
        search = st.text_input(
            "🔍 Search Follow-ups",
            placeholder="Search by Lead Name or Lead ID...",
            label_visibility="visible"
        )

    with f_col2:
        status = st.selectbox(
            "Status",
            ["All", "Pending", "Completed", "Cancelled"],
            index=0
        )

    with f_col3:
        if followups:
            csv_data = pd.DataFrame(followups).to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Export CSV",
                data=csv_data,
                file_name="followups_export.csv",
                mime="text/csv",
                use_container_width=True
            )

# Filter Logic
filtered = []
search_query = search.strip().lower()

for item in followups:
    item_status = str(item.get("status", "")).strip()
    item_lead_id = str(item.get("lead_id", "")).lower()
    item_lead_name = str(item.get("lead_name", "")).lower()

    if status != "All" and item_status != status:
        continue

    if search_query and (search_query not in item_lead_id and search_query not in item_lead_name):
        continue

    filtered.append(item)

st.write("")

# ==========================================
# KPI Cards Section
# ==========================================

pending_cnt = sum(1 for x in filtered if str(x.get("status")).strip() == "Pending")
completed_cnt = sum(1 for x in filtered if str(x.get("status")).strip() == "Completed")
cancelled_cnt = sum(1 for x in filtered if str(x.get("status")).strip() == "Cancelled")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="fol-kpi-card">
        <div class="fol-kpi-label">📞 Total Filtered</div>
        <div class="fol-kpi-value">{len(filtered)}</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="fol-kpi-card">
        <div class="fol-kpi-label">⏳ Pending</div>
        <div class="fol-kpi-value" style="color: #F59E0B;">{pending_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="fol-kpi-card">
        <div class="fol-kpi-label">✅ Completed</div>
        <div class="fol-kpi-value" style="color: #10B981;">{completed_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="fol-kpi-card">
        <div class="fol-kpi-label">🚫 Cancelled</div>
        <div class="fol-kpi-value" style="color: #6B7280;">{cancelled_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# AgGrid Follow-up Table
# ==========================================

selected_followup = None

if filtered:
    df = pd.DataFrame(filtered)

    target_cols = ["lead_name", "follow_up_type", "formatted_scheduled", "status"]
    avail_cols = [c for c in target_cols if c in df.columns]

    display_df = df[avail_cols].copy()
    display_df.rename(columns={
        "lead_name": "Lead Name",
        "follow_up_type": "Type",
        "formatted_scheduled": "Scheduled",
        "status": "Status"
    }, inplace=True)

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

    grid_response = AgGrid(
        display_df,
        gridOptions=gb.build(),
        height=420,
        theme="streamlit",
        fit_columns_on_grid_load=True,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    )

    # Selection Extraction
    selected_rows = grid_response.get("selected_rows", [])

    if selected_rows is not None:
        sel_lead_name = None
        sel_scheduled = None

        if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
            sel_lead_name = selected_rows.iloc[0].get("Lead Name")
            sel_scheduled = str(selected_rows.iloc[0].get("Scheduled"))
        elif isinstance(selected_rows, list) and len(selected_rows) > 0:
            sel_lead_name = selected_rows[0].get("Lead Name")
            sel_scheduled = str(selected_rows[0].get("Scheduled"))

        if sel_lead_name:
            selected_followup = next(
                (
                    x for x in filtered
                    if x.get("lead_name") == sel_lead_name
                    and str(x.get("formatted_scheduled")) == sel_scheduled
                ),
                None
            )

else:
    st.write("")
    st.warning("🔍 No follow-ups match your search criteria.", icon="ℹ️")

# ==========================================
# Follow-up Details Component View
# ==========================================

if selected_followup:
    st.write("")
    st.subheader(f"📄 Follow-up Details: {selected_followup.get('lead_name')}")
    render_followup_details(selected_followup)
else:
    st.caption("💡 Select a row in the table above to view complete follow-up details.")