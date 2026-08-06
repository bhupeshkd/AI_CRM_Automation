import sys
import re
from pathlib import Path
import streamlit as st
import pandas as pd

from st_aggrid import (
    AgGrid,
    GridOptionsBuilder,
    GridUpdateMode,
    DataReturnMode,
)

# Root directory configuration
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

from utils.auth import AuthManager
from services.conversation_service import get_all_conversations
from services.lead_service import get_all_leads
from components.dialogs import add_conversation_dialog
from components.lead_details import render_conversation_details
from components.sidebar import render_sidebar
from styles.css_loader import load_css

# ==========================================
# Helper Function: Clean HTML Tags
# ==========================================

def clean_html(val):
    """Strips HTML tags from string data so they don't appear in the table."""
    if isinstance(val, str):
        return re.sub(r'<[^>]*>', '', val).strip()
    return val

# ==========================================
# Page Config & Custom Styling (Matches Appointments)
# ==========================================

role = AuthManager.get_role()

st.set_page_config(
    page_title="Conversations | AI CRM",
    page_icon="💬",
    layout="wide",
)

load_css()
render_sidebar()

st.markdown("""
<style>
    /* KPI Card Styling (Matches Appointments Page) */
    .conv-kpi-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .conv-kpi-label {
        font-size: 0.78rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-weight: 600;
    }
    .conv-kpi-value {
        font-size: 1.85rem;
        font-weight: 700;
        margin-top: 4px;
        color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# Authentication
# ==========================================

if not AuthManager.is_logged_in():
    st.switch_page("Home.py")

# ==========================================
# Load & Clean Data
# ==========================================

raw_conversations = get_all_conversations() or []

conversations = []
for item in raw_conversations:
    cleaned_item = item.copy() if isinstance(item, dict) else {}

    for k, v in cleaned_item.items():
        cleaned_item[k] = clean_html(v)
    conversations.append(cleaned_item)

# ==========================================
# Header & Action Buttons
# ==========================================

title_col, action_col = st.columns([3, 1], vertical_alignment="center")

with title_col:
    st.title("💬 Conversation Management")
    st.caption("Track customer communications across calls, emails, WhatsApp, and SMS.")

with action_col:
    act1, act2 = st.columns(2)
    with act1:
        if st.button("🔄 Refresh", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
    with act2:
        if st.button("➕ Conversation", type="primary", use_container_width=True):
            add_conversation_dialog()

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
        message_type = st.selectbox(
            "Message Type",
            ["All", "Call", "WhatsApp", "Email", "SMS", "Note"],
            index=0
        )

    with f_col3:
        if conversations:
            df_export = pd.DataFrame(conversations)
            csv_data = df_export.to_csv(
                        index=False
                    ).encode("utf-8")

            st.download_button(
                label="📥 Export CSV",
                data=csv_data,
                file_name="conversations.csv",
                mime="text/csv",
                use_container_width=True
            )

# ==========================================
# Filter Logic
# ==========================================

filtered = []

for item in conversations:
    if message_type != "All":
        if item.get("message_type") != message_type:
            continue
    search_query = search.strip().lower()
    if search_query:
        if search_query not in str(
            item.get("lead_id", "")
        ).lower():
            continue

    filtered.append(item)

st.write("")

# ==========================================
# KPI Cards Breakdown (Matches Appointments UI Style)
# ==========================================

total_cnt = len(filtered)
call_cnt = sum(1 for x in filtered if x.get("message_type") == "Call")
wa_cnt = sum(1 for x in filtered if x.get("message_type") == "WhatsApp")
email_cnt = sum(1 for x in filtered if x.get("message_type") == "Email")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="conv-kpi-card">
        <div class="conv-kpi-label">💬 Total Interactions</div>
        <div class="conv-kpi-value">{total_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="conv-kpi-card">
        <div class="conv-kpi-label">📞 Calls</div>
        <div class="conv-kpi-value" style="color: #3B82F6;">{call_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="conv-kpi-card">
        <div class="conv-kpi-label">📲 WhatsApp</div>
        <div class="conv-kpi-value" style="color: #22C55E;">{wa_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="conv-kpi-card">
        <div class="conv-kpi-label">✉️ Emails</div>
        <div class="conv-kpi-value" style="color: #8B5CF6;">{email_cnt}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# AgGrid Table Rendering
# ==========================================

selected_conversation = None

if filtered:
    df = pd.DataFrame(filtered)

    display_df = df[
        [
            "lead_id",
            "sender",
            "message_type",
            "created_at",
        ]
    ].copy()

    display_df.columns = [
        "Lead ID",
        "Sender",
        "Type",
        "Created",
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
    st.warning("No Conversations Found.")

# ==========================================
# Selected Row & Details View
# ==========================================

if filtered and 'grid' in locals() and grid:
    selected_rows = grid.get("selected_rows", [])

    if isinstance(selected_rows, pd.DataFrame) and not selected_rows.empty:
        lead_id = selected_rows.iloc[0]["Lead ID"]
        created = str(selected_rows.iloc[0]["Created"])

        selected_conversation = next(
            (
                item for item in filtered
                if item.get("lead_id") == lead_id and str(item.get("created_at")) == created
            ),
            None,
        )
    elif isinstance(selected_rows, list) and len(selected_rows) > 0:
        lead_id = selected_rows[0]["Lead ID"]
        created = str(selected_rows[0]["Created"])

        selected_conversation = next(
            (
                item for item in filtered
                if item.get("lead_id") == lead_id and str(item.get("created_at")) == created
            ),
            None,
        )

if selected_conversation:
    st.write("")
    render_conversation_details(selected_conversation)