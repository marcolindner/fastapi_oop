# routes/animal_details_route.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/animal/{animalid}")
def get_animal_details(animalid: int):
    return {"animal_id": animalid}

