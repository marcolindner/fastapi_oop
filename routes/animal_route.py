# routes/animal_route.py
from fastapi import APIRouter
from animal import Animal
from animals import animals

router = APIRouter()

# Neues Tier anlegen
@router.put("/animal")
def put_animal(animal:Animal):
    animals.append(animal)
    return animal

