from typing import List

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.base_config import auth_backend
from auth.manager import get_user_manager
from auth.models import User, UserRead, UserCreate
from tasks.schemas import Task

app = FastAPI()
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


@app.post("/task/")
async def add_task(tasks: List[Task]):
    pass


@app.get("/users/{user_id}", response_model=List[User])
async def get_user(user_id: int):
    return [user for user in [] if user.get("id") == user_id]

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
