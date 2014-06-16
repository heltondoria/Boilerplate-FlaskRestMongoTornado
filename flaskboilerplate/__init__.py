from flask import Flask
from flask.ext import restful
from flask_restful.utils import cors
from decorators import authenticate

# Configure the Application
app = Flask(__name__)
app.config.from_object('flaskboilerplate.config.Config')

from odm import odm



# Configure the Applications API
api = restful.Api(app)
api.decorators = [
    authenticate(endpoint=app.config['OAUTH_ENDPOINT']),
    cors.crossdomain(origin=app.config['CORS_ORIGIN'], methods=app.config['CORS_METHODS'],headers=app.config['CORS_HEADERS'])
]

# Load all further resources
from . import views
from . import resources
