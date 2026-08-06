import streamlit as st
from services.lead_service import (
    create_lead,
    update_lead,
    delete_lead,
)



@st.dialog("➕ Add New Lead", width="large")
def add_lead_dialog():

    st.subheader("Customer Information")
    st.caption(
    "Fill the customer details below to create a new lead."
)

    col1, col2 = st.columns(2)

    with col1:

        full_name = st.text_input("Full Name *")

        email = st.text_input("Email *")

        phone = st.text_input("Phone *")

        city = st.text_input("City *")

    with col2:

        vehicle_interest = st.text_input(
            "Vehicle Interest *"
        )

        budget = st.number_input(
                "Budget *",
                min_value=100000,
                value=1000000,
                step=50000,
            )

        purchase_timeline = st.selectbox(
            "Purchase Timeline *",
            [
                "Within 7 Days",
                "Within 30 Days",
                "Within 3 Months",
                "More than 3 Months"
            ]
        )
        lead_source = st.selectbox(
            "Lead Source",
            [
                "Website",
                "Facebook",
                "Instagram",
                "Google Ads",
                "Walk-in",
                "Referral",
                "WhatsApp",
            ]
        )
    st.divider()

    notes = st.text_area(
        "Notes"
    )

    tags = st.text_input(
        "Tags (comma separated)"
    )

    # col1, col2 = st.columns(2)
    col1, col2 = st.columns([1, 1])
    

    with col1:

        cancel = st.button(
            "❌ Cancel",
            use_container_width=True
        )

    with col2:

        submit = st.button(
            "✅ Save Lead",
            use_container_width=True,
            type="primary"
        )

    if cancel:
        st.rerun()

    if submit:

        if (
            not full_name.strip()
            or not email.strip()
            or not phone.strip()
            or not city.strip()
            or not vehicle_interest.strip()
        ):

            st.error(
                "Please fill all required fields."
            )

            st.stop()

        if "@" not in email:

            st.error(
                "Please enter a valid email."
            )

            st.stop()

        if not phone.isdigit():

            st.error(
                "Phone number should contain only digits."
            )

            st.stop()

        if len(phone) != 10:

            st.error(
                "Phone number must be exactly 10 digits."
            )

            st.stop()

        data = {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "city": city,
            "vehicle_interest": vehicle_interest,
            "budget": budget,
            "purchase_timeline": purchase_timeline,
            "lead_source": lead_source,
            "notes": notes,
            "tags": tags
        }

        # response = create_lead(data)
        with st.spinner(
            "Creating Lead..."
        ):

            response = create_lead(data)

        if response.status_code == 201:

            st.toast(
                "✅ Lead Created Successfully",
                icon="🎉"
            )

            st.cache_data.clear()
            st.rerun()

        else:

            try:
                st.error(
                    response.json()["detail"]
                )
            except Exception:
                st.error("Something went wrong.")

@st.dialog("✏ Edit Lead", width="large")
def edit_lead_dialog(lead: dict):

    full_name = st.text_input(
        "Full Name",
        value=lead["full_name"]
    )

    city = st.text_input(
        "City",
        value=lead["city"]
    )

    vehicle = st.text_input(
        "Vehicle",
        value=lead["vehicle_interest"]
    )

    budget = st.number_input(
        "Budget",
        value=int(lead["budget"])
    )

    notes = st.text_area(
        "Notes",
        value=lead.get("notes") or ""
    )

    tags = st.text_input(
        "Tags",
        value=lead.get("tags") or ""
    )

    if st.button(
        "💾 Update Lead",
        type="primary",
        use_container_width=True
    ):

        response = update_lead(
            lead["id"],
            {
                "full_name": full_name,
                "city": city,
                "vehicle_interest": vehicle,
                "budget": budget,
                "notes": notes,
                "tags": tags,
            }
        )

        if response.status_code == 200:

            st.toast("Lead Updated")

            st.cache_data.clear()

            st.rerun()

        else:

            st.error(response.text)

@st.dialog("🗑 Delete Lead")
def delete_lead_dialog(lead: dict):

    st.warning(
        f"Delete **{lead['full_name']}** ?"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "Cancel",
            use_container_width=True
        ):

            st.rerun()

    with c2:

        if st.button(
            "Delete",
            type="primary",
            use_container_width=True
        ):

            response = delete_lead(
                lead["id"]
            )

            if response.status_code == 200:

                st.toast("Lead Deleted")

                st.cache_data.clear()

                st.rerun()

            else:

                st.error(response.text)


# ==========================================
# Appointment Dialogs
# ==========================================

from datetime import datetime

from services.appointment_service import (
    create_appointment,
    update_appointment,
    delete_appointment,
)


