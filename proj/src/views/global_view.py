
from ..doc import tweepyAPI
import json
from flask import json, request, Response, Blueprint, g
from ..models.globalT import GlobalModel, GlobalSchema

global_api = Blueprint('Globaltweets', __name__)
global_schema = GlobalSchema()


@global_api.route('/', methods=['GET'])
def glob():
    """
    Endpoint to return whats in the db
    """
    x = GlobalModel.getGlobal()
    data = global_schema.dump(x, many=True).data
    return custom_response(data, 200)


@global_api.route('glob/', methods=['GET'])
def global_trending():
    """
    Endpoint to return whatever is globally trending on twitter and save it
    """
    GlobalModel.clear()
    tweets = GlobalModel.getGlobal()

    trending = tweepyAPI.trends_place(1)
    x = json.dumps(trending)
    for i in trending:
        for trends in i['trends']:
            if trends['name'] is None:
                trends['name'] = 'N/A'

            if trends['url'] is None:
                trends['url'] = 'N/A'

            if trends['tweet_volume'] is None:
                trends['tweet_volume'] = 0

            x = {
                'name': trends['name'],
                'url': trends['url'],
                'tweets': trends['tweet_volume']
            }

            data, error = global_schema.load(x)

            if error:
                print(error)
                return custom_response(error, 404)

            globaltweet = GlobalModel(data)
            globaltweet.save()

    tweets = GlobalModel.getGlobal()
    data = global_schema.dump(tweets, many=True).data
    return custom_response(data, 200)


def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )
