# routes/animal_route.py
from fastapi import APIRouter
from studentModel import StudentModel
from studentsList import studentsList
import uuid

router = APIRouter()

# Neues Tier anlegen
@router.put("/student", response_model=None)
def put_student(student:StudentModel):
    student.id = str(uuid(4))
    studentsList.append(student)
    return student

