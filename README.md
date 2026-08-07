<!-- ========================================================= -->
<!--                       AI CRM AUTOMATION                    -->
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

---

<h1 align="center">
🤖 AI CRM Automation System
</h1>

<p align="center">
Production-Ready AI Powered CRM Automation Platform built with FastAPI, Streamlit, PostgreSQL (Supabase), Google Gemini AI, JWT Authentication and Google Sheets Integration.
</p>

<p align="center">

![Python](...)
![FastAPI](...)
![Streamlit](...)
...

</p>

<p align="center">

<a href="https://frontend-m0l5.onrender.com">
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


# 🚀 Project Overview

AI CRM Automation is a complete Customer Relationship Management platform designed for automobile dealerships.

Instead of simply storing customer information, the system automatically analyzes every lead using Artificial Intelligence, qualifies the customer, recommends the next action, schedules follow-ups, stores conversations, synchronizes data with Google Sheets, and provides an interactive management dashboard.

The project follows a production-style architecture with clear separation between API, Services, Repositories, AI modules and Frontend.

---

# ✨ Features

## 👥 Lead Management

- Create Lead
- Update Lead
- Delete Lead
- View Lead Details
- AI Lead Qualification
- Automatic Lead Score
- Pipeline Management
- Priority Assignment

---

## 🤖 AI Lead Qualification

Automatically generates

- Lead Score
- Qualification Status
- Pipeline Stage
- Priority
- CRM Notes
- CRM Tags
- Recommended Action
- Follow-up Time

Powered by **Google Gemini AI**

---

## 📧 AI Communication Generator

Automatically creates

- Professional Email Subject
- Professional Email Body
- WhatsApp Message

Personalized according to customer information.

---

## 📅 Appointment Management

- Schedule Appointment
- Update Appointment
- Cancel Appointment
- Appointment Status Tracking

---

## 📞 Follow-up Management

- Create Follow-up
- Update Follow-up
- Delete Follow-up
- Status Tracking

---

## 💬 Conversation Management

Maintain complete customer communication history

Supports

- Call
- WhatsApp
- Email
- SMS
- Notes

---

## 📊 Dashboard

Interactive Streamlit Dashboard

Includes

- KPI Cards
- Search
- Filters
- AgGrid Tables
- CSV Export
- Responsive Layout

---

## 🔒 Authentication

JWT Authentication

Role Based User System

- Admin
- Sales Executive

---

## 📑 Google Sheets Integration

Every lead is automatically synchronized to Google Sheets.

---

# 🏗 Architecture

```
                Streamlit Frontend
                        │
                        ▼
                FastAPI REST API
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
 Gemini AI       PostgreSQL        Google Sheets
                        │
                        ▼
                SQLAlchemy ORM
```

---

# ⚙ Tech Stack

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

- PostgreSQL
- Supabase

## Integrations

- Google Sheets API

---

# 📂 Project Structure

```
AI_CRM_Automation/

│
├── backend/
│   ├── app/
│   │
│   ├── ai/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   │
│   └── main.py
│
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── styles/
│   ├── utils/
│   └── Home.py
│
└── README.md
```

---

# 🔄 CRM Workflow

```
Lead Created

        │

        ▼

AI Qualification

        │

        ▼

Google Sheets Sync

        │

        ▼

Recommended Action

        │

        ▼

Conversation

        │

        ▼

Follow-up

        │

        ▼

Appointment

        │

        ▼

Sales Conversion
```

---

# 🛠 Installation

Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_CRM_Automation.git

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

# Environment Variables

Create `.env`

```
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

# API Documentation

FastAPI automatically provides

```
/docs

/redoc
```

---

# Screenshots

Coming Soon

- Login
- Dashboard
- Lead Management
- Appointment
- Follow-up
- Conversation

---

# Future Improvements

- Email Integration
- WhatsApp API
- Docker
- CI/CD
- Background Tasks
- Notifications
- Analytics Dashboard
- Role Based Permissions
- Unit Testing

---

# Author

**Bhupesh Kumar Dewangan**

Python Developer • AI Developer

GitHub

https://github.com/bhupeshkd

LinkedIn

https://www.linkedin.com/in/bhupesh-dew

---

# License

This project is licensed under the MIT License.

⭐ If you found this project useful, consider giving it a star.