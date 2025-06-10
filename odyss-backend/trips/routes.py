from flask import Blueprint, request, jsonify
from trips.services import TripService
from trips.schemas import TripCreateSchema
from auth.guards import login_required
from core.exceptions import OdyssException

trips_bp = Blueprint("trips", __name__)

@trips_bp.route("", methods=["POST"])
@login_required
def create_trip(current_user):
    try:
        schema = TripCreateSchema()
        data = schema.load(request.get_json())
        trip = TripService.create_trip(data, current_user)
        return jsonify({"message": "Trip created", "trip": trip.to_dict()}), 201
    except Exception as e:
        raise OdyssException(str(e), 400)

@trips_bp.route("", methods=["GET"])
def get_trips():
    try:
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)
        trips = TripService.get_trips(page, per_page)
        return jsonify({"trips": [trip.to_dict() for trip in trips]}), 200
    except Exception as e:
        raise OdyssException(str(e), 400)