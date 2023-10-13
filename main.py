from animal import Animal
from fastapi import FastAPI, HTTPException
app = FastAPI(title="Animal API", version="0.0.1")
animals: list[Animal] = []

# Basis Route
@app.get("/")
def get_root():
    return "Animal API"

# Liste aller Tiere mit Name, Tierart, Einlieferungsdatum
@app.get("/animals")
def get_animals():
    return None

# Neues Tier anlegen
@app.put("/animal")
def put_animal(animal:Animal):
    animals.append(animal)
    return animal

# Details eines Tieres Name, Tierart, Einlieferungsdatum, Alter, Geschlecht, geimpft, kastriert
@app.get("/animal/{animalid}")
def get_animaldetails(animalid):
    print(animalid)
    for animal in animals:
        if animal.id == animalid:
            return animal
    raise HTTPException(status_code=404, detail="Vieh not found")
    #return None

if(__name__ == "__main__"):
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
