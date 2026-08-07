import streamlit as st
from datetime import datetime
from components.dialogs import (
    edit_lead_dialog,
    delete_lead_dialog,
    edit_appointment_dialog,
    delete_appointment_dialog,
    edit_followup_dialog,
    delete_followup_dialog,
    edit_conversation_dialog,
    delete_conversation_dialog,
    add_appointment_dialog,
    add_conversation_dialog
)

# Shared Modern CSS Injection
def _inject_details_css():
    st.markdown("""
    <style>
        .details-wrapper {
            background: #161b22;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 24px;
            margin-top: 12px;
            margin-bottom: 20px;
        }

        .info-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 12px;
            padding: 18px 20px;
            height: 100%;
        }

        .card-header {
            font-size: 0.88rem;
            font-weight: 700;
            color: #818CF8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .data-item {
            margin-bottom: 12px;
        }
        
        .data-label {
            font-size: 0.75rem;
            color: #94A3B8;
            text-transform: uppercase;
            font-weight: 600;
            margin-bottom: 2px;
        }

        .data-value {
            font-size: 0.92rem;
            color: #F8FAFC;
            font-weight: 500;
        }

        .ai-insight-box {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(168, 85, 247, 0.1) 100%);
            border: 1px solid rgba(99, 102, 241, 0.25);
            border-radius: 12px;
            padding: 18px 20px;
            margin-top: 16px;
        }

        .pill-badge {
            display: inline-block;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.78rem;
            font-weight: 600;
        }
        .pill-hot { background: rgba(248, 113, 113, 0.15); color: #F87171; }
        .pill-warm { background: rgba(251, 191, 36, 0.15); color: #FBBF24; }
        .pill-cold { background: rgba(56, 189, 248, 0.15); color: #38BDF8; }
        .pill-high { color: #F43F5E; font-weight: 700; }
        .pill-med { color: #F59E0B; font-weight: 700; }
        
        .tag-chip {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #CBD5E1;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.78rem;
            display: inline-block;
            margin-right: 6px;
            margin-bottom: 6px;
        }

        .code-pill {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #CBD5E1;
            padding: 2px 8px;
            border-radius: 6px;
            font-family: monospace;
            font-size: 0.8rem;
        }
    </style>
    """, unsafe_allow_html=True)


# ==========================================
# Lead Details
# ==========================================

