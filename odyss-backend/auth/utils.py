from flask_jwt_extended import decode_token
from core.exceptions import OdyssException

def verify_token(token):
    try:
        decoded = decode_token(token)
        return decoded["sub"]
    except Exception:
        raise OdyssException("Invalid token", 401)