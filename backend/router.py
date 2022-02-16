from fastapi import APIRouter
from api import time_serie

router = APIRouter()

router.include_router(
    time_serie.router, prefix="/time_serie", tags=["time_serie"]
)  # noqa: E501
