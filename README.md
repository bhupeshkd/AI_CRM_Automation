<!-- ========================================================= -->
<!--                 AI CRM AUTOMATION SYSTEM                  -->
<!-- ========================================================= -->

<h1 align="center">
🤖 AI CRM Automation System
</h1>

<p align="center">
Production-Ready AI Powered CRM Automation Platform built with FastAPI, Streamlit, PostgreSQL (Supabase), Google Gemini AI, JWT Authentication and Google Sheets Integration.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)

![FastAPI](https://img.shields.io/badge/FastAPI-Production-green?logo=fastapi)

![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-blue?logo=postgresql)

![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-orange)

![Gemini AI](https://img.shields.io/badge/Google-Gemini_AI-blue)

![JWT](https://img.shields.io/badge/JWT-Authentication-success)

![License](https://img.shields.io/badge/License-MIT-green)

</p>

<p align="center">

<a href="https://ai-crm-frontend-m0l5.onrender.com">
<img src="https://img.shields.io/badge/🌐_Live_Demo-Visit-success?style=for-the-badge" />
</a>

<a href="https://ai-crm-backend-ibos.onrender.com/docs">
<img src="https://img.shields.io/badge/📚_API_Docs-Swagger-blue?style=for-the-badge" />
</a>

<a href="https://ai-crm-backend-ibos.onrender.com">
<img src="https://img.shields.io/badge/⚡_Backend-Live-orange?style=for-the-badge" />
</a>

</p>

---

# 🚀 Project Overview

AI CRM Automation is a production-ready Customer Relationship Management platform designed for automobile dealerships.

Instead of simply storing customer information, the system automatically analyzes every lead using Google Gemini AI, qualifies the customer, assigns a lead score and priority, recommends the next sales action, synchronizes lead data with Google Sheets, and provides an interactive CRM dashboard for managing leads, appointments, follow-ups, and conversations.

The project follows a layered architecture with a clear separation between APIs, Services, Repositories, AI modules, Database, and Frontend.

---

# ✨ Features

## 👥 Lead Management

- Create Lead
- Update Lead
- Delete Lead
- View Lead Details
- AI Lead Qualification
- Lead Score Generation
- Pipeline Assignment
- Priority Assignment

---

## 🤖 AI Lead Qualification

Automatically generates:

- Lead Score
- Qualification Status
- Pipeline Stage
- Priority
- AI Reason
- Recommended Action
- Follow-up Time

Powered by **Google Gemini AI**

---

## 📅 Appointment Management

- Create Appointment
- Update Appointment
- Delete Appointment
- Appointment Status Tracking

---

## 📞 Follow-up Management

- Create Follow-up
- Update Follow-up
- Delete Follow-up
- Status Tracking

---

## 💬 Conversation Management

Maintain complete customer communication history.

Supported communication types:

- Call
- Email
- WhatsApp
- SMS
- Notes

---

## 📊 Dashboard

Interactive Streamlit Dashboard with:

- KPI Cards
- Search
- Filters
- AgGrid Tables
- Responsive Layout

---

## 🔒 Authentication

JWT Authentication

Role-based User Management

- Admin
- Sales Executive

---

## 📑 Google Sheets Integration

Every newly created lead is automatically synchronized with Google Sheets for reporting and CRM backup.

---

# 🏗️ Architecture

```text
                 Streamlit Frontend
                         │
                         ▼
                  FastAPI REST API
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
 Authentication     CRM Services      AI Services
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
                  Repository Layer
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
 PostgreSQL       Google Gemini AI   Google Sheets
 (Supabase)         Lead Analysis      Auto Sync
```

---

# ⚙️ Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Supabase
- Alembic
- JWT Authentication
- Pydantic

## Frontend

- Streamlit
- AgGrid
- Pandas

## AI

- Google Gemini AI

## Database

- PostgreSQL (Supabase)

## Integrations

- Google Sheets API

---

# 📂 Project Structure

```text
AI_CRM_Automation/

├── backend/
│   ├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── styles/
│   ├── utils/
│   └── Home.py
│
└── README.md
```

---

# 🔄 CRM Workflow

```text
Lead Created
      │
      ▼
Duplicate Validation
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
Lead Saved to PostgreSQL
      │
      ▼
Google Sheets Sync
      │
      ▼
Activity Logged
      │
      ▼
Dashboard Updated
```

---

# 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/bhupeshkd/AI_CRM_Automation.git

cd AI_CRM_Automation
```

---

## Backend

```bash
cd backend

uv sync

uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

uv sync

streamlit run Home.py
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
DATABASE_URL=

SECRET_KEY=

JWT_ALGORITHM=

ACCESS_TOKEN_EXPIRE_MINUTES=

GEMINI_API_KEY=

GOOGLE_SHEET_NAME=

GOOGLE_WORKSHEET_NAME=

GOOGLE_CREDENTIALS=
```

---

# 📡 API Documentation

### Swagger UI

```text
https://ai-crm-backend-ibos.onrender.com/docs
```

### ReDoc

```text
https://ai-crm-backend-ibos.onrender.com/redoc
```

---

# 📸 Screenshots

> Screenshots will be added soon.

- Login
- Dashboard
- Lead Management
- Appointment Management
- Follow-up Management
- Conversation Management

---

# 🚀 Future Improvements

- Email Notifications
- WhatsApp Business API
- SMS Integration
- Background Job Scheduler
- Redis + Celery
- Docker Support
- CI/CD Pipeline
- AI Voice Assistant
- Advanced Analytics Dashboard
- RAG-based Customer Knowledge Assistant

---

# 👨‍💻 Author

**Bhupesh Kumar Dewangan**

Python Developer • AI Developer

**GitHub**

https://github.com/bhupeshkd

**LinkedIn**

https://www.linkedin.com/in/bhupesh-dew

---

# 📄 License

This project is licensed under the MIT License.

⭐ If you found this project useful, consider giving it a star.