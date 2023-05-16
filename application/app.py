from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from time import time
import asyncio
import json
from application.routers import validation, home

app = FastAPI()

# add static files
app.mount(
    "/static",
    StaticFiles(directory="application/static"),
    name="static",
)

cmsUrl = "http://localhost:8000/api/v2/pages/4/?format=json"
conservationAreaUrl = "https://www.planning.data.gov.uk/dataset/conservation-area.json"

app.include_router(home.router)
app.include_router(validation.router, prefix="/validation")
