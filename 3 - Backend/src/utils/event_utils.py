#!/usr/bin/env python

from utils import crud

SENSORS = "sensors"
PROPERTIES = "properties"
USERS = "users"

connector = crud.Crud()


def simulate_send(sensor):
    print("Simulating data send in intruder event!")
    result, success = connector.list_by_id(SENSORS, sensor)
    sensor_description = result[3]
    property_id = result[2]

    result, success = connector.list_by_id(PROPERTIES, property_id)
    cep = result[2]
    street = result[3]
    neighborhood = result[4]
    city = result[5]
    state = result[6]
    country = result[7]
    number = result[8]
    user_id = result[10]

    result, success = connector.list_by_id(USERS, user_id)

    cpf = result[2]
    username = result[3]
    email = result[4]
    phone = result[5]

    print(f"Simulate e-mail and SMS to user [name: {username}, CPF: {cpf}, email: {email}, phone: {phone}].")
    send_email(email, username, sensor_description, cep, street, neighborhood, city, state, country, number)
    send_sms(phone, username, sensor_description, cep, street, neighborhood, city, state, country, number)


def send_email(email, username, sensor_description, cep, street, neighborhood, city, state, country, number):
    msg = f"""
        Dear {username}.
            We receive a message from sensor [{sensor_description}] in the property [
                CEP: {cep},
                Street: {street}.
                Neighborhood: {neighborhood},
                City: {city},
                State: {state},
                Country: {country},
                Number: {number}
            ]
            about an possible intruder!!!
            
            Please call the policy, and go to a safe place.
            """
    print(f"Send email with content [\n\n[{msg}\n\n] to e-mail [{email}].")


def send_sms(phone, username, sensor_description, cep, street, neighborhood, city, state, country, number):
    msg = f"""
        Dear {username}.
            We receive a message from sensor [{sensor_description}] in the property [
                CEP: {cep},
                Street: {street}.
                Neighborhood: {neighborhood},
                City: {city},
                State: {state},
                Country: {country},
                Number: {number}
            ]
            about an possible intruder!!!

            Please call the policy, and go to a safe place.
            """
    print(f"Send SMS with content [\n\n{msg}]\n\n] to phone [{phone}].")

