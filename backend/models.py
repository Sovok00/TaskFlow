from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

class TaskCreate(BaseModel):
  title: str
  done: bool = False


