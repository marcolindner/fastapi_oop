# routes/animal_route.py
from fastapi import APIRouter
from animal import AnimalModel
from animals import animalsList

router = APIRouter()

# Neues Tier anlegen
@router.put("/animal")
def put_animal(animal:AnimalModel):
    animalsList.append(animal)
    return animal

