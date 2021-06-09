#!/usr/bin/python3
###############################################################################
# Script      : main.py
# Author      : David Velez
# Date        : 06/08/2021
# Description : Test Driven with FastAPI and Docker (Course)
###############################################################################

# Imports
import os
from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise
# Custom Imports
from app.config import get_settings, Settings

api = FastAPI()

register_tortoise(
    api,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@api.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
