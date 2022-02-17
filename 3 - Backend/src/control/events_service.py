from utils import crud

EVENTS = "events"

connector = crud.Crud()


def sensor_event(data):
    pass


def list_event(id):
    return connector.list_by_id(EVENTS, id)


def list_all():
    return connector.list_all(EVENTS)