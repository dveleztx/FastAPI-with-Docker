#!/usr/bin/python3
###############################################################################
# Script      : main.py
# Author      : David Velez
# Date        : 06/08/2021
# Description : Test Driven with FastAPI and Docker (Course)
###############################################################################

# Imports
import logging
from fastapi import FastAPI
# Custom Imports
from app.api import ping, summaries
from app.db import init_db


log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(summaries.router, prefix="/summaries", tags=["summaries"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
