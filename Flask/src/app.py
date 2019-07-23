import os
from flask import Flask
from flask_cors import CORS
from .config import app_config
from .models import db, bcrypt

from .views.global_view import global_api as global_blueprint
from .views.loc_view import loc_api as loc_blueprint
from .views.home_view import home_api as home_blueprint


def create_app(env_name):
    app = Flask(__name__)
    CORS(app)

    SQLALCHEMY_DATABASE_URI = 'postgres://newtestuser:masterpass12@testid.csrw9zlcpo5t.us-east-1.rds.amazonaws.com/trenddb'
    app.config.from_object(app_config['development'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CORS_HEADERS'] = 'application/json'

    app.register_blueprint(global_blueprint, url_prefix='/api/v1/global')
    app.register_blueprint(loc_blueprint, url_prefix='/api/v1/loc')
    app.register_blueprint(home_blueprint, url_prefix='')

    db.init_app(app)
    bcrypt.init_app(app)

    return app
