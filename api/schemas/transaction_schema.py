"""Transaction schema module."""

from marshmallow import fields as ma_fields

from api import ma

from ..models import transaction_model


class TransactionSchema(ma.SQLAlchemyAutoSchema):
    """Transaction schema class."""

    class Meta:
        """Transaction schema meta definitions."""

        model = transaction_model.Transaction
        fields = (
            "id",
            "name",
            "description",
            "value",
            "transaction_type",
            "account_id",
            "_links",
        )
        load_instance = True

    name = ma_fields.String(required=True)
    description = ma_fields.String(required=True)
    value = ma_fields.Float(required=True)
    transaction_type = ma_fields.String(required=True)
    account_id = ma_fields.Integer(required=True)

    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("transactiondetail", values=dict(pk="<id>")),
            "put": ma.URLFor("transactiondetail", values=dict(pk="<id>")),
            "delete": ma.URLFor("transactiondetail", values=dict(pk="<id>")),
        }
    )
