from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.lead import router as lead_router
from app.api import appointment
from app.api import conversation
from app.api import follow_up
from app.api import auth


app = FastAPI(
    title="AI CRM Automation API",
    description="Production Ready AI CRM Automation System",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Deployment ke baad specific URL rakhna
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lead_router)
app.include_router(appointment.router)
app.include_router(conversation.router)
app.include_router(follow_up.router)
app.include_router(auth.router)


@app.get("/", tags=["Root"])
async def root():
    return {
        "status": "success",
        "message": "Welcome to AI CRM Automation API 🚀",
    }


@app.get("/health", tags=["Health"])
async def health():
    return {
    "status": "healthy",
    "service": "AI CRM Automation Backend",
    "version": "1.0.0",
}