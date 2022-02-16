from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import router
from config import settings
from pipeline import gather_canotify_data

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT"],
    allow_headers=["*"],
)

app.include_router(router.router, prefix="/api")


@app.get("/")
async def read_index():
    return FileResponse("static/index.html")


@app.on_event("startup")
async def init_schedule():
    gather_canotify_data()

    schedule = AsyncIOScheduler()
    schedule.add_job(gather_canotify_data, "cron", hour=0)
    schedule.start()
