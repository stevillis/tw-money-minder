"""Account views module."""

from flask import jsonify, make_response, request
from flask_restful import Resource

from api import api

from ..entities import account_entity
from ..models.account_model import Account
from ..pagination import paginate
from ..schemas import account_schema
from ..services import account_service


def get_account_fields(req):
    """Get account fields from request."""
    name = req.json["name"]
    description = req.json["description"]
    balance = req.json["balance"]

    return name, description, balance


class AccountList(Resource):
    """Account class based views without parameter."""

    def get(self):
        """
        List all Accounts.
        ---
        responses:
          200:
            description: List of all Accounts.
            schema:
              id: Account
              properties:
                id:
                  type: integer
                name:
                  type: string
                description:
                  type: string
                balance:
                  type: string
        """
        # accounts = account_service.get_accounts()
        ts = account_schema.AccountSchema(many=True)

        # return make_response(ts.jsonify(accounts), 200)
        return paginate(Account, ts)

    def post(self):
        """
        Create Account.
        ---
        parameters:
          - in: body
            name: Account
            description: Create a Account.
            schema:
              type: object
              required:
                - name
                - description
                - balance
              properties:
                name:
                  type: string
                description:
                  type: string
                balance:
                  type: string
        responses:
          201:
            description: Account created successfully.
            schema:
              id: Account
              properties:
                name:
                  type: string
                description:
                  type: string
                balance:
                  type: string
          400:
            description: Bad request. Loading Accounts failed.
          404:
            description: Account not found.
        """
        # claims = get_jwt()
        # if claims["roles"] != "admin":
        #     return make_response(jsonify("User without authorization to access the resource."), 403)

        ts = account_schema.AccountSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        name, description, balance = get_account_fields(request)

        new_account = account_entity.Account(
            name=name,
            description=description,
            balance=balance,
        )

        account_db = account_service.create_account(new_account)

        return make_response(ts.jsonify(account_db), 201)


class AccountDetail(Resource):
    """Account class based views with parameter."""

    def get(self, pk):
        """
        Get a Account by its pk.
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
        responses:
          200:
            description: The Account if found.
            schema:
              id: Account
              properties:
                id:
                  type: integer
                name:
                  type: string
                description:
                  type: string
                balance:
                  type: string
          404:
            description: Account not found.
        """
        account = account_service.get_account_by_pk(pk)
        if not account:
            return make_response(jsonify("Account not found!"), 404)

        ts = account_schema.AccountSchema()
        return make_response(ts.jsonify(account), 200)

    def put(self, pk):
        """
        Update Account.
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
          - in: body
            description: Update a Account
            schema:
              type: object
              required:
                - name
                - description
                - balance
              properties:
                name:
                  type: string
                description:
                  type: string
                balance:
                  type: string
        responses:
          200:
            description: Account successfully updated.
            schema:
              id: Account
              properties:
                name:
                  type: string
                description:
                  type: string
                balance:
                  type: string
          400:
            description: Bad request. Malformed data.
          404:
            description: Account not found.
        """
        account_db = account_service.get_account_by_pk(pk)
        if not account_db:
            return make_response(jsonify("Account not found!"), 404)

        ts = account_schema.AccountSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        name, description, balance = get_account_fields(request)

        new_account = account_entity.Account(
            name=name,
            description=description,
            balance=balance,
        )

        account_service.update_account(account_db, new_account)
        updated_account = account_service.get_account_by_pk(pk)

        return make_response(ts.jsonify(updated_account), 200)

    def delete(self, pk):
        """
        Delete a Account.
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
        responses:
          204:
            description: Account successfully deleted.
          404:
            description: Account not found.
        """
        account = account_service.get_account_by_pk(pk)
        if not account:
            return make_response(jsonify("Account not found!"), 404)

        account_service.delete_account(account)
        return make_response("", 204)


api.add_resource(AccountList, "/accounts")
api.add_resource(AccountDetail, "/accounts/<int:pk>")
