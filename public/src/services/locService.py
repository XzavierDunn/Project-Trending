import json
import requests
from ..doc import tweepyAPI
from ..models.locT import LocSchema

locSchema = LocSchema()


def getWoeid(coords):
    lat = coords[0]
    lng = coords[1]
    location = tweepyAPI.trends_closest(lat, lng)
    x = location[0]['woeid']
    return x


def getCoords(location):
    r = requests.get(
        f'http://www.mapquestapi.com/geocoding/v1/address?key=G7GTGs1Pf62DjHNWUAcsu8Jn7bxjNJvz&location={location}')
    for i in r.json()['results']:
        x = i['locations'][0]['latLng']
        lat = x['lat']
        lng = x['lng']
    return lat, lng


def getLoc(location):
    location = str(location)

    coords = getCoords(location)
    woeid = getWoeid(coords)
    trending = tweepyAPI.trends_place(woeid)

    x = json.dumps(trending)
    all = []

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

            data, error = locSchema.load(x)

            if error:
                return (error, 404)

            all.append(x)

    return json.dumps(all)
