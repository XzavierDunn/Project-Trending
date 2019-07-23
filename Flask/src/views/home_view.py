from flask import request, Blueprint

home_api = Blueprint('Home', __name__)

@home_api.route('/', methods=['GET'])
def home():
    return 'Hello World'
