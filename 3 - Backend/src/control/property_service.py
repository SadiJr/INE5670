from utils import crud

PROPERTIES = "properties"

connector = crud.Crud()


def list_property(id):
    return connector.list_by_id(PROPERTIES, id)


def list_all():
    return connector.list_all(PROPERTIES)


def add_property(data):
    pass


def edit_property(data):
    # TODO
    return "Not implemented yet", False


def remove_property(id):
    return connector.remove_by_id(id)