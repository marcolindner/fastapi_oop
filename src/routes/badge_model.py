# routes/student_route.py
from fastapi import APIRouter
from badgeModel import BadgeModel
from badgesList import badgesList
import uuid

router = APIRouter()

# Neue Badge anlegen
@router.put("/badge", response_model=None)
def put_badge(badge:BadgeModel):
    badge.id = str(uuid(4))
    badgesList.append(bage)
    return badge

