# routes/animals_route.py
from fastapi import APIRouter
from animalModel import AnimalModel
from animalsList import animalsList

router = APIRouter()
# Returned eine reduzierte Liste von animals (Name, Rasse, Einlieferungsdatum)
@router.get("/animals")
def get_animals():
    # return [animal.id, animal.name, animal.species, animal.arrival_date]
    miniAnimalList = []
    
    for animal in animalsList:
        miniAnimalList.append({"id": animal.id,"name": animal.name, "species": animal.species, "arrival_date": animal.arrival_date})
    
    return miniAnimalList

