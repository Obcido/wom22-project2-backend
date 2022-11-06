from flask import Blueprint, jsonify, request
from app.models import Order
import datetime

orders = Blueprint('orders', __name__)


@orders.route('/', methods=['GET'])
def query_orders():
    try:
        order_list = Order.get_all()
        return jsonify(order_list)
    except:
        return jsonify("Error")


@orders.route('/', methods=['POST'])
def create_order():
    content = request.json
    try:
        order = Order(content["cabin"], content["service_name"], datetime.date.today())
        order.save()
        return jsonify({"success": True, "created": content})
    except:
        return jsonify("error")


@orders.route('/<int:uid>', methods=['PUT'])
def update_order(uid):
    content = request.json
    try:
        order = Order.get_by_id(uid)
        order.cabin = content["cabin"]
        order.service_name = content["service_name"]
        order.save()
        content["id"] = uid
        return jsonify({"success": True, "updated": content})
    except:
        return jsonify("Error: No order found with that ID")


@orders.route('/<int:uid>', methods=['DELETE'])
def delete_order(uid):
    try:
        if Order.delete_by_id(uid):
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "Error": "No order found with that ID"})
    except:
        return jsonify("Error")
