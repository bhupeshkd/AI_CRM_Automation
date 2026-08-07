# CRM Pipeline Design

## Overview

The AI CRM Automation System follows a structured sales pipeline that helps sales teams track customer progress from initial inquiry to final conversion.

Each lead moves through different stages based on customer interactions, appointments, and sales activities.

---

# Sales Pipeline

```text
New Lead
    │
    ▼
Qualified
    │
    ▼
Contacted
    │
    ▼
Appointment Scheduled
    │
    ▼
Test Drive Completed
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
Contacted
    │
    ▼
No Response
    │
    ▼
Lost
```

---

# Pipeline Stages

## 1. New Lead

A customer submits an enquiry through the CRM.

Information collected includes:

- Customer Details
- Vehicle Interest
- Budget
- Purchase Timeline
- Lead Source

---

## 2. Qualified

After a lead is created, **Google Gemini AI** automatically evaluates the customer and generates:

- Lead Score
- Qualification Status
- Pipeline Stage
- Priority
- Recommended Action
- Follow-up Time
- AI Reason

---

## 3. Contacted

A sales executive contacts the customer and records communication inside the CRM.

Supported communication types:

- Call
- Email
- WhatsApp
- SMS
- Internal Notes

---

## 4. Appointment Scheduled

A showroom visit or test drive appointment is scheduled.

Appointment information includes:

- Date & Time
- Status
- Notes

---

## 5. Test Drive Completed

The customer completes the scheduled vehicle test drive.

Sales representatives can update the appointment status accordingly.

---

## 6. Negotiation

Pricing, finance options, exchange offers, and other commercial discussions take place.

---

## 7. Won

The customer proceeds with the vehicle purchase.

The lead reaches the successful end of the sales pipeline.

---

## 8. Lost

The lead is marked as lost when the customer decides not to proceed with the purchase.

---

# Duplicate Prevention

The CRM prevents duplicate lead creation using:

- Email Address
- Phone Number

Duplicate records are rejected before being stored.

---

# Automation

The current version of the project automates the following processes:

- AI Lead Qualification
- AI Lead Scoring
- AI Priority Assignment
- AI Pipeline Prediction
- AI Recommended Action
- AI Follow-up Time Suggestion
- Google Sheets Synchronization
- Activity Logging

---

# CRM Records

The system manages the following information:

- Customer Details
- AI Qualification
- Lead Score
- Pipeline Stage
- Priority
- Appointments
- Follow-ups
- Conversations
- Notes
- Tags
- Activity Logs

---

# Current Limitations

The following processes are managed manually in the current version:

- Appointment Scheduling
- Follow-up Creation
- Conversation Updates
- Pipeline Stage Changes

Future versions may automate these workflows.

---

# Future Enhancements

Possible future improvements include:

- Automatic Follow-up Scheduling
- Email Notifications
- WhatsApp Business API
- SMS Notifications
- AI Voice Assistant
- Background Job Scheduler
- Predictive Sales Analytics
- Customer Re-engagement Automation
- Multi-tenant CRM Support