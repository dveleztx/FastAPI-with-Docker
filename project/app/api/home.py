# Imports
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def index():
    return "Welcome to the Test-Driven FastAPI Demo"
