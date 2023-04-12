"""User views module."""

from flask import jsonify, make_response, request
from flask_restful import Resource

from api import api

from ..entities import user_entity
from ..schemas import user_schema
from ..services import user_service


def get_user_fields(req):
    """Get user fields from request."""
    name = req.json["name"]
    email = req.json["email"]
    password = req.json["password"]

    return name, email, password


class UserList(Resource):
    """User class based views without parameter."""

    def post(self):
        """Create User view."""
        us = user_schema.UserSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        name, email, password = get_user_fields(request)

        new_user = user_entity.User(name=name, email=email, password=password)

        user_db = user_service.create_user(new_user)

        return make_response(us.jsonify(user_db), 201)


api.add_resource(UserList, "/users")
