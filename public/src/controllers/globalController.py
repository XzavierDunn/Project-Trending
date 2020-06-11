from flask import json, request, Response, Blueprint, g, make_response
from ..services.globalService import getGlobal

globalApi = Blueprint('Globaltweets', __name__)


@globalApi.route('/', methods=['GET'])
def glob():
    """
    Endpoint to return whats in the db
    """
    return make_response(getGlobal(), 200)
