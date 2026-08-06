from utils.api import APIClient

# ==========================================
# Get All Appointments
# ==========================================

def get_all_appointments():

    response = APIClient.get_appointments()
    if response.status_code == 200:
        return response.json()
    return []

# ==========================================
# Get Appointment
# ==========================================

def get_appointment(
    appointment_id: str
):
    return APIClient.get_appointment(
        appointment_id
    )

# ==========================================
# Create Appointment
# ==========================================

def create_appointment(
    data: dict
):

    return APIClient.create_appointment(
        data
    )

# ==========================================
# Update Appointment
# ==========================================

def update_appointment(
    appointment_id: str,
    data: dict
):

    return APIClient.update_appointment(
        appointment_id,
        data
    )

# ==========================================
# Delete Appointment
# ==========================================

def delete_appointment(
    appointment_id: str
):

    return APIClient.delete_appointment(
        appointment_id
    )