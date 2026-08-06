from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):

    # ==========================
    # Database
    # ==========================
    DATABASE_URL: str

    # ==========================
    # AI APIs
    # ==========================
    OPENAI_API_KEY: str = ""

    GEMINI_API_KEY: str

    # ==========================
    # Google Sheets
    # ==========================
    GOOGLE_SHEET_NAME: str

    GOOGLE_WORKSHEET_NAME: str

    GOOGLE_CREDENTIALS: str

    GOOGLE_CREDENTIALS_JSON: str = ""

    # ==========================
    # JWT Authentication
    # ==========================
    SECRET_KEY: str

    JWT_ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # ==========================
    # Environment
    # ==========================
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()