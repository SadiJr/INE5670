#!/usr/bin/env python

import os
from dotenv import load_dotenv
import pymysql

DATABASE_NAME = 'sensors'


class BasicQueries(object):
    def __init__(self):
        load_dotenv()

        user = os.getenv('USERNAME')
        pwd = os.getenv('PASSWD')

        self.cursor = pymysql.connect(user=user, password=pwd).cursor()

    def list_by_id(self, table, id):
        self.cursor.execute(f"USE {DATABASE_NAME};")
        result = self.cursor.execute(f"SELECT * FROM {table} WHERE id = {id};")
        if result <= 0:
            return f"Object with id {id} don't exists!", False
        elif result > 1:
            return f"Found more than one object with id {id}. Please contact the IT support!", False
        return self.cursor.fetchall(), True

    def list_all(self, table):
        self.cursor.execute(f"USE {DATABASE_NAME};")
        result = self.cursor.execute(f"SELECT * FROM {table};")
        if result <= 0:
            return f"Can't find any data!!!", False
        return self.cursor.fetchall(), True

    def remove_by_id(self, table, id):
        self.cursor.execute(f"USE {DATABASE_NAME};")
        result = self.cursor.execute(f"SELECT * FROM {table} WHERE id = {id};")
        if result <= 0:
            return f"Object with id {id} don't exists!", False
        try:
            if self.cursor.execute(f"DELETE FROM {table} WHERE id = {id};"):
                self.cursor.connection.commit()
                return "Object deleted with success", True
            else:
                return f"Failed to delete object. Please contact the IT team.", False
        except Exception as e:
            print(f"Failed to delete id {id} from table {table} due to {e}.")
            return "Internal error trying to delete object. Please contact the IT team.", False

    def get_cursor(self):
        return self.cursor
