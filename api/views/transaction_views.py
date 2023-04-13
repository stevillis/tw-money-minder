"""Transaction views module."""

from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api import api

from ..entities import transaction_entity
from ..models.transaction_model import Transaction
from ..pagination import paginate
from ..schemas import transaction_schema
from ..services import account_service, transaction_service


def get_transaction_fields(req):
    """Get transaction fields from request."""
    name = req.json["name"]
    description = req.json["description"]
    value = req.json["value"]
    transaction_type = req.json["transaction_type"]
    account_id = req.json["account_id"]

    return name, description, value, transaction_type, account_id


class TransactionList(Resource):
    """Transaction class based views without parameter."""

    @jwt_required()
    def get(self):
        """
        List all Transactions.
        ---
        responses:
          200:
            description: List of all Transactions.
            schema:
              id: Transaction
              properties:
                id:
                  type: integer
                name:
                  type: string
                description:
                  type: string
                value:
                  type: string
                transaction_type:
                  type: string
        """
        # transactions = transaction_service.get_transactions()
        acc_schema = transaction_schema.TransactionSchema(many=True)

        # return make_response(acc_schema.jsonify(transactions), 200)
        return paginate(Transaction, acc_schema)

    @jwt_required()
    def post(self):
        """
        Create Transaction.
        ---
        parameters:
          - in: body
            name: Transaction
            description: Create a Transaction.
            schema:
              type: object
              required:
                - name
                - description
                - value
                - transaction_type
              properties:
                name:
                  type: string
                description:
                  type: string
                value:
                  type: string
                transaction_type:
                  type: string
        responses:
          201:
            description: Transaction created successfully.
            schema:
              id: Transaction
              properties:
                name:
                  type: string
                description:
                  type: string
                value:
                  type: string
                transaction_type:
                  type: string
          400:
            description: Bad request. Loading Transactions failed.
          404:
            description: Transaction not found.
        """
        # claims = get_jwt()
        # if claims["roles"] != "admin":
        #     return make_response(jsonify("User without authorization to access the resource."), 403)

        acc_schema = transaction_schema.TransactionSchema()
        validate = acc_schema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        name, description, value, transaction_type, account_id = get_transaction_fields(
            request
        )

        if not account_service.get_account_by_pk(account_id):
            return make_response("Account not found!", 404)

        new_transaction = transaction_entity.Transaction(
            name=name,
            description=description,
            value=value,
            transaction_type=transaction_type,
            account_id=account_id,
        )

        transaction_db = transaction_service.create_transaction(new_transaction)

        return make_response(acc_schema.jsonify(transaction_db), 201)


class TransactionDetail(Resource):
    """Transaction class based views with parameter."""

    @jwt_required()
    def get(self, pk):
        """
        Get a Transaction by its pk.
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
        responses:
          200:
            description: The Transaction if found.
            schema:
              id: Transaction
              properties:
                id:
                  type: integer
                name:
                  type: string
                description:
                  type: string
                value:
                  type: string
                transaction_type:
                  type: string
                account_id:
                  type: int
          404:
            description: Transaction not found.
        """
        transaction = transaction_service.get_transaction_by_pk(pk)
        if not transaction:
            return make_response(jsonify("Transaction not found!"), 404)

        acc_schema = transaction_schema.TransactionSchema()
        return make_response(acc_schema.jsonify(transaction), 200)

    @jwt_required()
    def put(self, pk):
        """
        Update Transaction.
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
          - in: body
            description: Update a Transaction
            schema:
              type: object
              required:
                - name
                - description
                - value
                - transaction_type
                - account_id
              properties:
                name:
                  type: string
                description:
                  type: string
                value:
                  type: string
                transaction_type:
                  type: string
                account_id:
                  type: int
        responses:
          200:
            description: Transaction successfully updated.
            schema:
              id: Transaction
              properties:
                name:
                  type: string
                description:
                  type: string
                value:
                  type: string
                transaction_type:
                  type: string
                account_id:
                  type: int
          400:
            description: Bad request. Malformed data.
          404:
            description: Transaction not found.
        """
        transaction_db = transaction_service.get_transaction_by_pk(pk)
        if not transaction_db:
            return make_response(jsonify("Transaction not found!"), 404)

        acc_schema = transaction_schema.TransactionSchema()
        validate = acc_schema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        name, description, value, transaction_type, account_id = get_transaction_fields(
            request
        )

        if not account_service.get_account_by_pk(account_id):
            return make_response("Account not found!", 404)

        new_transaction = transaction_entity.Transaction(
            name=name,
            description=description,
            value=value,
            transaction_type=transaction_type,
            account_id=account_id,
        )

        updated_transaction = transaction_service.update_transaction(
            transaction_db, new_transaction
        )

        return make_response(acc_schema.jsonify(updated_transaction), 200)

    @jwt_required()
    def delete(self, pk):
        """
        Delete a Transaction.
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
        responses:
          204:
            description: Transaction successfully deleted.
          404:
            description: Transaction not found.
        """
        transaction = transaction_service.get_transaction_by_pk(pk)
        if not transaction:
            return make_response(jsonify("Transaction not found!"), 404)

        transaction_service.delete_transaction(transaction)
        return make_response("", 204)


api.add_resource(TransactionList, "/transactions")
api.add_resource(TransactionDetail, "/transactions/<int:pk>")
