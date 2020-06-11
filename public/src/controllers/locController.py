from flask import Blueprint, make_response
from ..services.locService import getLoc

locApi = Blueprint('LocTweets', __name__)


@locApi.route('<location>/', methods=['GET'])
def locate_trending(location):
    """
    Endpoint for location based trends on twitter
    """

    results = getLoc(location)
    if type(results) != list:
        return make_response(results)
    else:
        return make_response(results, 200)
