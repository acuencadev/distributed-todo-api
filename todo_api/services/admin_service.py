import uuid
from typing import List, Optional

from todo_api.extensions import db
from todo_api.models import User


def create_user(username: str, unhashed_password: str, admin: bool = False) -> User:
    user = User(public_id=uuid.uuid4(), username=username, unhashed_password=unhashed_password, admin=admin)

    db.session.add(user)
    db.session.commit()

    return user


def get_all_users() -> List[User]:
    return User.query.all()


def get_user_by_public_id(public_id: str) -> Optional[User]:
    user = User.query.filter_by(public_id=public_id).first()

    return user


def update_user(public_id: str, username: str, admin: bool = False) -> Optional[User]:
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return None

    user.username = username
    user.admin = admin

    db.session.commit()

    return user


def promote_user(public_id: str) -> Optional[User]:
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return None

    user.admin = True

    db.session.commit()

    return user


def delete_user(public_id: str) -> bool:
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return False

    db.session.delete(user)
    db.session.commit()

    return True


def delete_all_users() -> int:
    users_deleted = User.query.delete()

    db.session.commit()

    return users_deleted
