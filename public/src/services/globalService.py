import json
from ..doc import tweepyAPI
from ..models.globalT import GlobalSchema

globalSchema = GlobalSchema()


def getGlobal():

    trending = tweepyAPI.trends_place(1)

    x = json.dumps(trending)
    all = []

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

            data, error = globalSchema.load(x)

            if error:
                return (error, 404)

            all.append(x)

    return json.dumps(all)
