from utils.api import APIClient

def get_all_leads():

    response = APIClient.get_leads()
    if response.status_code == 200:
        return response.json()
    return []


def create_lead(data: dict):

    response = APIClient.create_lead(data)
    return response

def update_lead(
    lead_id: str,
    data: dict
):
    return APIClient.update_lead(
        lead_id,
        data
    )

def delete_lead(
    lead_id: str
):
    return APIClient.delete_lead(
        lead_id
    )