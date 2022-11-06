from flask import Blueprint, jsonify, request
from app.models import Service
import datetime

services = Blueprint('services', __name__)


@services.route('/', methods=['GET'])
def query_services():
    try:
        service = Service.get_all()

        return jsonify(service)
    except:
        return jsonify("Error")


@services.route('/', methods=['POST'])
def create_service():
    content = request.json
    try:
        service = Service(content["service_name"])
        service.save()
        return jsonify({"success": True, "created": content})
    except:
        return jsonify("error")


@services.route('/<int:uid>', methods=['PUT'])
def update_service(uid):
    content = request.json
    try:
        service = Service.get_by_id(uid)
        service.service_name = content["service_name"]
        service.save()
        content["id"] = uid
        return jsonify({"success": True, "updated": content})
    except:
        return jsonify("Error: No service found with that ID")


@services.route('/<int:uid>', methods=['DELETE'])
def delete_service(uid):
    try:
        if Service.delete_by_id(uid):
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "Error": "No service found with that ID"})
    except:
        return jsonify("Error")
