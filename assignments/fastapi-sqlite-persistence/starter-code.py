from contextlib import contextmanager
from pathlib import Path
import sqlite3
from typing import Iterator

import uvicorn
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel


DATABASE_PATH = Path(__file__).with_name("tasks.db")
app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def initialize_database() -> None:
    with get_connection() as connection:
        # TODO: Create the tasks table if it does not already exist.
        pass


def row_to_task(row: sqlite3.Row) -> dict[str, int | str | bool]:
    return {
        "id": row["id"],
        "title": row["title"],
        "completed": bool(row["completed"]),
    }


initialize_database()


# TODO: Add GET /tasks to return all tasks from SQLite.
# TODO: Add POST /tasks to insert a task and return it with status 201.
# TODO: Add GET, PUT, and DELETE routes for /tasks/{task_id}.


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
