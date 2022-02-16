from enum import Enum
from pathlib import Path
from typing import List, Union

from pydantic import BaseSettings, HttpUrl, AnyHttpUrl, validator

BASE_DATADESK_URL: HttpUrl = "https://raw.githubusercontent.com/datadesk/california-coronavirus-data/master/"  # noqa: E501


class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class Settings(BaseSettings):
    ENVIRONMENT: Environment = Environment.DEVELOPMENT

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(
        cls, v: Union[str, List[str]]
    ) -> Union[List[str], str]:  # noqa: 501
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    OUTPUT_DATA: Path = Path("static/data")

    @validator("OUTPUT_DATA", pre=True)
    def assemble_output_dir(cls, v: Union[str, Path]) -> Path:
        if isinstance(v, str):
            return Path(v)
        elif isinstance(v, Path):
            return v
        raise ValueError(v)

    # Urls for non engagement data
    BASE_DATADESK_URL: HttpUrl = BASE_DATADESK_URL
    URL_CASES_DEATHS: HttpUrl = (
        BASE_DATADESK_URL + "cdph-state-cases-deaths.csv"
    )  # noqa: 501

    class Config:
        case_sensitive = True


settings = Settings()
settings.OUTPUT_DATA.mkdir(parents=True, exist_ok=True)
