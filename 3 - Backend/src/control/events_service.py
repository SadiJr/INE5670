from utils import basic_db_operations

EVENTS = "events"

connector = basic_db_operations.BasicQueries()


def sensor_event(body):
    pass


def list_event(id):
    return connector.list_by_id(EVENTS, id)


def list_all():
    return connector.list_all(EVENTS)