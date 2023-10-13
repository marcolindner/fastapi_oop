# routes/animals_route.py
from fastapi import APIRouter
from animal import AnimalModel
from animals import animalsList

router = APIRouter()
# Returned eine reduzierte Liste von animals (Name, Rasse, Einlieferungsdatum)
@router.get("/animals")
def get_animals():
    # return [Animal.name, Animal.species, Animal.arrival_date]
    miniAnimalList = []
    
    for animal in animalsList:
        miniAnimalList.append({"name": animal.name, "species": animal.species, "arrival_date": animal.arrival_date})
    
    return miniAnimalList

