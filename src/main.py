from fastapi import FastAPI
from root_route import router as root_router
# from root_route import router as root_router
# from routes.animals_route import router as animals_router
# from routes.animal_route import router as animal_router
# from routes.animal_details_route import router as animal_details_router
from mangum import Mangum

app = FastAPI(title="Animal API", version="0.0.1", openapi_url="/openapi.json")

app.include_router(root_router)
# app.include_router(animals_router)
# app.include_router(animal_router)
# app.include_router(animal_details_router)

handler = Mangum(app)