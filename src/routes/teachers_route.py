# routes/students_route.py
from fastapi import APIRouter
from teacherModel import TeacherModel
from teachersList import teachersList

router = APIRouter()
@router.get("/teachers")
def get_teachers():
    miniTeachersList = []
    
    for teacher in teachersList:
        miniTeachersList.append({"id": teacher.id,"name": teacher.name })
    
    return miniTeachersList
