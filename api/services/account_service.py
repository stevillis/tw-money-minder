"""Account service module."""

from typing import List

from api import db

from ..entities.account_entity import Account as AccountEntity
from ..models.account_model import Account as AccountModel


def create_account(account: AccountEntity) -> AccountModel:
    """Create account service."""
    account_db = AccountModel(
        name=account.name, description=account.description, balance=account.balance
    )

    db.session.add(account_db)
    db.session.commit()

    return account_db


def get_accounts() -> List[AccountModel]:
    """Get accounts service."""
    return AccountModel.query.all()


def get_account_by_pk(pk):
    """Get account by pk service."""
    return AccountModel.query.filter_by(id=pk).first()


def update_account(account_db, new_account):
    """Update account service."""
    account_db.name = new_account.name
    account_db.description = new_account.description
    account_db.balance = new_account.balance
    db.session.commit()


def delete_account(account):
    """Delete account service."""
    db.session.delete(account)
    db.session.commit()
