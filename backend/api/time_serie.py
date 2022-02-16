from datetime import datetime
from typing import List
import pandas as pd

from fastapi import APIRouter
from pydantic import BaseModel


class Score(BaseModel):
    date: datetime
    value: float


router = APIRouter()


@router.get("/cases", response_model=List[Score])
def get_cases():
    df = pd.read_csv("static/data/cases.csv")
    cases = df[["date", "confirmed_cases"]]
    cases.columns = ["date", "value"]
    cases.date = pd.to_datetime(cases.date)
    return [row.to_dict() for i, row in cases.iterrows()]


@router.get("/deaths", response_model=List[Score])
def get_deaths():
    df = pd.read_csv("static/data/cases.csv")
    deaths = df[["date", "reported_deaths"]]
    deaths.columns = ["date", "value"]
    deaths.date = pd.to_datetime(deaths.date)
    return [row.to_dict() for i, row in deaths.iterrows()]
