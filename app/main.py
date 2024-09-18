from fastapi import FastAPI
from typing import List

from auth.schemas import User
from tasks.schemas import Task
from database import fake_tasks, fake_users

app = FastAPI()


@app.post("/task/")
async def add_task(tasks: List[Task]):
    fake_tasks.extend(tasks)
    return {"status": 200, "data": fake_tasks}

@app.get("/users/{user_id}", response_model=List[User])
async def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]

