from models.trip import Trip
from core.database import session_scope

class TripRepository:
    @staticmethod
    def get_by_id(trip_id):
        with session_scope() as session:
            return session.query(Trip).get(trip_id)