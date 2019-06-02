
from . import db, bcrypt
from marshmallow import Schema, fields
from ..doc import *
import requests
from flask import Response, json


class LocModel(db.Model):
    __tablename__ = 'locTrends'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    tweets = db.Column(db.Integer, nullable=False)

    def __init__(self, data):
        self.name = data.get('name')
        self.url = data.get('url')
        self.tweets = data.get('tweets')

    def __repr__(self):
        return f'<id {self.id}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    @staticmethod
    def clear():
        num_rows_deleted = db.session.query(LocModel).delete()
        db.session.commit()


    @staticmethod
    def getLoc():
        return LocModel.query.all()


    @staticmethod
    def getCoords(location):
        r = requests.get(f'http://www.mapquestapi.com/geocoding/v1/address?key=G7GTGs1Pf62DjHNWUAcsu8Jn7bxjNJvz&location={location}')
        for i in r.json()['results']:
                x = i['locations'][0]['latLng']
                lat = x['lat']
                lng = x['lng']
        return lat, lng


    @staticmethod
    def woeid(coords):
        lat = coords[0]
        lng = coords[1]
        location = tweepyAPI.trends_closest(lat, lng)
        x = location[0]['woeid']
        return x


def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )


class LocSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    url = fields.Str(required=True)
    tweets = fields.Int(required=True)
