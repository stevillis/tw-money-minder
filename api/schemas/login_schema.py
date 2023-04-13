"""Login schema module."""

from marshmallow import fields as ma_fields

from api import ma

from ..models import user_model


class LoginSchema(ma.SQLAlchemyAutoSchema):
    """Login schema class."""

    class Meta:
        """Login schema meta definitions."""

        model = user_model.User

    name = ma_fields.String(required=False)
    email = ma_fields.String(required=True)
    password = ma_fields.String(required=True)
