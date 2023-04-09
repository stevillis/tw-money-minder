"""Account model module."""
from api import db


class Account(db.Model):
    """Account model."""

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    balance = db.Column(db.Float, nullable=False)
