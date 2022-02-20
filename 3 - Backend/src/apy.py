#!/usr/bin/env python

from control import user_service, sensor_service, events_service, property_service
from flask import Flask, json, request, jsonify, send_file, Response
from utils import init_db
import json

app = Flask(__name__)


@app.route("/routes", methods=["GET"])
def get_routes():
    routes = {}
    for r in app.url_map._rules:
        routes[r.rule] = {}
        routes[r.rule]["functionName"] = r.endpoint
        routes[r.rule]["methods"] = list(r.methods)

    routes.pop("/static/<path:filename>")

    return jsonify(routes)


@app.route('/property/list/<int:id>', methods=['GET'])
def list_property(id):
    msg, success = property_service.list_property(id)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/property/list/all', methods=['GET'])
def list_all_properties():
    msg, success = property_service.list_all()
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/property/add', methods=['POST'])
def add_property():
    data = request.json
    msg, success = property_service.add_property(data)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/property/edit', methods=['POST'])
def edit_property():
    data = request.json
    msg, success = property_service.edit_property(data)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/property/remove/<int:id>', methods=['GET'])
def remove_property(id):
    msg, success = property_service.remove_property(id)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/sensor/list/<int:id>', methods=['GET'])
def list_sensor(id):
    msg, success = sensor_service.list_sensor(id)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/sensor/list/all', methods=['GET'])
def list_all_sensors():
    msg, success = sensor_service.list_all()
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/sensor/event', methods=['POST'])
def sensor_event():
    data = request.json
    msg, success = events_service.sensor_event(data)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/sensor/add', methods=['POST'])
def add_sensor():
    data = request.json
    msg, success = sensor_service.add_sensor(data)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/sensor/edit', methods=['POST'])
def edit_sensor():
    data = request.json
    msg, success = sensor_service.edit_sensor(data)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/event/list/<int:id>', methods=['GET'])
def list_event(id):
    msg, success = events_service.list_event(id)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/event/list/all', methods=['GET'])
def list_all_events():
    msg, success = events_service.list_all()
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/sensor/remove/<int:id>', methods=['GET'])
def remove_sensor(id):
    msg, success = sensor_service.remove_sensor(id)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/user/list/<int:id>', methods=['GET'])
def list_user(id):
    msg, success = user_service.list_user(id)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/user/list/all', methods=['GET'])
def list_all_users():
    msg, success = user_service.list_all()
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/user/add', methods=['POST'])
def add_user():
    data = request.json
    msg, success = user_service.add_user(data)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/user/edit', methods=['POST'])
def edit_user():
    data = request.json
    msg, success = user_service.edit_user(data)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


@app.route('/user/remove/<int:id>', methods=['GET'])
def remove_user(id):
    msg, success = user_service.remove_user(id)
    resp = jsonify({'message': msg})
    resp.status_code = 200 if success else 400
    return resp


if __name__ == '__main__':
    try:
        init_db.init_database()
        app.run(port=8082, debug=True)
    except Exception as e:
        print(f"Exception is {e},")
