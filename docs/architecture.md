# AI CRM Automation System Architecture

## Overview

The AI CRM Automation System is a production-oriented backend application built using FastAPI and PostgreSQL. The system automates the complete customer journey from lead capture to appointment booking while maintaining activity history, conversation logs, follow-up automation, and CRM synchronization.

The project follows a layered architecture to ensure clean separation of concerns, maintainability, scalability, and easier testing.

---

# High Level Architecture

```
                Client Applications
       (Swagger UI / React / Mobile App)
                       │
                       ▼
                FastAPI REST APIs
                       │
 ┌─────────────────────┼─────────────────────┐
 │                     │                     │
 ▼                     ▼                     ▼
Lead APIs        Appointment APIs     Conversation APIs
 │                     │                     │
 └─────────────────────┼─────────────────────┘
                       ▼
                Service Layer
 │────────────────────────────────────────────│
 │ LeadService                                │
 │ AppointmentService                         │
 │ FollowUpService                            │
 │ ConversationService                        │
 │ AutomationService                          │
 │ ActivityService                            │
 │ GoogleSheetService                         │
 │────────────────────────────────────────────│
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
Repository Layer   AI Qualification   Google Sheets
      │
      ▼
 PostgreSQL Database
```

---

# Project Layers

## 1. API Layer

The API layer exposes REST endpoints to external applications.

Responsibilities:

- Receive HTTP requests
- Validate request payloads
- Call business services
- Return API responses

Examples:

- /leads
- /appointments
- /follow-ups
- /conversations

---

## 2. Service Layer

The Service Layer contains all business logic.

Responsibilities:

- AI Lead Qualification
- Appointment Validation
- Duplicate Detection
- Follow-up Automation
- Activity Logging
- Google Sheet Synchronization
- CRM Workflow Management

Business rules are never written inside API routes.

---

## 3. Repository Layer

Repositories are responsible for database communication.

Responsibilities:

- Create Records
- Read Records
- Update Records
- Delete Records

Repositories isolate SQLAlchemy logic from business logic.

---

## 4. AI Layer

The AI Qualification module evaluates incoming leads using:

- Budget
- Purchase Timeline
- Vehicle Interest
- City

The AI returns:

- Lead Score
- Qualification Status
- Pipeline Stage
- Priority
- Recommended Action
- Follow-up Time
- AI Reason

---

## 5. Database Layer

PostgreSQL stores all CRM information.

Current Tables:

- Leads
- Activities
- Appointments
- Conversations
- FollowUps

---

## 6. External Services

The system integrates with Google Sheets to maintain a live CRM copy.

Information synchronized:

- Customer Details
- Lead Score
- Qualification
- Pipeline
- Notes
- Tags
- AI Reason

---

# Design Principles

The project follows:

- Layered Architecture
- Repository Pattern
- Service Pattern
- Separation of Concerns
- Single Responsibility Principle
- Scalable Folder Structure

---

# Benefits

This architecture provides:

- Easy maintenance
- Better scalability
- Cleaner codebase
- Easier testing
- Production-ready design
- Simple integration with external CRMs

---

# Future Improvements

The architecture can be extended with:

- JWT Authentication
- Redis
- Celery Background Jobs
- WhatsApp API
- Email Automation
- Voice AI
- Docker
- Kubernetes
- Monitoring & Logging
- CI/CD Pipeline
