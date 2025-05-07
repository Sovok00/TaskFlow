from models import Task

task_db: list[Task] = [
  Task(id=1, title="Изучить FastAPI", done=False),
  Task(id=2, title="Написать первый API", done=True),
]
