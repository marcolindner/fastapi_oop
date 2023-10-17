# routes/student_details_route.py
from fastapi import APIRouter, HTTPException
from studentModel import StudentModel
from studentsList import studentsList

router = APIRouter()

@router.get("/student/{studentId}")
def get_student_details(studentId):
    for student in studentsList:
        if student.id == studentId:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

