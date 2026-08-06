import json

from google import genai

from app.core.config import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


class AICommunication:

    @staticmethod
    def generate(data: dict):

        prompt = f"""
        You are an AI Sales Communication Assistant for an Automobile CRM.

        Your responsibility is to generate personalized customer communication
        based on the customer's profile.

        Customer Details:

        {json.dumps(data, indent=2)}

        Generate the following:

        1. Professional Email Subject

        2. Professional Email Body

        Rules:

        - Keep it professional.
        - Maximum 120 words.
        - Personalize using the customer's name.
        - Mention the interested vehicle.
        - Encourage the customer to schedule a test drive.
        - Mention dealership assistance.
        - End with a professional closing.

        3. Professional WhatsApp Message

        Rules:

        - Friendly tone.
        - Maximum 60 words.
        - Personalize using customer's first name.
        - Mention vehicle interest.
        - Encourage quick response.
        - Use at most one emoji.

        Return ONLY valid JSON.

        Example:

        {{
            "email_subject": "Exclusive Test Drive Invitation for Mahindra Scorpio N",

            "email_body": "Dear Rahul Sharma,\n\nThank you for showing interest in the Mahindra Scorpio N. We would be delighted to arrange a complimentary test drive at your convenience. Our sales team is available to assist you with pricing, finance options, and exchange offers.\n\nPlease let us know your preferred date and time.\n\nRegards,\nMahindra Sales Team",

            "whatsapp_message": "Hi Rahul 👋 Thanks for your interest in the Mahindra Scorpio N. We'd love to arrange your free test drive. Reply to this message and our sales advisor will assist you."
        }}

        Rules:

        - Return ONLY valid JSON.
        - No markdown.
        - No code block.
        - No explanation.
        - Do not add extra fields.
        """

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = (
                text.replace("```json", "")
                .replace("```", "")
                .strip()
            )

        return json.loads(text)