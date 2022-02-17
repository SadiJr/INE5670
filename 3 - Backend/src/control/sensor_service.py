from utils import crud

SENSORS = "sensors"

connector = crud.Crud()


def list_sensor(id):
    return connector.list_by_id(SENSORS, id)


def list_all():
    return connector.list_all(SENSORS)


def add_sensor(body):
    pass


def edit_sensor(body):
    # TODO
    return "Not implemented yet", False


def remove_sensor(id):
    return connector.remove_by_id(SENSORS, id)