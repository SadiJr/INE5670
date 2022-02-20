#!/usr/bin/env python

from utils import crud
from model.properties import Properties
from datetime import datetime
import jsons

DATABASE_NAME = 'sensors'
PROPERTIES = "properties"
USERS = "users"
KEYS = ["cep", "street", "neighborhood", "city", "state", "country", "number", "user"]
USER_KEYS = ['cpf', 'fullname', 'email', 'phone']

connector = crud.Crud()


def list_property(id):
    result, success = connector.list_by_id(PROPERTIES, id)
    if not success:
        return result, success
    result = jsons.dump(Properties(result[1], result[2], result[3], result[4], result[5], result[6], result[7],
                                   result[8], result[9], result[10], id=result[0]))
    return result, success


def list_all():
    properties = []
    result, success = connector.list_all(PROPERTIES)
    if success:
        for u in result:
            properties.append(jsons.dump(Properties(u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9], u[10],
                                                    id=u[0])))
        return properties, True
    return result, success


def add_property(data):
    data = dict((k.lower(), v) for k, v in data.items())

    if not all(key in data for key in KEYS):
        return f"There are missing values! Can't finish the new property registration. Make sure the values {KEYS} " \
               f"are in the request.", False

    user_id = data.get('user')
    result, success = connector.list_by_id(USERS, user_id)
    if not success:
        return f"Can't find any user with id {user_id}!", False

    cep = data.get('cep')
    street = data.get('street')
    neighborhood = data.get('neighborhood')
    city = data.get('city')
    state = data.get('state')
    country = data.get('country')
    number = data.get('number')
    complement = data.get('complement')
    property = Properties(datetime.now(), cep, street, neighborhood, city, state, country, number, complement, user_id)
    return insert_property(property.get_sql_values())


def edit_property(data):
    # TODO
    return "Not implemented yet", False


def remove_property(id):
    return connector.remove_by_id(id)


def insert_property(values):
    try:
        sql = f"INSERT INTO {PROPERTIES} (created_at, cep, street, neighborhood, city, state, country, number, " \
              f"complement, user) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        connector.get_cursor().execute(f"USE {DATABASE_NAME};")
        connector.get_cursor().execute(sql, values)
        connector.get_cursor().connection.commit()
        return "Property added with success", True
    except Exception as e:
        print(f"Error in MySQL insert: {e}")
        return f"Can't add property due to {e}!", False
