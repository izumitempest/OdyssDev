from app.extensions import db
from models.base import BaseModel
from sqlalchemy.dialects.postgresql import UUID

class Booking(BaseModel):
    __tablename__ = "bookings"
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)
    trip_id = db.Column(UUID(as_uuid=True), db.ForeignKey("trips.id"), nullable=False)
    status = db.Column(db.String(50), default="pending")
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "trip_id": str(self.trip_id),
            "status": self.status,
        }