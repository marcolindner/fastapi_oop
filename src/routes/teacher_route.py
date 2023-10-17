# routes/students_route.py
from fastapi import APIRouter
from teacherModel import TeacherModel
from teachersList import teachersList

router = APIRouter()
@router.put("/teacher", response_model=None)
def put_teacher(teacher:TeacherModel):
    teacher.id=str( uuid4())
    teachersList.append( teacher )
    return teacher