def render_lead_details(lead: dict):
    if not lead or not isinstance(lead, dict):
        st.warning("No lead details available.")
        return

    _inject_details_css()

    full_name = lead.get("full_name", "-")
    email = lead.get("email", "-")
    phone = lead.get("phone", "-")
    city = lead.get("city", "-")
    vehicle = lead.get("vehicle_interest", "-")
    budget = lead.get("budget", 0)
    timeline = lead.get("purchase_timeline", "-")
    source = lead.get("lead_source", "-")

    score = lead.get("lead_score", 0)
    qualification = lead.get("qualification_status", "-")
    priority = lead.get("priority", "-")
    pipeline = lead.get("pipeline_stage", "-")
    follow_up = lead.get("follow_up_in_hours", 0)

    recommended = lead.get("recommended_action", "No Recommendation")
    ai_reason = lead.get("ai_reason", "No Reason Available")

    suggested = lead.get("suggested_appointment_at")
    if suggested:
        try:
            suggested = datetime.fromisoformat(suggested).strftime("%d %b %Y • %I:%M %p")
        except Exception:
            pass

    notes = lead.get("notes", "No Notes")
    tags = lead.get("tags", "No Tags")

    st.markdown('<div class="details-wrapper">', unsafe_allow_html=True)
    st.subheader("👤 Lead Details & Intelligence")
    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-header">👤 Customer Information</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                <div class="data-item">
                    <div class="data-label">Full Name</div>
                    <div class="data-value">{full_name}</div>
                </div>
                <div class="data-item">
                    <div class="data-label">City</div>
                    <div class="data-value">{city}</div>
                </div>
                <div class="data-item">
                    <div class="data-label">Email</div>
                    <div class="data-value"><a href="mailto:{email}" style="color: #818CF8; text-decoration: none;">{email}</a></div>
                </div>
                <div class="data-item">
                    <div class="data-label">Phone</div>
                    <div class="data-value">{phone}</div>
                </div>
                <div class="data-item">
                    <div class="data-label">Vehicle Interest</div>
                    <div class="data-value" style="color: #38BDF8;">{vehicle}</div>
                </div>
                <div class="data-item">
                    <div class="data-label">Budget</div>
                    <div class="data-value">₹{budget:,}</div>
                </div>
                <div class="data-item">
                    <div class="data-label">Timeline</div>
                    <div class="data-value">{timeline}</div>
                </div>
                <div class="data-item">
                    <div class="data-label">Source</div>
                    <div class="data-value">{source}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        qual_class = "pill-hot" if qualification == "Hot" else ("pill-warm" if qualification == "Warm" else "pill-cold")
        prio_color = "pill-high" if priority == "High" else "pill-med"

        st.markdown(f"""
        <div class="info-card">
            <div class="card-header">🎯 AI Qualification</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                <div class="data-item">
                    <div class="data-label">Lead Score</div>
                    <div class="data-value" style="font-size: 1.3rem; font-weight: 800; color: #10B981;">⭐ {score}</div>
                </div>
                <div class="data-item">
                    <div class="data-label">Qualification Status</div>
                    <div class="data-value" style="margin-top: 4px;"><span class="pill-badge {qual_class}">{qualification}</span></div>
                </div>
                <div class="data-item">
                    <div class="data-label">Priority Level</div>
                    <div class="data-value {prio_color}">{priority}</div>
                </div>
                <div class="data-item">
                    <div class="data-label">Pipeline Stage</div>
                    <div class="data-value">{pipeline}</div>
                </div>
                <div class="data-item" style="grid-column: span 2;">
                    <div class="data-label">Suggested Follow-Up</div>
                    <div class="data-value" style="color: #FBBF24;">⏱️ {follow_up} Hours</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # AI Recommendation & Reasoning Callout
    st.markdown(f"""
    <div class="ai-insight-box">
        <div style="color: #A78BFA; font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px;">
            🤖 AI Recommendation & Strategy
        </div>
        <div style="color: #F8FAFC; font-size: 0.92rem; line-height: 1.5; font-weight: 500; margin-bottom: 10px;">
            {recommended}
        </div>
        <div style="color: #94A3B8; font-size: 0.84rem; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px;">
            <strong style="color: #CBD5E1;">AI Reason:</strong> {ai_reason}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Appointment, Notes, and Tags Section
    b1, b2 = st.columns([1.2, 1])

    with b1:
        status = lead.get("appointment_recommendation_status", "N/A")
        status_html = f'<span class="pill-badge pill-warm">🟡 {status}</span>' if status == "Awaiting Confirmation" else (
            f'<span class="pill-badge pill-hot" style="background:rgba(52,211,153,0.15); color:#34D399;">🟢 {status}</span>' if status == "Confirmed" else f'<span class="pill-badge pill-cold">{status}</span>'
        )

        st.markdown(f"""
        <div class="info-card">
            <div class="card-header">📅 Appointment Suggestion</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                <div class="data-item">
                    <div class="data-label">Suggested Date</div>
                    <div class="data-value" style="color: #38BDF8;">{suggested or '-'}</div>
                </div>
                <div class="data-item">
                    <div class="data-label">Meeting Type</div>
                    <div class="data-value">{lead.get('suggested_meeting_type', '-')}</div>
                </div>
                <div class="data-item" style="grid-column: span 2;">
                    <div class="data-label">Status</div>
                    <div class="data-value" style="margin-top: 2px;">{status_html}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with b2:
        st.markdown("""
        <div class="info-card">
            <div class="card-header">🏷️ Notes & Tags</div>
        """, unsafe_allow_html=True)

        if notes and notes != "No Notes":
            st.markdown(f'<div style="font-size: 0.88rem; color: #CBD5E1; margin-bottom: 10px;">{notes}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="font-size: 0.82rem; color: #64748B; margin-bottom: 10px;">No custom notes attached.</div>', unsafe_allow_html=True)

        if isinstance(tags, list) and len(tags) > 0:
            tags_html = "".join([f'<span class="tag-chip">{t}</span>' for t in tags])
            st.markdown(tags_html, unsafe_allow_html=True)
        elif isinstance(tags, str) and tags != "No Tags":
            st.markdown(f'<span class="tag-chip">{tags}</span>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="font-size: 0.82rem; color: #64748B;">No tags assigned.</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    # Action Toolbar
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        if st.button("✏️ Edit", use_container_width=True, key=f"edit_{lead['id']}"):
            edit_lead_dialog(lead)

    with c2:
        if st.button("🗑️ Delete", use_container_width=True, key=f"delete_{lead['id']}"):
            delete_lead_dialog(lead)

    with c3:
        if lead.get("appointment_recommendation_status") == "Awaiting Confirmation":
            if st.button("📅 Book Appointment", type="primary", use_container_width=True, key=f"appointment_{lead['id']}"):
                add_appointment_dialog(lead)
        else:
            st.button("✅ Appointment Processed", disabled=True, use_container_width=True, key=f"apt_proc_{lead['id']}")

    with c4:
        if st.button("💬 Log Conversation", use_container_width=True, key=f"conversation_{lead['id']}"):
            add_conversation_dialog(lead)

    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# Appointment Details
# ==========================================

def render_appointment_details(appointment: dict):
    if not appointment or not isinstance(appointment, dict):
        return

    _inject_details_css()

    status = appointment.get("status", "Unknown")
    status_class = "pill-cold" if status == "Scheduled" else ("pill-hot" if status in ["Cancelled", "Missed"] else "pill-warm")

    st.markdown('<div class="details-wrapper">', unsafe_allow_html=True)
    st.subheader("📅 Appointment Details")
    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-header">📋 Information</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                <div class="data-item">
                    <div class="data-label">Appointment ID</div>
                    <div class="data-value"><span class="code-pill">{appointment.get('id', '-')}</span></div>
                </div>
                <div class="data-item">
                    <div class="data-label">Lead ID</div>
                    <div class="data-value"><span class="code-pill">{appointment.get('lead_id', '-')}</span></div>
                </div>
                <div class="data-item">
                    <div class="data-label">Meeting Type</div>
                    <div class="data-value">{appointment.get('meeting_type', '-')}</div>
                </div>
                <div class="data-item">
                    <div class="data-label">Appointment Date</div>
                    <div class="data-value" style="color: #38BDF8;">{appointment.get('appointment_date', '-')}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-header">📊 Status & Timeline</div>
            <div class="data-item">
                <div class="data-label">Current Status</div>
                <div class="data-value" style="margin-top: 4px;"><span class="pill-badge {status_class}">{status}</span></div>
            </div>
            <div class="data-item" style="margin-top: 14px;">
                <div class="data-label">Created At</div>
                <div class="data-value">{appointment.get('created_at', '-')}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("✏️ Edit Appointment", use_container_width=True, key=f"edit_app_{appointment['id']}"):
            edit_appointment_dialog(appointment)

    with c2:
        if st.button("🗑️ Delete Appointment", use_container_width=True, key=f"delete_app_{appointment['id']}"):
            delete_appointment_dialog(appointment)

    with c3:
        if st.button("✅ Mark Completed", type="primary", use_container_width=True, key=f"complete_app_{appointment['id']}"):
            edit_appointment_dialog({
                **appointment,
                "status": "Completed"
            })

    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# Follow-up Details
# ==========================================

def render_followup_details(followup: dict):
    if not followup or not isinstance(followup, dict):
        return

    _inject_details_css()

    status = followup.get("status", "Unknown")
    status_class = "pill-warm" if status == "Pending" else ("pill-hot" if status == "Cancelled" else "pill-cold")

    st.markdown('<div class="details-wrapper">', unsafe_allow_html=True)
    st.subheader("📞 Follow-up Details")
    st.write("")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-header">📞 Information</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                <div class="data-item">
                    <div class="data-label">ID</div>
                    <div class="data-value"><span class="code-pill">{followup.get('id', '-')}</span></div>
                </div>
                <div class="data-item">
                    <div class="data-label">Lead ID</div>
                    <div class="data-value"><span class="code-pill">{followup.get('lead_id', '-')}</span></div>
                </div>
                <div class="data-item">
                    <div class="data-label">Follow-up Type</div>
                    <div class="data-value">{followup.get('follow_up_type', '-')}</div>
                </div>
                <div class="data-item">
                    <div class="data-label">Scheduled At</div>
                    <div class="data-value" style="color: #38BDF8;">{followup.get('scheduled_at', '-')}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-header">📝 Remarks & Status</div>
            <div class="data-item">
                <div class="data-label">Status</div>
                <div class="data-value" style="margin-top: 4px;"><span class="pill-badge {status_class}">{status}</span></div>
            </div>
            <div class="data-item" style="margin-top: 10px;">
                <div class="data-label">Remarks</div>
                <div class="data-value" style="color: #CBD5E1;">{followup.get('remarks', 'No Remarks')}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✏️ Edit Follow-up", use_container_width=True, key=f"edit_followup_{followup['id']}"):
            edit_followup_dialog(followup)

    with col2:
        if st.button("🗑️ Delete Follow-up", use_container_width=True, key=f"delete_followup_{followup['id']}"):
            delete_followup_dialog(followup)

    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# Conversation Details
# ==========================================

def render_conversation_details(conversation: dict):
    if not conversation or not isinstance(conversation, dict):
        return

    _inject_details_css()

    st.markdown('<div class="details-wrapper">', unsafe_allow_html=True)
    st.subheader("💬 Conversation Details")
    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-header">💬 Information</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                <div class="data-item">
                    <div class="data-label">Conversation ID</div>
                    <div class="data-value"><span class="code-pill">{conversation.get('id', '-')}</span></div>
                </div>
                <div class="data-item">
                    <div class="data-label">Lead ID</div>
                    <div class="data-value"><span class="code-pill">{conversation.get('lead_id', '-')}</span></div>
                </div>
                <div class="data-item">
                    <div class="data-label">Sender</div>
                    <div class="data-value">{conversation.get('sender', '-')}</div>
                </div>
                <div class="data-item">
                    <div class="data-label">Message Type</div>
                    <div class="data-value" style="color: #C084FC;">{conversation.get('message_type', '-')}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-header">✉️ Message Log</div>
            <div class="data-label">Message Payload</div>
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); padding: 12px; border-radius: 8px; color: #E2E8F0; font-size: 0.88rem; margin-top: 4px;">
                {conversation.get('message', 'No Message')}
            </div>
            <div class="data-item" style="margin-top: 10px;">
                <div class="data-label">Logged At</div>
                <div class="data-value" style="font-size: 0.8rem; color: #94A3B8;">{conversation.get('created_at', '-')}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("✏️ Edit Conversation", use_container_width=True, key=f"edit_conv_{conversation['id']}"):
            edit_conversation_dialog(conversation)

    with c2:
        if st.button("🗑️ Delete Conversation", use_container_width=True, key=f"delete_conv_{conversation['id']}"):
            delete_conversation_dialog(conversation)

    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# Activity Details
# ==========================================

def render_activity_details(activity: dict):
    if not activity or not isinstance(activity, dict):
        return

    _inject_details_css()

    st.markdown('<div class="details-wrapper">', unsafe_allow_html=True)
    st.subheader("📋 Activity Details")
    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-header">📋 Information</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                <div class="data-item">
                    <div class="data-label">Activity ID</div>
                    <div class="data-value"><span class="code-pill">{activity.get('id', '-')}</span></div>
                </div>
                <div class="data-item">
                    <div class="data-label">Lead ID</div>
                    <div class="data-value"><span class="code-pill">{activity.get('lead_id', '-')}</span></div>
                </div>
                <div class="data-item" style="grid-column: span 2;">
                    <div class="data-label">Activity Type</div>
                    <div class="data-value" style="color: #818CF8; font-weight: 600;">{activity.get('activity_type', '-')}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-header">📝 Description & Timeline</div>
            <div class="data-label">Description</div>
            <div style="color: #CBD5E1; font-size: 0.88rem; margin-bottom: 10px;">
                {activity.get('description', 'No Description')}
            </div>
            <div class="data-item">
                <div class="data-label">Logged At</div>
                <div class="data-value" style="font-size: 0.8rem; color: #94A3B8;">{activity.get('created_at', '-')}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)