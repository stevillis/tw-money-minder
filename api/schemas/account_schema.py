"""Account schema module."""

from marshmallow import fields as ma_fields

from api import ma

from ..models import account_model
from ..schemas.transaction_schema import TransactionSchema


class AccountSchema(ma.SQLAlchemyAutoSchema):
    """Account schema class."""

    transactions = ma_fields.Nested(TransactionSchema, many=True)

    class Meta:
        """Account schema meta definitions."""

        model = account_model.Account
        fields = ("id", "name", "description", "balance", "transactions", "_links")
        load_instance = True

    name = ma_fields.String(required=True)
    description = ma_fields.String(required=True)
    balance = ma_fields.Float(required=True)

    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("accountdetail", values=dict(pk="<id>")),
            "put": ma.URLFor("accountdetail", values=dict(pk="<id>")),
            "delete": ma.URLFor("accountdetail", values=dict(pk="<id>")),
        }
    )
