from utils import basic_db_operations
from utils import user_utils
from model.users import User
from datetime import datetime
from pymysql import err,IntegrityError as IntegrityError
import jsons
import re

DATABASE_NAME = 'sensors'
USERS = "users"
KEYS = ['cpf', 'fullname', 'email', 'phone']
connector = basic_db_operations.BasicQueries()


def list_user(id):
    result, success = connector.list_by_id(USERS, id)
    if not success:
        return result, success
    result = result[0]
    result = jsons.dump(User(result[1], result[2], result[3], result[4], result[5], result[6], id=result[0]))
    return result, success

def list_all():
    users = []
    result, success = connector.list_all(USERS)
    if success:
        for u in result:
            users.append(jsons.dump(User(u[1], u[2], u[3], u[4], u[5], u[6], id=u[0])))
        return users, True
    return result, success

def add_user(data: dict) -> {str, bool}:
    data = dict((k.lower(), v) for k, v in data.items())

    if not all(key in data for key in KEYS):
        return f"There are missing values! Can't finish the new user registration. Make sure the values {KEYS} are " \
               f"in the request.", False

    cpf = data.get('cpf')
    email = data.get('email')
    phone = str(data.get('phone'))

    result = validate_data(cpf, email, phone)
    if result is not None:
        return result

    cpf = cpf.replace('.', '').replace('-', '')
    phone = int(re.sub("[^0-9]", "", phone))
    name = data.get('fullname')

    user = User(datetime.now(), cpf, name, email, phone, None)
    return insert_user(user.get_sql_values())

def validate_data(cpf, email, phone):
    if not user_utils.validate_cpf(cpf):
        return f"The CPF {cpf} isn't valid! Try again with an valid CPF.", False

    if not user_utils.validate_email(email):
        return f"The e-mail {email} isn't valid! Try again with a valid e-mail.", False

    if not user_utils.validate_phone(phone):
        return f"The phone {phone} isn't valid! Try again with a valid phone number.", False
    return None

def edit_user(data: dict) -> {str, bool}:
    return "Not implemented yet", False


def remove_user(id: int) -> bool:
    return connector.remove_by_id(USERS, id)

def insert_user(values):
    try:
        sql = f"INSERT INTO {USERS} (created_at, cpf, fullname, email, phone, removed) VALUES (%s, %s, %s ,%s ,%s ,%s);"
        connector.get_cursor().execute(f"USE {DATABASE_NAME};")
        connector.get_cursor().execute(sql, values)
        connector.get_cursor().connection.commit()
        return "User added with success", True
    except IntegrityError as e:
        print(f"Error in MySQL insert: {e}")
        return f"User with this CPF already exists!", False

