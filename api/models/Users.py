from api.core import Mixin
from .base import db


class Users(Mixin, db.Model):
    """Users Table."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, email):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<ID {self.id}><Username {self.username}>\
        <Email {self.email}><Password {self.password}>"
