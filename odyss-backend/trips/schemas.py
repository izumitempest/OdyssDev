from marshmallow import Schema, fields, validate, ValidationError
from datetime import datetime

class TripCreateSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    description = fields.Str()
    metadata = fields.Dict(default={})
    start_date = fields.Str(required=True, validate=lambda x: datetime.strptime(x, "%Y-%m-%d"))
    end_date = fields.Str(required=True, validate=lambda x: datetime.strptime(x, "%Y-%m-%d"))