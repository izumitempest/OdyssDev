from app.extensions import db
from models.base import BaseModel
from sqlalchemy.dialects.postgresql import UUID

class Payment(BaseModel):
    __tablename__ = "payments"
    booking_id = db.Column(UUID(as_uuid=True), db.ForeignKey("bookings.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    status = db.Column(db.String(50), default="pending")
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "booking_id": str(self.booking_id),
            "amount": self.amount,
            "currency": self.currency,
            "status": self.status,
        }