@st.dialog("📅 Schedule Appointment", width="large")
def add_appointment_dialog():

    st.subheader("Schedule Appointment")

    lead_id = st.text_input(
        "Lead ID *"
    )

    col1, col2 = st.columns(2)

    with col1:

        appointment_date = st.date_input(
            "Appointment Date"
        )

    with col2:

        appointment_time = st.time_input(
            "Appointment Time"
        )

    meeting_type = st.selectbox(
        "Meeting Type",
        [
            "Test Drive",
            "Showroom Visit",
            "Phone Call",
            "Video Call",
        ]
    )

    c1, c2 = st.columns(2)

    with c1:

        cancel = st.button(
            "❌ Cancel",
            use_container_width=True,
            key="cancel_appointment"
        )

    with c2:

        submit = st.button(
            "✅ Schedule",
            type="primary",
            use_container_width=True,
            key="save_appointment"
        )

    if cancel:

        st.rerun()

    if submit:

        if not lead_id.strip():

            st.error("Lead ID is required.")

            st.stop()

        appointment_datetime = datetime.combine(
            appointment_date,
            appointment_time
        )

        response = create_appointment(
            {
                "lead_id": lead_id,
                "appointment_date": appointment_datetime.isoformat(),
                "meeting_type": meeting_type,
            }
        )

        if response.status_code == 201:

            st.toast(
                "Appointment Scheduled",
                icon="🎉"
            )

            st.rerun()

        else:

            try:

                st.error(
                    response.json()["detail"]
                )

            except Exception:

                st.error(response.text)


@st.dialog("✏ Edit Appointment")
def edit_appointment_dialog(
    appointment: dict
):

    meeting_type = st.selectbox(
        "Meeting Type",
        [
            "Test Drive",
            "Showroom Visit",
            "Phone Call",
            "Video Call",
        ],
        index=[
            "Test Drive",
            "Showroom Visit",
            "Phone Call",
            "Video Call",
        ].index(
            appointment["meeting_type"]
        )
    )

    status = st.selectbox(
        "Status",
        [
            "Scheduled",
            "Completed",
            "Cancelled",
            "Missed",
        ],
        index=[
            "Scheduled",
            "Completed",
            "Cancelled",
            "Missed",
        ].index(
            appointment["status"]
        )
    )

    if st.button(
        "💾 Update Appointment",
        type="primary",
        use_container_width=True,
    ):

        response = update_appointment(
            appointment["id"],
            {
                "meeting_type": meeting_type,
                "status": status,
            }
        )

        if response.status_code == 200:

            st.toast(
                "Appointment Updated",
                icon="✅"
            )

            st.rerun()

        else:

            st.error(response.text)


@st.dialog("🗑 Delete Appointment")
def delete_appointment_dialog(
    appointment: dict
):

    st.warning(
        f"Delete Appointment ?"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "Cancel",
            use_container_width=True,
            key="cancel_delete_appointment"
        ):

            st.rerun()

    with c2:

        if st.button(
            "Delete",
            type="primary",
            use_container_width=True,
            key="delete_appointment"
        ):

            response = delete_appointment(
                appointment["id"]
            )

            if response.status_code == 200:

                st.toast(
                    "Appointment Deleted",
                    icon="🗑"
                )

                st.rerun()

            else:

                st.error(
                    response.text
                )

# ==========================================
# Follow-up Dialogs
# ==========================================

from datetime import datetime

from services.followup_service import (
    create_followup,
    update_followup,
    delete_followup,
)


@st.dialog("📞 Schedule Follow-up", width="large")
def add_followup_dialog():

    st.subheader("Schedule Follow-up")

    lead_id = st.text_input(
        "Lead ID *"
    )

    col1, col2 = st.columns(2)

    with col1:

        followup_type = st.selectbox(
            "Follow-up Type",
            [
                "Phone Call",
                "Email",
                "WhatsApp",
                "SMS",
                "Meeting",
            ],
        )

    with col2:

        scheduled_date = st.date_input(
            "Schedule Date"
        )

    scheduled_time = st.time_input(
        "Schedule Time"
    )

    remarks = st.text_area(
        "Remarks"
    )

    c1, c2 = st.columns(2)

    with c1:

        cancel = st.button(
            "❌ Cancel",
            key="cancel_followup",
            use_container_width=True,
        )

    with c2:

        submit = st.button(
            "✅ Schedule",
            key="save_followup",
            type="primary",
            use_container_width=True,
        )

    if cancel:

        st.rerun()

    if submit:

        if not lead_id.strip():

            st.error(
                "Lead ID is required."
            )

            st.stop()

        schedule = datetime.combine(
            scheduled_date,
            scheduled_time,
        )

        response = create_followup(
            {
                "lead_id": lead_id,
                "follow_up_type": followup_type,
                "scheduled_at": schedule.isoformat(),
                "remarks": remarks,
            }
        )

        if response.status_code == 201:

            st.toast(
                "Follow-up Scheduled",
                icon="🎉",
            )

            st.rerun()

        else:

            try:

                st.error(
                    response.json()["detail"]
                )

            except Exception:

                st.error(response.text)


