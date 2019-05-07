
from ..doc import *
import json
from flask import json, request, Response, Blueprint, g
from ..models.globalT import GlobalModel, GlobalSchema


global_api = Blueprint('tweets', __name__)
global_schema = GlobalSchema()

# Endpoint to return whatever is globally trending on twitter
@global_api.route('/', methods=['GET'])
def global_trending():
    trending = tweepyAPI.trends_place(1)
    x = json.dumps(trending)
    for i in trending:
        for trends in i['trends']:        
            if trends['name'] == None:
                trends['name'] = 'N/A'

            if trends['url'] == None:
                trends['url'] = 'N/A'

            if trends['tweet_volume'] == None or 'None':
                trends['tweet_volume'] = 0

            x = {
                'name': trends['name'],
                'url' : trends['url'],
                'tweets': trends['tweet_volume']
            }
            print(x, ' x ======================')

            data, error = global_schema.load(x)

            if error:
                print(error)
                return custom_response(error, 404)

            globaltweet = GlobalModel(data)
            globaltweet.save()


    tweets = GlobalModel.getGlobal()
    data = global_schema.dump(tweets, many=True).data
    return custom_response(data, 200)


# Endpoint for location based trends on twitter
@global_api.route('/loc', methods=['GET'])
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
