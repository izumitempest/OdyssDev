from marshmallow import Schema, fields
from uuid import UUID

class BookingCreateSchema(Schema):
    trip_id = fields.UUID(required=True)