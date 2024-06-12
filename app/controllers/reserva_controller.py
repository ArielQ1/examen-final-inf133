from flask import Blueprint, request, jsonify
from app.models.reserva_model import Reserva
from app.views.reserva_view import render_reserva_detail, render_reserva_list
from app.utils.decorators import jwt_required, role_required


reserva_bp = Blueprint("reserva", __name__)


@reserva_bp.route("/reservations", methods=["GET"])
@jwt_required
@role_required("admin")
def get_reserva():
    reservas = Reserva.get_all()
    return jsonify(render_reserva_list(reservas))

@reserva_bp.route("/reservations/<int:id>", methods=["GET"])
@jwt_required
@role_required("admin")
def get_reserva(id):
    reserva = Reserva.get_by_id(id)
    if reserva:
        return jsonify(render_reserva_detail(reserva))
    return jsonify({"error":"Reserva no encontrado"}), 404

@reserva_bp.route("/reservations", methods=["POST"])
@jwt_required
@role_required("admin")
def create_reserva():
    data = request.json


    user_id = data.get("user_id")
    restaurante_id = data.get("restaurante_id")
    reservation_date = data.get("reservation_date")
    num_guests = data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")

    if not user_id or not restaurante_id or not reservation_date or not num_guests:
        return jsonify({"error":"Faltan datos requeridos"}), 400
       

    reserva = Reserva(user_id=user_id, restaurante_id=restaurante_id, reservation_date=reservation_date, num_guests=num_guests, special_requests=special_requests, status=status)
    reserva.save()
    return jsonify(render_reserva_detail(reserva)), 201


@reserva_bp.route("/reservations/<int:id>", methods=["PUT"])
@jwt_required
@role_required("admin")
def update_reserva(id):
    reserva = Reserva.get_by_id(id)
    if not reserva:
        return jsonify({"error":"Reserva no encontrado"}), 404
    
    data = request.json
    user_id = data.get("user_id")
    restaurante_id = data.get("restaurante_id")
    reservation_date = data.get("reservation_date")
    num_guests = data.get("num_guests")
    special_requests = data.get("special_requests")
    status = data.get("status")

    reserva.update()
    return jsonify(render_reserva_detail(reserva))

@reserva_bp.route("/reservations/<int:id>", methods=["DELETE"])
@jwt_required
@role_required("admin")
def delete_reserva(id):
    reserva = Reserva.get_by_id(id)
    if not reserva:
        return jsonify({"error":"Reserva no encontrado"}),404
    
    reserva.delete()

    return "", 204