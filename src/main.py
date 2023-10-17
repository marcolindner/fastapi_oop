from fastapi import FastAPI
from routes.root_route import router as root_router
from routes.students_route import router as students_router
from routes.student_route import router as student_router
from routes.student_details_route import router as student_details_router
from mangum import Mangum

app = FastAPI(title="Student API", version="0.0.1", root_path="/Prod")

app.include_router(root_router)
app.include_router(students_router)
app.include_router(student_router)
app.include_router(student_details_router)

handler = Mangum(app)
