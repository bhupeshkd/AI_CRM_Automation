# 🚗 AI CRM Automation

> **An AI-powered Customer Relationship Management platform for automobile dealerships built with FastAPI, Streamlit, PostgreSQL, and Google Gemini AI.**

Automatically qualify leads, generate AI recommendations, schedule appointments, manage customer conversations, synchronize data with Google Sheets, and track every CRM activity from a single dashboard.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791?style=for-the-badge&logo=postgresql)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-4285F4?style=for-the-badge&logo=google)
![Render](https://img.shields.io/badge/Deployment-Render-46E3B7?style=for-the-badge&logo=render)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

# 🌐 Live Demo

| Service | Link |
|---------|------|
| 🚀 Frontend | https://ai-crm-frontend-m0l5.onrender.com/ |
| ⚡ Backend API | https://ai-crm-backend-ibos.onrender.com |
| 📘 Swagger UI | https://ai-crm-backend-ibos.onrender.com/docs |
| 📖 ReDoc | https://ai-crm-backend-ibos.onrender.com/redoc |

# 📸 Screenshots

## 📊 Dashboard

<img width="1893" height="1048" alt="image" src="https://github.com/user-attachments/assets/20d1ddff-26af-42b9-a89e-4b76f76d2bff" />

---

## 👥 Lead Management

<img width="1919" height="1026" alt="image" src="https://github.com/user-attachments/assets/7d9205df-5bb8-4fd3-ad40-f8426393bbc2" />

---

## 📋 Activity Timeline

<img width="1919" height="1029" alt="image" src="https://github.com/user-attachments/assets/3b893fc3-7999-4b9d-96ef-0b4322d807c5" />


---

# 🚀 Project Overview

AI CRM Automation is a production-ready Customer Relationship Management platform designed specifically for automobile dealerships.

Instead of simply storing customer information, the platform leverages **Google Gemini AI** to automatically analyze every lead, calculate a lead score, assign qualification status and priority, recommend the next sales action, generate AI-powered customer communication, suggest appointments, synchronize data with Google Sheets, and maintain a complete activity timeline.

The application follows a layered architecture that separates APIs, Business Logic, Repositories, AI Modules, Database, and Frontend for better scalability and maintainability.

# ✨ Key Highlights

- 🤖 AI-powered Lead Qualification using Google Gemini
- 📈 Automatic Lead Scoring & Priority Assignment
- 📅 AI Appointment Recommendation
- 💬 AI-generated Customer Communication
- 📞 Follow-up Management
- 📝 Real-time Activity Timeline
- 📊 Interactive CRM Dashboard
- 🔐 JWT Authentication & Role-based Access
- ☁️ Google Sheets Synchronization
- 🏗️ Clean Layered Architecture (API → Service → Repository)

# 🚀 Features

## 👥 Lead Management

Manage the complete customer lifecycle.

- ✅ Create Lead
- ✅ Update Lead
- ✅ Delete Lead
- ✅ View Lead Details
- ✅ Search & Filter Leads
- ✅ AI Lead Qualification
- ✅ Lead Score Generation
- ✅ Pipeline Assignment
- ✅ Priority Assignment

---

## 📅 Appointment Management

Schedule and manage customer meetings.

- ✅ AI Appointment Recommendation
- ✅ Create Appointment
- ✅ Update Appointment
- ✅ Delete Appointment
- ✅ Appointment Status Tracking

---

## 📞 Follow-up Management

Track customer follow-ups efficiently.

- ✅ Create Follow-up
- ✅ Update Follow-up
- ✅ Delete Follow-up
- ✅ Follow-up Status Tracking

---

## 💬 Conversation Management

Maintain complete communication history.

Supported channels:

- 📱 WhatsApp
- 📞 Phone Call
- 📧 Email
- 💬 SMS
- 📝 Notes

---

## 📊 Dashboard

Interactive dashboard built with Streamlit.

- KPI Cards
- Search & Filters
- AgGrid Tables
- Responsive Layout
- Real-time CRM Insights

---

## 🔒 Authentication

- JWT Authentication
- Role-based Access Control

Supported Roles:

- 👑 Admin
- 👨‍💼 Sales Executive

# 🤖 AI Automation

Powered by **Google Gemini AI**, the CRM automatically performs multiple intelligent operations whenever a new lead is created.

### AI Lead Qualification

Automatically generates:

- Lead Score
- Qualification Status
- Priority
- Pipeline Stage
- AI Reasoning
- Recommended Sales Action
- Follow-up Recommendation

---

### AI Appointment Recommendation

The AI recommends:

- Best Appointment Date
- Meeting Type
- Appointment Priority

---

### AI Communication

Automatically generates customer communication for:

- WhatsApp
- Email

Sales executives can directly use AI-generated messages while communicating with customers.

# 📝 Activity Timeline

Every important CRM event is automatically recorded.

Supported activities include:

- ✅ Lead Created
- ✅ Lead Updated
- ✅ Lead Deleted
- ✅ AI Lead Qualification
- ✅ AI Communication Generated
- ✅ Appointment Scheduled
- ✅ Follow-up Scheduled
- ✅ Conversation Added
- ✅ Status Updates

The Activity Timeline provides a complete audit trail, allowing sales teams to understand every action performed on a customer lead without checking backend logs.

# 🏗️ System Architecture

The application follows a clean layered architecture to ensure scalability, maintainability, and separation of concerns.

```text
                    Streamlit Frontend
                           │
                           ▼
                    FastAPI REST API
                           │
     ┌─────────────────────┼─────────────────────┐
     ▼                     ▼                     ▼
 Authentication      CRM Services         AI Services
     │                     │                     │
     └─────────────────────┼─────────────────────┘
                           ▼
                    Repository Layer
                           │
     ┌─────────────────────┼─────────────────────┐
     ▼                     ▼                     ▼
 PostgreSQL          Google Gemini AI      Google Sheets
 (Supabase)          Lead Analysis          Auto Sync
```

The architecture separates business logic from APIs and database operations, making the application modular, testable, and easy to extend.

# ⚙️ Technology Stack

| Category | Technology |
|-----------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| Database | PostgreSQL (Supabase) |
| ORM | SQLAlchemy |
| Data Validation | Pydantic |
| Database Migration | Alembic |
| Authentication | JWT |
| AI Engine | Google Gemini AI |
| Data Analysis | Pandas |
| Tables | AgGrid |
| External Integration | Google Sheets API |
| Deployment | Render |
| Version Control | Git & GitHub |

# 📂 Project Structure

```text
AI_CRM_Automation/

├── backend/
│   ├── app/
│   │   ├── ai/
│   │   ├── api/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   └── alembic/
│
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── styles/
│   ├── utils/
│   └── Home.py
│
├── README.md
├── requirements.txt
└── .env
```

# 🔄 CRM Workflow

```text
Customer Lead Created
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
Qualification Assigned
          │
          ▼
Priority Assigned
          │
          ▼
Pipeline Assigned
          │
          ▼
AI Conversation Generated
          │
          ▼
AI Appointment Recommendation
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
Dashboard Updated
```

Every lead follows this automated pipeline with minimal manual intervention, enabling sales teams to focus on customer engagement instead of repetitive CRM tasks.

# 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/bhupeshkd/AI_CRM_Automation.git

cd AI_CRM_Automation
```

---

## Backend Setup

```bash
cd backend

uv sync

uvicorn app.main:app --reload
```

Backend will start at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

```bash
cd frontend

uv sync

streamlit run Home.py
```

Frontend will start at:

```text
http://localhost:8501
```

# 🔑 Environment Variables

Create a `.env` file inside the backend directory.

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

> **Note:** Never commit your `.env` file or API keys to GitHub.

# 📡 API Documentation

Interactive API documentation is available through Swagger UI and ReDoc.

| Documentation | URL |
|---------------|-----|
| Swagger UI | https://ai-crm-backend-ibos.onrender.com/docs |
| ReDoc | https://ai-crm-backend-ibos.onrender.com/redo |

---

### Main API Modules

- 🔐 Authentication
- 👥 Leads
- 📅 Appointments
- 📞 Follow-ups
- 💬 Conversations
- 📝 Activities

# 📸 Screenshots

## 📅 Appointment Management

<img width="1908" height="1041" alt="image" src="https://github.com/user-attachments/assets/deb2ec24-4ea1-4610-9441-27037050e1fd" />


---

## 📞Follow-Up Management

<img width="1919" height="1037" alt="image" src="https://github.com/user-attachments/assets/dbf5d1fd-2af2-4fc3-a0ac-9d2affe1720c" />


---


## 💬 Conversation Management

<img width="1919" height="1042" alt="image" src="https://github.com/user-attachments/assets/31b2e231-a788-446f-98ad-757f6c925d0e" />



# 👨‍💻 Author

## Bhupesh Kumar Dewangan

Python Developer • AI Developer

### Connect with Me

- 💼 LinkedIn: https://www.linkedin.com/in/bhupesh-dew
- 💻 GitHub: https://github.com/bhupeshkd

If you found this project interesting or useful, feel free to connect with me.

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and contribute according to the license terms.

---

<div align="center">

### ⭐ If you like this project, don't forget to give it a star!

Made with ❤️ using **FastAPI**, **Streamlit**, and **Google Gemini AI**.

</div>
