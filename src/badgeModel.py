from pydantic import BaseModel
from typing import Optional

class BadgeModel(BaseModel):
        id: str
        name: str
        description: str
        badgeType: str
        condition: str
        rewardType: str


