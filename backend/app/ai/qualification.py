import json

from google import genai

from app.core.config import settings


client = genai.Client(api_key=settings.GEMINI_API_KEY)


class LeadQualification:

    @staticmethod
    def qualify(data: dict):

        prompt = f"""
        You are an AI Lead Qualification Assistant for an Automobile CRM.

        Your responsibility is to analyze a customer's buying intent and generate structured CRM insights for the sales team.

        Lead Details:
        {json.dumps(data, indent=2)}

        Evaluate the lead using the following factors:

        1. Budget
        2. Purchase Timeline
        3. Vehicle Interest
        4. Customer Location

        Scoring Guidelines

        - Lead Score: Integer between 0 and 100.
        - Qualification Status:
            - Hot  : Customer is highly likely to purchase soon.
            - Warm : Customer is interested but requires nurturing.
            - Cold : Customer currently has low purchase intent.

        Pipeline Stage

        - Hot  -> Qualified
        - Warm -> Follow Up
        - Cold -> Nurturing

        Priority

        - Hot  -> High
        - Warm -> Medium
        - Cold -> Low

        Recommended Action

        Provide one short and actionable recommendation for the sales team.

        Follow-up Time

        Return the recommended follow-up time in hours.

        Examples:

        - Hot  -> 2 to 6 hours
        - Warm -> 24 to 48 hours
        - Cold -> 72 hours or more

        Reason

        Briefly explain why the lead received this qualification.

        CRM Tags

        Generate 2 to 5 short CRM tags.

        Examples:
        - SUV
        - Sedan
        - High Budget
        - Budget Buyer
        - Immediate Buyer
        - Family Car
        - Luxury Buyer
        - First Time Buyer

        CRM Notes

        Generate a concise CRM note (2–4 sentences) summarizing:

        - Customer intent
        - Buying timeline
        - Budget confidence
        - Recommended next action

        Return ONLY valid JSON using the following format.

        {{
            "lead_score": 90,
            "qualification_status": "Hot",
            "pipeline_stage": "Qualified",
            "priority": "High",
            "recommended_action": "Book a test drive within 24 hours.",
            "follow_up_in_hours": 2,
            "reason": "Customer has sufficient budget and immediate purchase intent.",
            "tags": [
                "SUV",
                "High Budget",
                "Immediate Buyer"
            ],
            "notes": "Customer is interested in purchasing an SUV within this month. Budget is sufficient and buying intent is high. Sales team should prioritize immediate follow-up and schedule a test drive."
        }}

        Rules

        - Return ONLY valid JSON.
        - Do not return markdown.
        - Do not use code blocks.
        - Do not include explanations outside JSON.
        - Do not add extra fields.
        - If any information is missing, make the best possible assessment using the available information.
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