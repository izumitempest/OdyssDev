from app.extensions import db
from models.booking import Booking
from models.trip import Trip
from core.database import session_scope
from core.exceptions import OdyssException

class BookingService:
    @staticmethod
    def create_booking(data, user):
        with session_scope() as session:
            trip = session.query(Trip).get(data["trip_id"])
            if not trip:
                raise OdyssException("Trip not found", 404)
            booking = Booking(user_id=user.id, trip_id=data["trip_id"], status="confirmed")
            session.add(booking)
            return booking