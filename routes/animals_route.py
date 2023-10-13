# routes/animals_route.py
from fastapi import APIRouter
from animal import Animal
from animals import animals

router = APIRouter()

@router.get("/animals")
def get_animals():
    return [Animal.name, Animal.species, Animal.arrival_date]

