# routes/animals_route.py
from fastapi import APIRouter
from studentModel import StudentModel
from studentsList import studentsList

router = APIRouter()
# Returned eine reduzierte Liste von animals (Name, Rasse, Einlieferungsdatum)
@router.get("/students")
def get_students():
    miniStudentList = []
    
    for student in studentsList:
        miniStudentList.append({"id": student.id,"name": student.name })
    
    return miniStudentList
