from utils.api import APIClient

# ==========================================
# Get All Conversations
# ==========================================

def get_all_conversations():

    response = APIClient.get_conversations()
    if response.status_code == 200:
        return response.json()

    return []

# ==========================================
# Get By Lead
# ==========================================

def get_conversations_by_lead(
    lead_id: str
):
    return APIClient.get_conversations_by_lead(
        lead_id
    )

# ==========================================
# Create
# ==========================================

def create_conversation(
    data: dict
):
    return APIClient.create_conversation(
        data
    )

# ==========================================
# Update
# ==========================================

def update_conversation(
    conversation_id: str,
    data: dict
):
    return APIClient.update_conversation(
        conversation_id,
        data
    )

# ==========================================
# Delete
# ==========================================

def delete_conversation(
    conversation_id: str
):

    return APIClient.delete_conversation(
        conversation_id
    )