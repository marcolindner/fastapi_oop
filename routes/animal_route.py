# routes/animal_route.py
from fastapi import APIRouter

router = APIRouter()

@router.put("/animal")
def put_animal():
    return None

