# AI Prompt Documentation

## Overview

The AI CRM Automation System uses **Google Gemini AI** to intelligently analyze every newly created lead and generate actionable sales insights.

The objective is to reduce manual lead qualification and help sales teams prioritize high-value customers.

---

# Objective

The AI model evaluates customer information and automatically generates:

- Lead Score
- Qualification Status
- Pipeline Stage
- Priority
- Recommended Action
- Follow-up Time
- AI Reason

These insights are stored in the CRM and displayed on the dashboard.

---

# Input Parameters

The prompt receives the following customer information:

- Full Name
- City
- Vehicle Interest
- Budget
- Purchase Timeline
- Lead Source
- Customer Notes

---

# AI Responsibilities

The AI analyzes the customer's buying intent and determines:

- Lead Score (0–100)
- Qualification Status
- Pipeline Stage
- Priority Level
- Recommended Sales Action
- Follow-up Time (Hours)
- Reasoning behind the recommendation

---

# Sample Output

```json
{
    "lead_score": 95,
    "qualification_status": "Highly Qualified",
    "pipeline_stage": "Qualified",
    "priority": "High",
    "recommended_action": "Contact the customer immediately and schedule a test drive.",
    "follow_up_in_hours": 1,
    "ai_reason": "The customer has a high budget, immediate purchase timeline, and strong buying intent."
}
```

---

# Prompt Goals

The prompt is designed to:

- Evaluate customer purchase intent
- Identify high-priority leads
- Estimate conversion potential
- Recommend the next sales action
- Suggest an appropriate follow-up timeline
- Reduce manual lead qualification effort
- Improve sales team productivity

---

# AI Workflow

```text
Customer Creates Lead
          │
          ▼
Lead Data Sent to Gemini AI
          │
          ▼
Lead Analysis
          │
          ▼
Lead Score Generated
          │
          ▼
Qualification Status Assigned
          │
          ▼
Priority Determined
          │
          ▼
Pipeline Stage Selected
          │
          ▼
Recommended Action Generated
          │
          ▼
Follow-up Time Suggested
          │
          ▼
AI Reason Generated
          │
          ▼
Response Returned to CRM
```

---

# Current Limitations

The AI currently evaluates only the information provided during lead creation.

It does not consider:

- Previous Conversations
- Appointment History
- Follow-up History
- Customer Purchase History
- Dealership Inventory
- Finance Eligibility
- Market Trends

---

# Future Enhancements

Future versions may enhance the prompt using:

- Conversation History
- Customer Interaction History
- Appointment History
- Previous Follow-ups
- Finance Eligibility
- Inventory Availability
- Customer Sentiment Analysis
- RAG-based Knowledge Retrieval
- Predictive Sales Analytics
- Multi-turn AI Reasoning