
import os


class Settings:
    APP_NAME: str = "RTPM-AIAlert API"
    API_VERSION: str = "0.1.0"
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/rtpm_aialert",
    )


settings = Settings()
