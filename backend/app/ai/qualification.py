import json

from google import genai

from app.core.config import settings


client = genai.Client(api_key=settings.GEMINI_API_KEY)


class LeadQualification:

    @staticmethod
    def qualify(data: dict):

        prompt = f"""
You are an expert Automobile CRM AI.

Analyze the following lead.

Lead Details:
{json.dumps(data, indent=2)}

Return ONLY valid JSON.

{{
    "lead_score": 90,
    "qualification_status": "Hot",
    "pipeline_stage": "Qualified",
    "priority": "High",
    "recommended_action": "Book a test drive within 24 hours.",
    "follow_up_in_hours": 2,
    "reason": "Customer has high budget and immediate buying intent."
}}

Do not return markdown.
Do not use ```json.
Return only JSON.
"""

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        # Remove markdown if Gemini returns it
        if text.startswith("```"):
            text = (
                text.replace("```json", "")
                .replace("```", "")
                .strip()
            )

        return json.loads(text)