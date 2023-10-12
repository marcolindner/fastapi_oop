# routes/animals_route.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/animals")
def get_animals():
    return None