@st.dialog("✏ Edit Follow-up")
def edit_followup_dialog(
    followup: dict
):

    status = st.selectbox(
        "Status",
        [
            "Pending",
            "Completed",
            "Cancelled",
        ],
        index=[
            "Pending",
            "Completed",
            "Cancelled",
        ].index(
            followup["status"]
        ),
    )

    remarks = st.text_area(
        "Remarks",
        value=followup.get("remarks") or "",
    )

    if st.button(
        "💾 Update",
        type="primary",
        use_container_width=True,
    ):

        response = update_followup(
            followup["id"],
            {
                "status": status,
                "remarks": remarks,
            },
        )

        if response.status_code == 200:

            st.toast(
                "Follow-up Updated",
                icon="✅",
            )

            st.rerun()

        else:

            st.error(
                response.text
            )


@st.dialog("🗑 Delete Follow-up")
def delete_followup_dialog(
    followup: dict
):

    st.warning(
        "Delete this follow-up?"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "Cancel",
            key="cancel_delete_followup",
            use_container_width=True,
        ):

            st.rerun()

    with c2:

        if st.button(
            "Delete",
            key="delete_followup",
            type="primary",
            use_container_width=True,
        ):

            response = delete_followup(
                followup["id"]
            )

            if response.status_code == 200:

                st.toast(
                    "Follow-up Deleted",
                    icon="🗑"
                )

                st.rerun()

            else:

                st.error(
                    response.text
                )

# ==========================================
# Conversation Dialogs
# ==========================================

from services.conversation_service import (
    create_conversation,
    update_conversation,
    delete_conversation,
)


@st.dialog("💬 Add Conversation", width="large")
def add_conversation_dialog():

    st.subheader("New Conversation")

    lead_id = st.text_input(
        "Lead ID *"
    )

    sender = st.selectbox(
        "Sender",
        [
            "Customer",
            "Sales Executive",
            "AI Agent",
        ]
    )

    message_type = st.selectbox(
        "Message Type",
        [
            "Call",
            "WhatsApp",
            "Email",
            "SMS",
            "Note",
        ]
    )

    message = st.text_area(
        "Message"
    )

    c1, c2 = st.columns(2)

    with c1:

        cancel = st.button(
            "❌ Cancel",
            key="cancel_conversation",
            use_container_width=True
        )

    with c2:

        submit = st.button(
            "✅ Save",
            key="save_conversation",
            type="primary",
            use_container_width=True
        )

    if cancel:

        st.rerun()

    if submit:

        if not lead_id.strip():

            st.error(
                "Lead ID required."
            )

            st.stop()

        if not message.strip():

            st.error(
                "Message required."
            )

            st.stop()

        response = create_conversation(
            {
                "lead_id": lead_id,
                "sender": sender,
                "message": message,
                "message_type": message_type,
            }
        )

        if response.status_code == 201:

            st.toast(
                "Conversation Added",
                icon="🎉"
            )

            st.rerun()

        else:

            try:

                st.error(
                    response.json()["detail"]
                )

            except Exception:

                st.error(
                    response.text
                )


@st.dialog("✏ Edit Conversation")
def edit_conversation_dialog(
    conversation: dict
):

    sender_options = [
        "Customer",
        "Sales Executive",
        "AI",
    ]

    current_sender = conversation.get(
        "sender",
        "Customer"
    )

    sender = st.selectbox(
        "Sender",
        sender_options,
        index=(
            sender_options.index(current_sender)
            if current_sender in sender_options
            else 0
        )
    )

    message_options = [
        "Call",
        "WhatsApp",
        "Email",
        "SMS",
        "Note",
    ]

    current_type = conversation.get(
        "message_type",
        "Note"
    )

    message_type = st.selectbox(
        "Message Type",
        message_options,
        index=(
            message_options.index(current_type)
            if current_type in message_options
            else 0
        )
    )

    message = st.text_area(
        "Message",
        value=conversation["message"]
    )

    if st.button(
        "💾 Update",
        use_container_width=True,
        type="primary"
    ):

        response = update_conversation(
            conversation["id"],
            {
                "sender": sender,
                "message": message,
                "message_type": message_type,
            }
        )

        if response.status_code == 200:

            st.toast(
                "Conversation Updated",
                icon="✅"
            )

            st.rerun()

        else:

            st.error(
                response.text
            )


@st.dialog("🗑 Delete Conversation")
def delete_conversation_dialog(
    conversation: dict
):

    st.warning(
        "Delete this conversation?"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "Cancel",
            key="cancel_delete_conversation",
            use_container_width=True
        ):

            st.rerun()

    with c2:

        if st.button(
            "Delete",
            key="delete_conversation",
            type="primary",
            use_container_width=True
        ):

            response = delete_conversation(
                conversation["id"]
            )

            if response.status_code == 200:

                st.toast(
                    "Conversation Deleted",
                    icon="🗑"
                )

                st.rerun()

            else:

                st.error(
                    response.text
                )