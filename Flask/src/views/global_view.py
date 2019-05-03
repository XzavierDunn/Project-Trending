
from ..doc import *
import json
from flask import json, request, Response, Blueprint, g
from ..models.globalT import GlobalModel, GlobalSchema


global_api = Blueprint('tweets', __name__)
gloabl_schema = GlobalSchema()

# Endpoint to return whatever is globally trending on twitter
@global_api.route('trending', methods=['GET'])
def global_trending():
    trending = tweepyAPI.trends_place(1)
    x = json.dumps(trending)
    return custom_response(x, 200)


# Endpoint for location based trends on twitter
@global_api.route('/', methods=['GET'])
def locate_trending():
    # staticmethod that takes in a location and returns coordinates
    coords = GlobalModel.getCoords('indianapolis')
    woeid = GlobalModel.woeid(coords)
    trending = tweepyAPI.trends_place(woeid)
    x = json.dumps(trending)

    return custom_response(x, 200)


def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )
