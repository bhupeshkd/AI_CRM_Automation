# API Documentation

## Overview

The AI CRM Automation System exposes RESTful APIs for managing customer leads, appointments, follow-ups, conversations, and user authentication.

The backend is built using **FastAPI** and follows a modular architecture with JWT-based authentication and AI-powered lead qualification.

---

# Base URLs

## Local Development

```text
http://localhost:8000
```

## Production

```text
https://ai-crm-backend-ibos.onrender.com
```

## Interactive API Documentation

### Swagger UI

```text
https://ai-crm-backend-ibos.onrender.com/docs
```

### ReDoc

```text
https://ai-crm-backend-ibos.onrender.com/redoc
```

---

# Authentication APIs

## Register User

**POST** `/auth/register`

Creates a new CRM user.

> **Note:** Only an authenticated Admin can create new users.

---

## Login

**POST** `/auth/login`

Authenticates a user and returns a JWT access token.

### Request

```json
{
  "email": "admin@example.com",
  "password": "Password@123"
}
```

### Response

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

---

## Current User

**GET** `/auth/me`

Returns details of the currently authenticated user.

Requires:

```
Authorization: Bearer <JWT_TOKEN>
```

---

# Lead APIs

## Create Lead

**POST** `/leads/`

Creates a new lead and automatically performs:

- AI Lead Qualification
- Lead Scoring
- Priority Assignment
- Pipeline Stage Prediction
- Recommended Action Generation
- Google Sheets Synchronization
- Activity Logging

### Sample Request

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

---

## Get All Leads

**GET** `/leads/`

Returns all CRM leads.

---

## Get Lead

**GET** `/leads/{lead_id}`

Returns details of a specific lead.

---

## Update Lead

**PATCH** `/leads/{lead_id}`

Updates lead information.

---

## Delete Lead

**DELETE** `/leads/{lead_id}`

Deletes a lead from the CRM.

---

# Appointment APIs

## Create Appointment

**POST** `/appointments/`

Creates an appointment for an existing lead.

Validation includes:

- Lead existence
- Appointment availability

---

## Get All Appointments

**GET** `/appointments/`

Returns all appointments.

---

## Get Appointment

**GET** `/appointments/{appointment_id}`

Returns appointment details.

---

## Update Appointment

**PATCH** `/appointments/{appointment_id}`

Updates appointment information or status.

Supported statuses include:

- Scheduled
- Completed
- Cancelled
- Missed

---

## Delete Appointment

**DELETE** `/appointments/{appointment_id}`

Deletes an appointment.

---

# Follow-up APIs

## Create Follow-up

**POST** `/follow-ups/`

Creates a follow-up task.

---

## Get All Follow-ups

**GET** `/follow-ups/`

Returns all follow-up records.

---

## Get Follow-ups by Lead

**GET** `/follow-ups/lead/{lead_id}`

Returns follow-ups associated with a lead.

---

## Update Follow-up

**PATCH** `/follow-ups/{followup_id}`

Updates follow-up information.

---

## Delete Follow-up

**DELETE** `/follow-ups/{followup_id}`

Deletes a follow-up.

---

# Conversation APIs

## Create Conversation

**POST** `/conversations/`

Stores customer communication history.

Supported communication types include:

- Call
- Email
- WhatsApp
- SMS
- Notes

---

## Get All Conversations

**GET** `/conversations/`

Returns all conversation records.

---

## Get Conversations by Lead

**GET** `/conversations/lead/{lead_id}`

Returns conversation history for a specific lead.

---

## Update Conversation

**PATCH** `/conversations/{conversation_id}`

Updates conversation details.

---

## Delete Conversation

**DELETE** `/conversations/{conversation_id}`

Deletes a conversation.

---

# AI Workflow

Whenever a new lead is created, the following workflow executes automatically:

```text
Lead Created
      │
      ▼
Gemini AI Qualification
      │
      ▼
Lead Score Generated
      │
      ▼
Priority Assigned
      │
      ▼
Pipeline Stage Selected
      │
      ▼
Recommended Action Generated
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
API Response Returned
```

---

# Authentication

Protected endpoints require a JWT access token.

Example:

```
Authorization: Bearer <JWT_TOKEN>
```

---

# Response Status Codes

| Code | Description |
|------|-------------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# Technologies Used

- FastAPI
- SQLAlchemy
- PostgreSQL (Supabase)
- Google Gemini AI
- Google Sheets API
- JWT Authentication
- Pydantic
- Alembic

---

# API Highlights

- RESTful API Design
- JWT Authentication
- AI-Powered Lead Qualification
- Google Sheets Synchronization
- Production Deployment on Render
- PostgreSQL Database
- Modular Service Architecture