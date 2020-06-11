import os
from flask import Flask
from flask_cors import CORS
from src.config import app_config

from src.controllers import global_blueprint
from src.controllers import loc_blueprint

env_name = os.getenv('FLASK_ENV')

app = Flask(__name__)
CORS(app)

app.config.from_object(app_config['development'])

app.register_blueprint(global_blueprint, url_prefix='/api/v1/global')
app.register_blueprint(loc_blueprint, url_prefix='/api/v1/loc')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
