"""Account service module."""

from typing import List

from api import db
from api.models.transaction_model import TransactionTypeEnum
from api.types import OperationTypeEnum

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

    return account_db


def delete_account(account):
    """Delete account service."""
    db.session.delete(account)
    db.session.commit()


def update_account_balance(
    account_id, transaction, operation_type, old_balance_value=None
):
    """Update account balance based on transaction type."""
    account = get_account_by_pk(account_id)
    if operation_type == OperationTypeEnum.INSERT:
        if transaction.transaction_type == TransactionTypeEnum.IN.name:
            account.balance += transaction.value
        else:
            account.balance -= transaction.value
    elif operation_type == OperationTypeEnum.UPDATE:
        if transaction.transaction_type == TransactionTypeEnum.IN.name:
            account.balance -= old_balance_value
            account.balance += transaction.value
        else:
            account.balance += old_balance_value
            account.balance -= transaction.value
    elif operation_type == OperationTypeEnum.DELETE:
        if transaction.transaction_type == TransactionTypeEnum.IN.name:
            account.balance -= transaction.value
        else:
            account.balance += transaction.value
    else:
        return None

    db.session.commit()
