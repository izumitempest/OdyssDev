from flask import Blueprint, request, jsonify
from bookings.services import BookingService
from bookings.schemas import BookingCreateSchema
from auth.guards import login_required
from core.exceptions import OdyssException

bookings_bp = Blueprint("bookings", __name__)

@bookings_bp.route("", methods=["POST"])
@login_required
def create_booking(current_user):
    try:
        schema = BookingCreateSchema()
        data = schema.load(request.get_json())
        booking = BookingService.create_booking(data, current_user)
        return jsonify({"message": "Booking created", "booking": booking.to_dict()}), 201
    except Exception as e:
        raise OdyssException(str(e), 400)