import requests

from utils.auth import AuthManager
from utils.config import Config


class APIClient:

    # ==========================================
    # Authentication
    # ==========================================

    @staticmethod
    def login(
        email: str,
        password: str
    ):

        return requests.post(
            f"{Config.API_URL}/auth/login",
            json={
                "email": email,
                "password": password
            },
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def get_headers():

        token = AuthManager.get_token()

        if not token:
            return {
                "Accept": "application/json"
        }

        return {
            "Authorization": f"Bearer {token}"
        }

    # ==========================================
    # Leads
    # ==========================================

    @staticmethod
    def get_leads():

        return requests.get(
            f"{Config.API_URL}/leads",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def get_lead(
        lead_id: str
    ):

        return requests.get(
            f"{Config.API_URL}/leads/{lead_id}",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def create_lead(
        data: dict
    ):

        return requests.post(
            f"{Config.API_URL}/leads",
            json=data,
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def update_lead(
        lead_id: str,
        data: dict
    ):

        return requests.patch(
            f"{Config.API_URL}/leads/{lead_id}",
            json=data,
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def delete_lead(
        lead_id: str
    ):

        return requests.delete(
            f"{Config.API_URL}/leads/{lead_id}",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    # ==========================================
    # Appointments
    # ==========================================

    @staticmethod
    def get_appointments():

        return requests.get(
            f"{Config.API_URL}/appointments",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )
    
    @staticmethod
    def get_appointment(
        appointment_id: str
    ):

        return requests.get(
            f"{Config.API_URL}/appointments/{appointment_id}",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def create_appointment(
        data: dict
    ):

        return requests.post(
            f"{Config.API_URL}/appointments",
            json=data,
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def update_appointment(
        appointment_id: str,
        data: dict
    ):

        return requests.patch(
            f"{Config.API_URL}/appointments/{appointment_id}",
            json=data,
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def delete_appointment(
        appointment_id: str
    ):

        return requests.delete(
            f"{Config.API_URL}/appointments/{appointment_id}",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    # ==========================================
    # Follow Ups
    # ==========================================

    @staticmethod
    def get_followups():

        return requests.get(
            f"{Config.API_URL}/follow-ups",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def get_followups_by_lead(
        lead_id: str
    ):

        return requests.get(
            f"{Config.API_URL}/follow-ups/lead/{lead_id}",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def create_followup(
        data: dict
    ):

        return requests.post(
            f"{Config.API_URL}/follow-ups",
            json=data,
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def update_followup(
        followup_id: str,
        data: dict
    ):

        return requests.patch(
            f"{Config.API_URL}/follow-ups/{followup_id}",
            json=data,
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def delete_followup(
        followup_id: str
    ):

        return requests.delete(
            f"{Config.API_URL}/follow-ups/{followup_id}",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    # ==========================================
    # Conversations
    # ==========================================

    @staticmethod
    def get_conversations():

        return requests.get(
            f"{Config.API_URL}/conversations",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )

    @staticmethod
    def get_conversations_by_lead(
        lead_id: str
    ):

        return requests.get(
            f"{Config.API_URL}/conversations/lead/{lead_id}",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )


    @staticmethod
    def create_conversation(
        data: dict
    ):

        return requests.post(
            f"{Config.API_URL}/conversations",
            json=data,
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )


    @staticmethod
    def update_conversation(
        conversation_id: str,
        data: dict
    ):

        return requests.patch(
            f"{Config.API_URL}/conversations/{conversation_id}",
            json=data,
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )


    @staticmethod
    def delete_conversation(
        conversation_id: str
    ):

        return requests.delete(
            f"{Config.API_URL}/conversations/{conversation_id}",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )
    @staticmethod
    def get_current_user():

        return requests.get(
            f"{Config.API_URL}/auth/me",
            headers=APIClient.get_headers(),
            timeout=Config.REQUEST_TIMEOUT
        )