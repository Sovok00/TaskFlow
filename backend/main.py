from fastapi import FastAPI
from .db import task_db
from .models import Task, TaskCreate

app = FastAPI()


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks_db


@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    new_task = Task(id=len(tasks_db) + 1, title=task.title, done=task.done)
    tasks_db.append(new_task)
    return new_task
