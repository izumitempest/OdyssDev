from app.extensions import db
from models.trip import Trip
from core.database import session_scope
from core.exceptions import OdyssException
from datetime import datetime

class TripService:
    @staticmethod
    def create_trip(data, user):
        with session_scope() as session:
            trip = Trip(
                name=data["name"],
                description=data.get("description"),
                trip_metadata=data.get("trip_metadata", {}),
                start_date=datetime.strptime(data["start_date"], "%Y-%m-%d"),
                end_date=datetime.strptime(data["end_date"], "%Y-%m-%d"),
                creator_id=user.id,
            )
            session.add(trip)
            return trip
    
    @staticmethod
    def get_trips(page, per_page):
        with session_scope() as session:
            return session.query(Trip).limit(per_page).offset((page - 1) * per_page).all()