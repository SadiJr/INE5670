from utils import basic_db_operations

PROPERTIES = "properties"

connector = basic_db_operations.BasicQueries()


def list_property(id):
    return connector.list_by_id(PROPERTIES, id)


def list_all():
    return connector.list_all(PROPERTIES)


def add_property(body):
    pass


def edit_property(body):
    pass


def remove_property(id):
    pass