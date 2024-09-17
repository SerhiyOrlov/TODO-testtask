from pydantic import BaseModel, conint
from typing import List

class Task(BaseModel):
    title: str
    description: str
    responsible_user_id: int
    # performers: List[] // TODO: Setup after Authentification
    # status: // TODO: Implement Enum for status
    priority: conint(ge=1, le=4)