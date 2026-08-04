from fastapi import FastAPI
from app.api.lead import router as lead_router

app = FastAPI(
    title="AI CRM Automation API",
    description="Production Ready AI CRM Automation System",
    version="1.0.0",
)

app.include_router(lead_router)

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
        "service": "AI CRM Automation Backend"
    }