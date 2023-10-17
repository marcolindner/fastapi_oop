from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
#from fastapi.responses import FileResponse
#import os

from routes.root_route import router as root_router
from routes.badge_route import router as badge_router

from routes.student_route import router as student_router
from routes.students_route import router as students_router

from routes.teacher_route import router as teacher_router
from routes.teachers_route import router as teachers_router

from routes.student_details_route import router as student_details_router
from mangum import Mangum

app = FastAPI(title="Student API", version="0.0.1")

#app.include_router(root_router)
app.include_router(students_router)
app.include_router(teacher_router)
app.include_router(teachers_router)
app.include_router(student_router)
app.include_router(badge_router)
app.include_router(student_details_router)


# Unterverzeichnis static für HTML Dateien konfigurieren
app.mount("/", StaticFiles(directory="static"), name="static")

#@app.get("/", response_class=FileResponse)
#async def read_root():
#    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
else:
    handler = Mangum(app)
