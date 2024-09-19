from .utils import get_user_db
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/users/")
async def get_users(user_db=Depends(get_user_db)):
    # Работа с пользователями
    pass
