from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    OPENAI_API_KEY: str = ""

    GEMINI_API_KEY: str

    GOOGLE_SHEET_NAME: str

    GOOGLE_WORKSHEET_NAME: str

    GOOGLE_CREDENTIALS: str

    SECRET_KEY: str

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()