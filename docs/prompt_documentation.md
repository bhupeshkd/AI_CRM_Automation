# Prompt Documentation

## Objective

The AI Qualification module analyzes incoming leads and recommends the next sales action.

---

# Input Parameters

The prompt receives:

- Budget
- Purchase Timeline
- Vehicle Interest
- City

---

# AI Responsibilities

The AI determines:

- Lead Score
- Qualification Status
- Pipeline Stage
- Priority
- Recommended Action
- Follow-up Time
- Reasoning

---

# Expected Output

```json
{
    "lead_score":95,
    "qualification_status":"Hot",
    "pipeline_stage":"Qualified",
    "priority":"High",
    "recommended_action":"Call immediately and schedule test drive.",
    "follow_up_in_hours":1,
    "reason":"Customer has immediate buying intent."
}
```

---

# Prompt Goals

The prompt should:

- Evaluate customer buying intent
- Identify urgency
- Recommend sales actions
- Reduce manual qualification effort

---

# Future Improvements

Future prompt versions may include:

- Conversation History
- Previous Activities
- Dealership Inventory
- Finance Eligibility
- Customer Sentiment
- RAG-based Context