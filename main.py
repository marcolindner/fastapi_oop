from animal import Animal
from fastapi import FastAPI, HTTPException
from routes.root_route import router as root_router
from routes.animals_route import router as animals_router
from routes.animal_route import router as animal_router
from routes.animal_details_route import router as animal_details_router

app = FastAPI(title="Animal API", version="0.0.1")

app.include_router(root_router)
app.include_router(animals_router)
app.include_router(animal_router)
app.include_router(animal_details_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

