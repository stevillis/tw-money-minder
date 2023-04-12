"""User schema module."""

from marshmallow import fields as ma_fields

from api import ma

from ..models import user_model


class UserSchema(ma.SQLAlchemyAutoSchema):
    """User schema class."""

    class Meta:
        """User schema meta definitions."""

        model = user_model.User
        fields = ("id", "name", "email", "password")
        load_instance = True

    name = ma_fields.String(required=True)
    email = ma_fields.String(required=True)
    password = ma_fields.String(required=True)
