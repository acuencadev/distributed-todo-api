import uuid
from typing import List, Optional

from todo_api.extensions import db
from todo_api.models import Todo


def create_todo(text: str, user_id: int) -> Todo:
    todo = Todo(public_id=uuid.uuid4(), text=text, user_id=user_id)

    db.session.add(todo)
    db.session.commit()

    return todo


def get_all_todos() -> List[Todo]:
    return Todo.query.all()


def get_todo_by_public_id(public_id: str) -> Optional[Todo]:
    todo = Todo.query.filter_by(public_id=public_id).first()

    return todo


def update_todo(public_id: str, text: str, completed: bool) -> Optional[Todo]:
    todo = Todo.query.filter_by(public_id=public_id).first()

    if not todo:
        return None

    todo.text = text
    todo.completed = completed

    db.session.commit()

    return todo


def complete_todo(public_id: str) -> Optional[Todo]:
    todo = Todo.query.filter_by(public_id=public_id).first()

    if not todo:
        return None

    todo.completed = True

    db.session.commit()

    return todo


def delete_todo(public_id: str) -> bool:
    todo = Todo.query.filter_by(public_id=public_id).first()

    if not todo:
        return False

    db.session.delete(todo)
    db.session.commit()

    return True


def delete_all_todos() -> int:
    todos_deleted = Todo.query.delete()

    db.session.commit()

    return todos_deleted
