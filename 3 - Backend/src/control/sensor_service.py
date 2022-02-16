from utils import basic_db_operations

SENSORS = "sensors"

connector = basic_db_operations.BasicQueries()


def list_sensor(id):
    return connector.list_by_id(SENSORS, id)


def list_all():
    return connector.list_all(SENSORS)


def add_sensor(body):
    pass


def edit_sensor(body):
    pass


def remove_sensor(id):
    pass