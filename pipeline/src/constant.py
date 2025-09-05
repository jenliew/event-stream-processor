from enum import Enum

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    postgres_user: str = "DEFAULT_USER"
    postgres_password: str = "DEFAULT_PASSWORD"
    database_host: str = "localhost"
    database_port: str = "localhost"
    database_name: str = "DB_NAME"
    database_host: str = "DB_NAME"
    database_url: str = "localhost"

    class Config:  # type: ignore
        env_file = ".env"


settings = Settings()

DATABASE_URL = (
    f"postgresql+asyncpg://{settings.postgres_user}:"
    f"{settings.postgres_password}"
    f"@{settings.database_url}/{settings.database_name}"
)

DEFAULT_RATE_LIMIT = 40  # Max requests per minute
DEFAULT_URL_API_STR = "127.0.0.1:8000"
MAX_RETRIES = 3
HTTP_TIMEOUT = 120  # Timeout 30 seconds
DEFAULT_WORKER_NUM = 3
MAX_RETRIES_POLL = 20
# Fields at the campaign level
CAMPAIGN_KEYS = {
    "campaign_id",
    "campaign_name",
    "campaign_budget",
    "start_date",
    "end_date",
    "objective",
}

# Mapping to normalize ad group keys
AD_GROUP_KEY_MAPPING = {
    "ad_group_id": "id",
    "ad_group_name": "name",
    "bid": "bid",
    "targeting_ages": "targeting_ages",
    "targeting_interests": "targeting_interests",
    "targeting_geo": "targeting_geo",
}

ADS_KEY_MAPPING = {
    "ad_id": "id",
    "ad_type": "type",
    "creative_url": "creative_url",
    "click_url": "click_url",
    "ad_status": "status",
}


class API_REQUEST(Enum):
    GET = 1
    POST = 2
