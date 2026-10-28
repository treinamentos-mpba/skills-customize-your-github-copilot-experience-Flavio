import uvicorn
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel


app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


tasks = {}
next_task_id = 1


# TODO: Add GET /tasks to return all tasks.
# TODO: Add POST /tasks to validate and store a task.
# TODO: Add GET, PUT, and DELETE routes for /tasks/{task_id}.


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)