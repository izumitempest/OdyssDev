from app.extensions import db
from models.base import BaseModel
from sqlalchemy.dialects.postgresql import JSONB

class Trip(BaseModel):
    __tablename__ = "trips"
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    metadata = db.Column(JSONB, default={})
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    creator_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "metadata": self.metadata,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "creator_id": str(self.creator_id),
        }