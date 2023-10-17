# routes/root_route.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_root():
    return "Student API"

