#!/usr/bin/env python

from utils import crud
from utils import event_utils
from model.events import Events
from model.events import Event
from datetime import datetime
import jsons

DATABASE_NAME = 'sensors'
EVENTS = "events"
SENSORS = 'sensors'
KEYS = ['event', 'sensor']
connector = crud.Crud()


def sensor_event(data):
    data = dict((k.lower(), v) for k, v in data.items())

    if not all(key in data for key in KEYS):
        return f"There are missing values! Can't finish the sensor event registration. Make sure the values {KEYS} are " \
               f"in the request.", False

    sensor = data.get('sensor')
    creation_date = data.get('created_at')
    created_at = creation_date if creation_date is not None else datetime.now()
    event = data.get('event')

    if type(sensor) is not int:
        return f"The id {sensor} of the sensor is not a int!", False

    result, success = connector.list_by_id(SENSORS, sensor)
    if not success:
        return f"Can't find any sensor with id {sensor}!", False

    event_data = None
    if type(event) is int and Event.has_value(event):
        event_data = Events(created_at, event, sensor)
    elif type(event) is str and Event.has_key(event):
        event_data = Events(created_at, Event[event].value, sensor)
    else:
        return f"The event informed is not valid!", False

    result, success = insert_event(event_data.get_sql_values())

    if event_data.event is Event.INTRUDER.value:
        event_utils.simulate_send(event_data.sensor)

    return result, success


def list_event(id):
    result, success = connector.list_by_id(EVENTS, id)
    if not success:
        return result, success
    result = jsons.dump(Events(result[1], result[2], result[3], id=result[0]))
    return result, success


def list_all():
    events = []
    result, success = connector.list_all(EVENTS)
    if success:
        for u in result:
            events.append(jsons.dump(Events(u[1], u[2], u[3], id=u[0])))
        return events, True
    return result, success


def insert_event(values):
    try:
        sql = f"INSERT INTO {EVENTS} (created_at, event, sensor) VALUES (%s, %s, %s);"
        connector.get_cursor().execute(f"USE {DATABASE_NAME};")
        connector.get_cursor().execute(sql, values)
        connector.get_cursor().connection.commit()
        return "Event added with success", True
    except Exception as e:
        print(f"Error in MySQL insert: {e}")
        return f"Error in insert sensor event due to {e}!", False
