# routes/animal_details_route.py
from fastapi import APIRouter, HTTPException
from animal import AnimalModel
from animals import animals

router = APIRouter()

# Details eines Tieres Name, Tierart, Einlieferungsdatum, Alter, Geschlecht, geimpft, kastriert
@router.get("/animal/{animalid}")
def get_animaldetails(animalid):
    print(animalid)
    for animal in animals:
        if animal.id == animalid:
            return animal
    raise HTTPException(status_code=404, detail="Vieh not found")

