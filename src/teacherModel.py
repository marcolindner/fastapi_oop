from pydantic import BaseModel
from typing import Optional

class TeacherModel(BaseModel):
        id: str
        name: str
        sex: str
        castrated: bool


