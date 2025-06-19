from flask import g
from flask_jwt_extended import get_jwt_identity
from app.extensions import db
from models.user import User

def get_current_user():
    user_id = get_jwt_identity()
    if not user_id:
        raise Exception("No user identity found")
    user = db.session.query(User).get(user_id)
    if not user:
        raise Exception("User not found")
    g.user = user
    return user