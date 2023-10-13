# routes/animal_details_route.py
from fastapi import APIRouter, HTTPException
from animalModel import AnimalModel
from animalsList import animalsList

router = APIRouter()

# Details eines Tieres Name, Tierart, Einlieferungsdatum, Alter, Geschlecht, geimpft, kastriert
@router.get("/animal/{animalId}")
def get_animaldetails(animalId):
    for animal in animalsList:
        if animal.id == animalId:
            return animal
    raise HTTPException(status_code=404, detail="Vieh not found")

