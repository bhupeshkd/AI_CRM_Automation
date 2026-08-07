# AI CRM Automation System Architecture

## Overview

The AI CRM Automation System is a production-ready Customer Relationship Management (CRM) platform built using **FastAPI**, **Streamlit**, **PostgreSQL (Supabase)**, and **Google Gemini AI**.

The system automates AI-powered lead qualification, lead scoring, priority assignment, pipeline prediction, Google Sheets synchronization, and activity logging while providing a modern CRM interface for managing leads, appointments, follow-ups, and customer conversations.

The project follows a layered architecture with clear separation of concerns, making it scalable, maintainable, and production-ready.

---

# High Level Architecture

```text
                   Streamlit Frontend
                           │
                           ▼
                    FastAPI REST APIs
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 Authentication      CRM Services        AI Services
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                    Repository Layer
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 PostgreSQL          Google Gemini AI   Google Sheets
  (Supabase)           Lead Analysis     Auto Sync
```

---

# Architecture Layers

## 1. Frontend Layer

The frontend is developed using **Streamlit**.

### Responsibilities

- User Authentication
- Dashboard
- Lead Management
- Appointment Management
- Follow-up Management
- Conversation Management
- API Communication

---

## 2. API Layer

The API layer exposes REST endpoints to client applications.

### Responsibilities

- Receive HTTP requests
- Validate request payloads
- Authenticate users
- Invoke business services
- Return structured JSON responses

### API Modules

- Authentication
- Leads
- Appointments
- Follow-ups
- Conversations

---

## 3. Service Layer

The Service Layer contains all business logic.

### Responsibilities

- AI Lead Qualification
- Lead Scoring
- Priority Assignment
- Pipeline Prediction
- Appointment Validation
- Google Sheets Synchronization
- Activity Logging
- CRM Workflow Management

Business logic is isolated from API routes to improve maintainability.

---

## 4. Repository Layer

Repositories manage all database operations using SQLAlchemy.

### Responsibilities

- Create Records
- Read Records
- Update Records
- Delete Records

This layer isolates database access from business logic.

---

## 5. AI Layer

The AI module is powered by **Google Gemini AI**.

During lead creation, the AI evaluates:

- Budget
- Purchase Timeline
- Vehicle Interest
- Lead Source
- Customer Notes

The AI automatically generates:

- Lead Score
- Qualification Status
- Pipeline Stage
- Priority
- Recommended Action
- Follow-up Time
- AI Reason

---

## 6. Database Layer

The application uses **PostgreSQL (Supabase)** as the primary database.

### Main Tables

- Users
- Leads
- Appointments
- FollowUps
- Conversations
- Activities

---

## 7. External Integrations

### Google Gemini AI

Used for intelligent lead qualification and recommendation generation.

### Google Sheets

Every newly created lead is automatically synchronized to Google Sheets for reporting and CRM backup.

---

# Design Principles

The project follows modern software engineering practices:

- Layered Architecture
- Repository Pattern
- Service Pattern
- Separation of Concerns
- Single Responsibility Principle (SRP)
- Modular Folder Structure
- RESTful API Design
- JWT Authentication
- Scalable Code Organization

---

# System Workflow

```text
Customer Creates Lead
          │
          ▼
FastAPI Receives Request
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
Lead Saved to PostgreSQL
          │
          ▼
Google Sheets Synchronization
          │
          ▼
Activity Logged
          │
          ▼
Response Returned to Frontend
```

---

# Benefits

The architecture provides:

- Clean Code Organization
- Scalable Design
- Easy Maintenance
- Separation of Business Logic
- Production-Ready Structure
- Easy Integration with External Services
- Simplified Testing
- Better Readability

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL (Supabase) |
| AI | Google Gemini AI |
| Authentication | JWT |
| API Validation | Pydantic |
| Migration | Alembic |
| External Integration | Google Sheets API |
| Deployment | Render |

---

# Future Enhancements

The architecture can be extended with:

- Email Notifications
- WhatsApp Business API
- SMS Integration
- Background Job Scheduler
- Redis + Celery
- Docker Containerization
- Kubernetes Deployment
- CI/CD Pipeline
- Monitoring & Logging
- AI Voice Assistant
- RAG-based Knowledge Assistant
- Predictive Sales Analytics
- Multi-tenant CRM Architecture