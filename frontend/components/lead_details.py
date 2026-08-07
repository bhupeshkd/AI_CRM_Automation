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




# ==========================================
# Lead Details
# ==========================================

def render_lead_details(lead: dict):

    st.divider()
    st.subheader("👤 Lead Details")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Customer Information")

        st.write(f"**Full Name :** {lead.get('full_name', '-')}")
        st.write(f"**Email :** {lead.get('email', '-')}")
        st.write(f"**Phone :** {lead.get('phone', '-')}")
        st.write(f"**City :** {lead.get('city', '-')}")
        st.write(f"**Vehicle :** {lead.get('vehicle_interest', '-')}")
        st.write(f"**Budget :** ₹{lead.get('budget', 0):,}")
        st.write(f"**Timeline :** {lead.get('purchase_timeline', '-')}")
        st.write(f"**Source :** {lead.get('lead_source', '-')}")

    with col2:

        st.markdown("### AI Qualification")

        st.write(f"**Lead Score :** ⭐ {lead.get('lead_score', 0)}")
        st.write(f"**Qualification :** {lead.get('qualification_status', '-')}")
        st.write(f"**Priority :** {lead.get('priority', '-')}")
        st.write(f"**Pipeline :** {lead.get('pipeline_stage', '-')}")
        st.write(f"**Follow Up :** {lead.get('follow_up_in_hours', 0)} Hours")

    st.divider()

    suggested = lead.get("suggested_appointment_at")

    if suggested:
        try:
            suggested = datetime.fromisoformat(suggested).strftime(
                "%d %b %Y • %I:%M %p"
            )
        except Exception:
            pass

    st.markdown("### 🤖 AI Recommendation")
    st.info(lead.get("recommended_action", "No Recommendation"))

    st.markdown("### 🧠 AI Reason")
    st.write(lead.get("ai_reason", "No Reason Available"))

    st.divider()

    st.subheader("📅 Appointment Suggestion")

    left, right = st.columns(2)

    with left:
        st.write(f"**📅 Suggested Date :** {suggested or '-'}")
        st.write(
            f"**🚗 Meeting Type :** "
            f"{lead.get('suggested_meeting_type', '-')}"
        )

    with right:
        status = lead.get(
            "appointment_recommendation_status",
            "N/A"
        )

        if status == "Awaiting Confirmation":
            st.warning("🟡 Awaiting Confirmation")
        elif status == "Confirmed":
            st.success("🟢 Confirmed")
        elif status == "Rejected":
            st.error("🔴 Rejected")
        else:
            st.info(status)
    st.divider()

    st.markdown("### 📝 Notes")
    st.write(lead.get("notes", "No Notes"))

    st.markdown("### 🏷️ Tags")
    st.write(lead.get("tags", "No Tags"))

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        if st.button("✏ Edit", use_container_width=True, key=f"edit_{lead['id']}"):
            edit_lead_dialog(lead)

    with c2:
        if st.button("🗑 Delete", use_container_width=True, key=f"delete_{lead['id']}"):
            delete_lead_dialog(lead)

    with c3:

        if (
            lead.get("appointment_recommendation_status")
            == "Awaiting Confirmation"
        ):

            if st.button(
                "📅 Book Appointment",
                use_container_width=True,
                key=f"appointment_{lead['id']}"
            ):  
                add_appointment_dialog(lead)

        else:

            st.success("✅ Appointment Processed")

        with c4:
            if st.button(
                "💬 Conversation",
                use_container_width=True,
                key=f"conversation_{lead['id']}"
            ):
                add_conversation_dialog(lead)


# ==========================================
# Appointment Details
# ==========================================

def render_appointment_details(appointment: dict):

    st.divider()
    st.subheader("📅 Appointment Details")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Appointment Information")

        st.write(f"**Appointment ID :** {appointment['id']}")
        st.write(f"**Lead ID :** {appointment['lead_id']}")
        st.write(f"**Meeting Type :** {appointment.get('meeting_type', '-')}")
        st.write(f"**Appointment Date :** {appointment.get('appointment_date', '-')}")

    with col2:

        st.markdown("### Status")

        status = appointment.get("status", "Unknown")

        if status == "Scheduled":
            st.info(status)
        elif status == "Completed":
            st.success(status)
        elif status == "Cancelled":
            st.error(status)
        elif status == "Missed":
            st.warning(status)
        else:
            st.write(status)

        st.write(f"**Created At :** {appointment.get('created_at', '-')}")

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("✏ Edit", use_container_width=True, key=f"edit_app_{appointment['id']}"):
            edit_appointment_dialog(appointment)

    with c2:
        if st.button("🗑 Delete", use_container_width=True, key=f"delete_app_{appointment['id']}"):
            delete_appointment_dialog(appointment)

    with c3:
        if st.button("✅ Complete", use_container_width=True, key=f"complete_app_{appointment['id']}"):
            edit_appointment_dialog({
                **appointment,
                "status": "Completed"
            })


# ==========================================
# Follow-up Details
# ==========================================

def render_followup_details(followup: dict):

    st.divider()
    st.subheader("📞 Follow-up Details")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("### Information")

        st.write(f"**ID :** {followup['id']}")
        st.write(f"**Lead ID :** {followup['lead_id']}")
        st.write(f"**Type :** {followup.get('follow_up_type', '-')}")
        st.write(f"**Scheduled :** {followup.get('scheduled_at', '-')}")

    with c2:

        status = followup.get("status", "Unknown")

        st.markdown("### Status")

        if status == "Pending":
            st.warning(status)
        elif status == "Completed":
            st.success(status)
        elif status == "Cancelled":
            st.error(status)
        else:
            st.write(status)

        st.write(f"**Created :** {followup.get('created_at', '-')}")

    st.divider()

    st.markdown("### Remarks")
    st.write(followup.get("remarks", "No Remarks"))

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✏ Edit", use_container_width=True, key=f"edit_followup_{followup['id']}"):
            edit_followup_dialog(followup)

    with col2:
        if st.button("🗑 Delete", use_container_width=True, key=f"delete_followup_{followup['id']}"):
            delete_followup_dialog(followup)


# ==========================================
# Conversation Details
# ==========================================

def render_conversation_details(conversation: dict):

    st.divider()
    st.subheader("💬 Conversation Details")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Information")

        st.write(f"**Conversation ID :** {conversation['id']}")
        st.write(f"**Lead ID :** {conversation['lead_id']}")
        st.write(f"**Sender :** {conversation.get('sender', '-')}")
        st.write(f"**Type :** {conversation.get('message_type', '-')}")

    with col2:

        st.markdown("### Timeline")

        st.write(f"**Created At :** {conversation.get('created_at', '-')}")

    st.divider()

    st.markdown("### Message")
    st.info(conversation.get("message", "No Message"))

    st.divider()

    c1, c2 = st.columns(2)

    with c1:
        if st.button("✏ Edit", use_container_width=True, key=f"edit_conv_{conversation['id']}"):
            edit_conversation_dialog(conversation)

    with c2:
        if st.button("🗑 Delete", use_container_width=True, key=f"delete_conv_{conversation['id']}"):
            delete_conversation_dialog(conversation)


