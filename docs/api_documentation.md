# API Documentation

## Overview

The AI CRM Automation System exposes REST APIs for managing leads, appointments, conversations, and follow-up automation.

Base URL

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

---

# Lead APIs

## Create Lead

POST /leads/

Creates a new lead, performs AI qualification, syncs data with Google Sheets, creates follow-up tasks, and logs activities.

### Request

```json
{
  "full_name": "Rohit Verma",
  "email": "rohit@gmail.com",
  "phone": "9876543210",
  "city": "Raipur",
  "vehicle_interest": "Mahindra Scorpio N",
  "budget": 2200000,
  "purchase_timeline": "Immediate",
  "lead_source": "Website",
  "notes": "Interested in top model.",
  "tags": "VIP,Hot"
}
```

### Response

Returns the complete lead object including:

- Lead Score
- Qualification
- Pipeline
- Priority
- AI Recommendation
- Follow-up Time

---

## Get All Leads

GET /leads/

Returns every lead stored inside the CRM.

---

## Get Lead By ID

GET /leads/{lead_id}

Returns complete information about a single lead.

---

# Appointment APIs

## Create Appointment

POST /appointments/

Creates a test drive appointment.

Validation:

- Lead must exist
- Appointment slot must not already be booked

---

## Get Appointments

GET /appointments/

Returns all appointments.

---

## Get Appointment

GET /appointments/{appointment_id}

Returns appointment details.

---

## Update Appointment

PATCH /appointments/{appointment_id}

Updates appointment status.

Example:

- Scheduled
- Completed
- Missed
- Cancelled

Missed appointments automatically trigger re-engagement workflow.

---

# Follow-up APIs

## Create Follow-up

POST /follow-ups/

Creates a follow-up task.

---

## Get Follow-ups

GET /follow-ups/

Returns all scheduled follow-ups.

---

# Conversation APIs

## Create Conversation

POST /conversations/

Stores AI or customer conversation.

---

## Get Conversations

GET /conversations/{lead_id}

Returns complete conversation history for a lead.

---

# Activity APIs

Activity records are automatically generated whenever:

- Lead Created
- Appointment Scheduled
- Appointment Updated
- Follow-up Scheduled
- Conversation Added

These APIs help maintain CRM audit history.

---

# Response Codes

| Code | Meaning |
|------|----------|
|200|Success|
|201|Resource Created|
|400|Bad Request|
|404|Not Found|
|500|Internal Server Error|

---

# API Workflow

Lead Creation

↓

AI Qualification

↓

Google Sheet Sync

↓

Automation Engine

↓

Follow-up Creation

↓

Activity Logging

↓

Response Returned
