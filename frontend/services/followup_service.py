from utils.api import APIClient

# ==========================================
# Get All Follow-ups
# ==========================================

def get_all_followups():

    response = APIClient.get_followups()
    if response.status_code == 200:
        return response.json()

    return []

# ==========================================
# Get Follow-ups By Lead
# ==========================================

def get_followups_by_lead(
    lead_id: str
):
    return APIClient.get_followups_by_lead(
        lead_id
    )

# ==========================================
# Create Follow-up
# ==========================================

def create_followup(
    data: dict
):

    return APIClient.create_followup(
        data
    )

# ==========================================
# Update Follow-up
# ==========================================

def update_followup(
    followup_id: str,
    data: dict
):
    return APIClient.update_followup(
        followup_id,
        data
    )

# ==========================================
# Delete Follow-up
# ==========================================

def delete_followup(
    followup_id: str
):
    return APIClient.delete_followup(
        followup_id
    )