import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from todo_api.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    last_update = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

    todos = db.relationship('Todo',
                            foreign_keys='Todo.user_id',
                            backref='user',
                            lazy=True)

    @property
    def unhashed_password(self):
        raise ValueError("You cannot get the unhashed password!")

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password: str):
        self.password = generate_password_hash(unhashed_password)

    def validate_password(self, unhashed_password: str) -> bool:
        return check_password_hash(self.password, unhashed_password)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    completed = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    last_update = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
