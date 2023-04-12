from flasgger import Swagger
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# App config
app = Flask(__name__)
app.config.from_object("config")

# Database config
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# Authentication
jwt = JWTManager(app)

# API config
api = Api(app)

# API Documentation
Swagger(app)

from .models import account_model, transaction_model, user_model
from .views import account_views, transaction_views, user_views
