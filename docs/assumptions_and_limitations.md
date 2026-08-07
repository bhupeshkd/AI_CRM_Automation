# Assumptions and Limitations

# Assumptions

The following assumptions were made during the development of the system.

## Business Assumptions

- Each customer is uniquely identified by their email address and phone number.
- Every lead represents a potential customer interested in purchasing a vehicle.
- AI qualification is automatically triggered whenever a new lead is created.
- One appointment can only be assigned to one lead at a specific date and time.
- Sales executives use AI recommendations to prioritize customer follow-ups.

---

## Technical Assumptions

- PostgreSQL (Supabase) is the primary database.
- Google Gemini AI returns structured and valid JSON responses.
- Google Sheets is used for automatic lead synchronization and reporting.
- FastAPI serves as the backend REST API.
- Streamlit provides the user interface and dashboard.
- JWT tokens are used for API authentication.

---

# Current Limitations

Although the project is production-ready, the current version has the following limitations:

- No email notification system
- No WhatsApp Business API integration
- No SMS notification service
- No background job scheduler (Celery/APScheduler)
- No Docker containerization
- No CI/CD pipeline
- No Redis-based task queue
- No automated reminder notifications
- No file upload support for customer documents
- No multi-tenant (organization-based) architecture

---

# Future Scope

Potential enhancements for future versions include:

- Email Automation
- WhatsApp Business API Integration
- SMS Notifications
- Background Task Scheduling
- Automated Follow-up Reminders
- AI Voice Assistant
- AI Receptionist
- RAG-based Customer Knowledge Assistant
- Docker & Kubernetes Deployment
- CI/CD Pipeline
- Redis + Celery Integration
- Advanced Analytics Dashboard
- Predictive Sales Analytics
- Multi-language Support
- Multi-tenant CRM Architecture