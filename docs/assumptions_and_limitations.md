# Assumptions and Limitations

# Assumptions

The following assumptions were made during development.

## Business

- Every lead is unique.
- Email and phone identify a customer.
- One appointment occupies one time slot.
- AI qualification executes immediately after lead creation.

---

## Technical

- PostgreSQL stores all CRM data.
- Google Sheets acts as external CRM reporting.
- FastAPI exposes REST APIs.
- AI qualification returns structured JSON.

---

# Limitations

Current MVP limitations include:

- No user authentication
- No role-based access control
- No background scheduler
- No WhatsApp Business API
- No Email API
- No SMS integration
- No Dashboard
- No Analytics
- No Docker deployment
- No Redis queue
- No Celery workers

---

# Future Scope

Possible enhancements:

- JWT Authentication
- Background Jobs
- Voice AI
- AI Receptionist
- WhatsApp Bot
- Email Automation
- RAG-based CRM
- Docker
- Kubernetes
- CI/CD
- Monitoring
- Analytics Dashboard
- Multi-language Support