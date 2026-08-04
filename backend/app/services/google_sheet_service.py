import gspread
from google.oauth2.service_account import Credentials

from app.core.config import settings
from app.models.lead import Lead


class GoogleSheetService:

    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    @classmethod
    def get_worksheet(cls):
        print("\n========== GOOGLE SHEET ==========")

        print("Loading Service Account...")
        credentials = Credentials.from_service_account_file(
            settings.GOOGLE_CREDENTIALS,
            scopes=cls.SCOPES,
        )
        print("✅ Credentials Loaded")

        print("Authorizing...")
        client = gspread.authorize(credentials)
        print("✅ Authorization Successful")

        print(f"Opening Spreadsheet : {settings.GOOGLE_SHEET_NAME}")
        spreadsheet = client.open(settings.GOOGLE_SHEET_NAME)
        print("✅ Spreadsheet Opened")

        print(f"Opening Worksheet : {settings.GOOGLE_WORKSHEET_NAME}")
        worksheet = spreadsheet.worksheet(settings.GOOGLE_WORKSHEET_NAME)
        print("✅ Worksheet Opened")

        print("==================================\n")

        return worksheet

    @classmethod
    def append_lead(cls, lead: Lead):

        print("\n========== SHEET SYNC START ==========")

        try:
            worksheet = cls.get_worksheet()

            row = [
                str(lead.id),
                lead.full_name,
                lead.email,
                lead.phone,
                lead.city,
                lead.vehicle_interest,
                lead.budget,
                lead.purchase_timeline,
                lead.lead_source,
                lead.lead_score,
                lead.qualification_status,
                lead.pipeline_stage,
                lead.priority,
                lead.recommended_action,
                lead.follow_up_in_hours,
                lead.ai_reason,
                str(lead.created_at),
            ]

            print("Appending Row...")
            print(row)

            worksheet.append_row(row)

            print("✅ Lead Synced Successfully")
            print("========== SHEET SYNC END ==========\n")

        except Exception as e:
            print("\n❌ GOOGLE SHEET ERROR")
            print(type(e).__name__)
            print(e)
            print("====================================\n")
            raise