from flask_jwt_extended import get_jwt_identity
from models.user import User
from core.database import session_scope

def get_current_user():
    user_id = get_jwt_identity()
    if not user_id:
        return None
    with session_scope() as session:
        return session.query(User).get(user_id)