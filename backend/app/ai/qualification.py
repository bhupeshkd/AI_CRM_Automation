import json

from google import genai

from app.core.config import settings


client = genai.Client(api_key=settings.GEMINI_API_KEY)


class LeadQualification:

    @staticmethod
    def qualify(data: dict):

        prompt = f"""
            You are an AI Lead Qualification Assistant for an Automobile CRM.

            Your task is to analyze a customer's interest in purchasing a vehicle and return a structured lead qualification.

            Lead Details:
            {json.dumps(data, indent=2)}

            Evaluate the lead using the following criteria:

            1. Budget
            2. Purchase Timeline
            3. Vehicle Interest
            4. Customer Location

            Scoring Guidelines:

            - Lead Score: Integer between 0 and 100.
            - Qualification Status:
                - Hot  : Customer is highly likely to purchase soon.
                - Warm : Customer shows interest but needs follow-up.
                - Cold : Customer has low purchase intent.

            Recommended Action:
            Provide one short and actionable recommendation for the sales team.

            Follow-up Time:
            Return the recommended follow-up time in hours.
            Examples:
            - Hot  -> 2-6 hours
            - Warm -> 24-48 hours
            - Cold -> 72+ hours

            Reason:
            Briefly explain why the lead received this qualification.

            Return ONLY valid JSON in the following format:

            {{
                "lead_score": 90,
                "qualification_status": "Hot",
                "pipeline_stage": "Qualified",
                "priority": "High",
                "recommended_action": "Book a test drive within 24 hours.",
                "follow_up_in_hours": 2,
                "reason": "Customer has sufficient budget, immediate purchase timeline, and high buying intent."
            }}

            Rules:
            - Return only valid JSON.
            - Do not return markdown.
            - Do not include explanations outside JSON.
            - Do not use code blocks.
            - Do not add extra fields.
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