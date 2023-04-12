"""Transaction service module."""

from typing import List

from api import db

from ..entities.transaction_entity import Transaction as TransactionEntity
from ..models.transaction_model import Transaction as TransactionModel


def create_transaction(transaction: TransactionEntity) -> TransactionModel:
    """Create transaction service."""
    transaction_db = TransactionModel(
        name=transaction.name,
        description=transaction.description,
        value=transaction.value,
        transaction_type=transaction.transaction_type,
        account_id=transaction.account_id,
    )

    db.session.add(transaction_db)
    db.session.commit()

    return transaction_db


def get_transactions() -> List[TransactionModel]:
    """Get transactions service."""
    return TransactionModel.query.all()


def get_transaction_by_pk(pk):
    """Get transaction by pk service."""
    return TransactionModel.query.filter_by(id=pk).first()


def update_transaction(transaction_db, new_transaction):
    """Update transaction service."""
    transaction_db.name = new_transaction.name
    transaction_db.description = new_transaction.description
    transaction_db.value = new_transaction.value
    transaction_db.transaction_type = new_transaction.transaction_type
    transaction_db.account_id = new_transaction.account_id
    db.session.commit()

    return transaction_db


def delete_transaction(transaction):
    """Delete transaction service."""
    db.session.delete(transaction)
    db.session.commit()
