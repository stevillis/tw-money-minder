"""Account schema module."""

from marshmallow import fields as ma_fields

from api import ma

from ..models import account_model


class AccountSchema(ma.SQLAlchemySchema):
    """Account schema class."""

    class Meta:
        """Account schema meta definitions."""

        model = account_model.Account
        fields = ("id", "name", "description", "balance", "_links")
        load_model = True

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
