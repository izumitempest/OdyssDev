from app.extensions import db
from models.base import BaseModel

class Permission(BaseModel):
    __tablename__ = "permissions"
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    
    def to_dict(self):
        return {"id": str(self.id), "name": self.name, "description": self.description}