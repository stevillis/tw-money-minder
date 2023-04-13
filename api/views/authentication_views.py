"""Login views module."""

from datetime import timedelta

from flask import jsonify, make_response, request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)
from flask_restful import Resource

from api import api
from config import AUTH_TOKEN_VALIDITY

from ..schemas import login_schema
from ..services import user_service


def get_user_fields(req):
    """Get user fields from request."""
    email = req.json["email"]
    password = req.json["password"]

    return email, password


class Login(Resource):
    """Login class based views without parameter."""

    def post(self):
        """User login view."""
        auth_schema = login_schema.LoginSchema()
        validate = auth_schema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        email, password = get_user_fields(request)

        user_db = user_service.get_user_by_email(email)
        if user_db and user_db.validate_password(password):
            access_token = create_access_token(
                identity=user_db.id,
                expires_delta=timedelta(seconds=AUTH_TOKEN_VALIDITY),
            )
            refresh_token = create_refresh_token(identity=user_db.id)

            return make_response(
                jsonify(
                    {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                        "message": "Login realizado com sucesso!",
                    }
                ),
                200,
            )

        return make_response(jsonify({"message": "Credenciais inválidas!"}), 401)


class RefreshToken(Resource):
    """Refresh token class based views without parameter."""

    @jwt_required(refresh=True)
    def post(self):
        """Refresh token view."""
        user_token = get_jwt_identity()
        access_token = create_access_token(
            identity=user_token,
            expires_delta=timedelta(seconds=AUTH_TOKEN_VALIDITY),
        )
        refresh_token = create_refresh_token(identity=user_token)

        return make_response(
            jsonify(
                {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                }
            ),
            200,
        )


api.add_resource(Login, "/login")
api.add_resource(RefreshToken, "/token/refresh")
