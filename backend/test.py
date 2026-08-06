# from google import genai
# from app.core.config import settings

# client = genai.Client(api_key=settings.GEMINI_API_KEY)

# response = client.models.generate_content(
#     model="gemini-3.5-flash",
#     contents="Reply with only the word Hello"
# )

# print(response.text)


from app.ai.communication import AICommunication

data = {
    "full_name": "Rahul Sharma",
    "vehicle_interest": "Mahindra Scorpio N",
    "budget": 1800000,
    "purchase_timeline": "Within 30 Days",
    "city": "Bilaspur",
    "qualification_status": "Hot",
    "priority": "High",
    "recommended_action": "Book a test drive within 24 hours."
}

result = AICommunication.generate(data)

print(result)