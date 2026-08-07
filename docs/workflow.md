# AI CRM Automation Workflow

## Overview

The AI CRM Automation System follows a structured workflow that combines Artificial Intelligence, CRM management, and Google Sheets synchronization to streamline lead processing.

The workflow begins when a new lead is created and ends after the lead is stored, analyzed, synchronized, and made available for further CRM activities.

---

# Lead Processing Workflow

```text
Customer Creates Lead
          │
          ▼
Duplicate Validation
          │
          ▼
Google Gemini AI Analysis
          │
          ▼
Lead Score Generated
          │
          ▼
Qualification Status
          │
          ▼
Pipeline Stage
          │
          ▼
Priority Assignment
          │
          ▼
Recommended Action
          │
          ▼
Follow-up Time Suggestion
          │
          ▼
Lead Saved to PostgreSQL
          │
          ▼
Google Sheets Synchronization
          │
          ▼
Activity Logged
          │
          ▼
Response Returned
```

---

# CRM Workflow

```text
New Lead
     │
     ▼
Qualified
     │
     ▼
Sales Contact
     │
     ▼
Appointment Scheduled
     │
     ▼
Conversation Recorded
     │
     ▼
Follow-up Added
     │
     ▼
Negotiation
     │
     ▼
Won

────────────── OR ──────────────

Qualified
     │
     ▼
Sales Contact
     │
     ▼
Lost
```

---

# AI Qualification Workflow

```text
Lead Information
       │
       ▼
Google Gemini AI
       │
       ▼
Customer Intent Analysis
       │
       ▼
Lead Score
Qualification
Priority
Pipeline Stage
Recommended Action
Follow-up Time
AI Reason
```

---

# Google Sheets Workflow

```text
Lead Saved
     │
     ▼
Google Sheets Service
     │
     ▼
Spreadsheet Authentication
     │
     ▼
Worksheet Opened
     │
     ▼
Lead Appended
     │
     ▼
Synchronization Complete
```

---

# Dashboard Workflow

```text
Frontend Request
        │
        ▼
FastAPI API
        │
        ▼
PostgreSQL
        │
        ▼
Return CRM Data
        │
        ▼
Dashboard Updated
```

---

# Authentication Workflow

```text
User Login
     │
     ▼
Credential Validation
     │
     ▼
JWT Token Generated
     │
     ▼
Authenticated API Requests
     │
     ▼
Protected CRM Resources
```

---

# Current Automation

The current version automatically performs:

- Duplicate Lead Validation
- AI Lead Qualification
- AI Lead Scoring
- AI Priority Assignment
- AI Pipeline Prediction
- AI Recommended Action
- AI Follow-up Time Suggestion
- Google Sheets Synchronization
- Activity Logging

---

# Manual CRM Operations

The following operations are currently managed manually:

- Appointment Scheduling
- Follow-up Management
- Conversation Management
- Pipeline Progression
- Customer Negotiation
- Sales Conversion