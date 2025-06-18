from app.extensions import db
from models.base import BaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Role(BaseModel):
    __tablename__ = "roles"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def to_dict(self):
        return {"id": str(self.id), "name": self.name}