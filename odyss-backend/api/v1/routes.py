from flask import Blueprint
from auth.routes import auth_bp
from trips.routes import trips_bp
from bookings.routes import bookings_bp

api_v1_bp = Blueprint("api_v1", __name__)

api_v1_bp.register_blueprint(auth_bp, url_prefix="/auth")
api_v1_bp.register_blueprint(trips_bp, url_prefix="/trips")
api_v1_bp.register_blueprint(bookings_bp, url_prefix="/bookings")