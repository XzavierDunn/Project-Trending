
from ..doc import *
import json
from flask import json, request, Response, Blueprint, g
from ..models.locT import LocModel, LocSchema


loc_api = Blueprint('LocTweets', __name__)
loc_schema = LocSchema()


@loc_api.route('/clear', methods=['GET'])
def clear():
    LocModel.clear()
    print('cleared =========================================')


@loc_api.route('<location>/', methods=['GET'])
def locate_trending(location):
    """
    Endpoint for location based trends on twitter
    """
    LocModel.clear()
    str(location)
    coords = LocModel.getCoords(location)
    woeid = LocModel.woeid(coords)
    trending = tweepyAPI.trends_place(woeid)
    x = json.dumps(trending)
    for i in trending:
        for trends in i['trends']:
            if not trends['name']:
                trends['name'] = 'N/A'

            if not trends['url']:
                trends['url'] = 'N/A'

            if not trends['tweet_volume']:
                trends['tweet_volume'] = 0

            x = {
                'name': trends['name'],
                'url': trends['url'],
                'tweets': trends['tweet_volume']
            }

            data, error = loc_schema.load(x)

            if error:
                print(error)
                return custom_response(error, 404)

            loctweet = LocModel(data)
            loctweet.save()

    tweets = LocModel.getLoc()
    data = loc_schema.dump(tweets, many=True).data
    return custom_response(data, 200)


@loc_api.route('/', methods=['GET'])
def glob():
    """
    Endpoint to return whats in the db
    """
    x = LocModel.getLoc()
    data = loc_schema.dump(x, many=True).data
    return custom_response(data, 200)


def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )
