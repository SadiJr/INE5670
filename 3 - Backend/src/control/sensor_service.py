from utils import crud
from model.sensors import Sensors
import jsons
from datetime import datetime

DATABASE_NAME = 'sensors'
SENSORS = "sensors"
PROPERTIES = "properties"
connector = crud.Crud()
KEYS = ['property']


def list_sensor(id):
    result, success = connector.list_by_id(SENSORS, id)
    if not success:
        return result, success
    result = jsons.dump(Sensors(result[1], result[2], description=result[3], id=result[0]))
    return result, success


def list_all():
    sensors = []
    result, success = connector.list_all(SENSORS)
    if success:
        for u in result:
            sensors.append(jsons.dump(Sensors(u[1], u[2], description=u[3], id=u[0])))
        return sensors, True
    return result, success


def add_sensor(data):
    data = dict((k.lower(), v) for k, v in data.items())

    if not all(key in data for key in KEYS):
        return f"There are missing values! Can't finish the new sensor registration. Make sure the values {KEYS} are " \
               f"in the request.", False

    property = data.get('property')
    if type(property) is not int:
        return f"You need to pass the id of the property to which this sensor belongs!", False

    description = data.get('description')

    result, success = connector.list_by_id(PROPERTIES, property)
    if not success:
        return f"Can't find any property with id {property}!", False
    sensor = Sensors(datetime.now(), property, description=description)
    return insert_sensor(sensor.get_sql_values())


def edit_sensor(data):
    # TODO
    return "Not implemented yet", False


def remove_sensor(id):
    return connector.remove_by_id(SENSORS, id)


def insert_sensor(values):
    try:
        sql = f"INSERT INTO {SENSORS} (created_at, property, description) VALUES (%s, %s, %s);"
        connector.get_cursor().execute(f"USE {DATABASE_NAME};")
        connector.get_cursor().execute(sql, values)
        connector.get_cursor().connection.commit()
        return "Sensor added with success", True
    except IntegrityError as e:
        print(f"Error in MySQL insert: {e}")
        return f"Error in insert sensor due to {e}!", False