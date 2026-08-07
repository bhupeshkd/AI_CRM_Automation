from utils.api import APIClient


def get_all_activities():

    response = APIClient.get_activities()

    if response.status_code == 200:
        return response.json()

    return []