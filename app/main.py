#!/usr/bin/python3
###############################################################################
# Script      : main.py
# Author      : David Velez
# Date        : 06/08/2021
# Description : Test Driven with FastAPI and Docker (Course)
###############################################################################

# Imports
from fastapi import FastAPI, Depends
from app.config import get_settings, Settings

api = FastAPI()


@api.get("/ping")
def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
