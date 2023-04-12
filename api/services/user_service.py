"""User service module."""

from api import db

from ..entities.user_entity import User as UserEntity
from ..models.user_model import User as UserModel


def create_user(user: UserEntity) -> UserModel:
    """Create user service."""
    user_db = UserModel(name=user.name, email=user.email, password=user.password)
    user_db.encrypt_password()

    db.session.add(user_db)
    db.session.commit()

    return user_db


def get_user_by_pk(pk: int):
    """Get user by pk."""
    return UserModel.query.filter_by(id=pk).first()


def get_user_by_email(email: str):
    """Get user by email."""
    return UserModel.query.filter_by(email=email).first()
