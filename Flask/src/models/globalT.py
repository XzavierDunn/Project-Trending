
from . import db, bcrypt
from marshmallow import Schema, fields
from ..doc import *
import requests
from flask import Response, json


class GlobalModel(db.Model):
    __tablename__ = 'globalTweets'

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
        num_rows_deleted = db.session.query(GlobalModel).delete()
        db.session.commit()

    @staticmethod
    def getGlobal():
        return GlobalModel.query.all()



def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )


class GlobalSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    url = fields.Str(required=True)
    tweets = fields.Int(required=True)
