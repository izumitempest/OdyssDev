from app.extensions import db
from models.user import User
from flask_jwt_extended import create_access_token
from core.database import session_scope
from core.exceptions import OdyssException

class AuthService:
    @staticmethod
    def login(email, password):
        with session_scope() as session:
            user = session.query(User).filter_by(email=email).first()           
            if user and user.check_password(password):
                access_token = create_access_token(identity=user.id)
                return {"access_token": access_token, "user": user.to_dict()}, 200
            raise OdyssException("Invalid credentials", 401)
    
    @staticmethod
    def register(email, password):
        with session_scope() as session:
            if session.query(User).filter_by(email=email).first():
                raise OdyssException("Email already exists", 400)
            user = User(email=email)
            user.set_password(password)
            session.add(user)
            return {"message": "User created", "user": user.to_dict()}, 201