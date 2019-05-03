from flask import Flask
from flask_cors import CORS
from .config import app_config
from .models import db, bcrypt

from .views.global_view import global_api as global_blueprint

def create_app(env_name):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(app_config['development'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CORS_HEADERS'] = 'application/json'

    app.register_blueprint(global_blueprint, url_prefix='/api/v1/global')


    db.init_app(app)
    bcrypt.init_app(app)

    return app
