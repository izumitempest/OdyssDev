# from functools import wraps
# from flask_jwt_extended import verify_jwt_in_request
# from core.dependencies import get_current_user
# from core.exceptions import OdyssException

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         verify_jwt_in_request()
#         user = get_current_user()
#         if not user:
#             raise OdyssException("Unauthorized", 401)
#         return f(current_user=user, *args, **kwargs)
#     return decorated_function

from flask_jwt_extended import jwt_required
from core.dependencies import get_current_user

def jwt_auth_required():
    def decorated_function(f):
        @jwt_required()
        def wrapper(*args, **kwargs):
            user = get_current_user()
            return f(current_user=user, *args, **kwargs)
        return wrapper
    return decorated_function