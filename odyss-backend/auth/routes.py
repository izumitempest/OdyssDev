from flask import Blueprint, request, jsonify
from auth.services import AuthService
from core.exceptions import OdyssException

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        response, status = AuthService.register(email, password)
        return jsonify(response), status
    except Exception as e:
        raise OdyssException(str(e), 400)

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        response, status = AuthService.login(email, password)
        return jsonify(response), status
    except Exception as e:
        raise OdyssException(str(e), 400)