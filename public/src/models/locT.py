from marshmallow import Schema, fields


class LocSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    url = fields.Str(required=True)
    tweets = fields.Int(required=True)
