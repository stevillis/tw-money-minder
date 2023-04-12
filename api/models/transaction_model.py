"""Transaction model module."""
from enum import Enum

from api import db


class TransactionTypeEnum(Enum):
    """Transaction Type Enum definition."""

    IN = 1
    OUT = 2


class Transaction(db.Model):
    """Transaction model."""

    __tablename__ = "transaction"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    value = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.Enum(TransactionTypeEnum), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))

    account = db.relationship(
        "Account", backref=db.backref("transactions", lazy="dynamic")
    )
