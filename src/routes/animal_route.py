# routes/animal_route.py
from fastapi import APIRouter
from animalModel import AnimalModel
from animalsList import animalsList
import uuid

router = APIRouter()

# Neues Tier anlegen
@router.put("/animal", response_model=None)
def put_animal(animal:AnimalModel):
    animal.id = str(uuid.uuid4())
    animalsList.append(animal)
    return animal

