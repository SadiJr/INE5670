#!/usr/bin/env python

class User(object):
    def __init__(self, created_at, cpf, full_name, email, cellphone, id=None):
        self.id = id
        self.created_at = created_at
        self.cpf = cpf
        self.full_name = full_name
        self.email = email
        self.cellphone = cellphone

    def get_sql_values(self):
        return [self.created_at, self.cpf, self.full_name, self.email, self.cellphone]

    def get_values(self):
        return [self.id, self.created_at, self.cpf, self.full_name, self.email, self.cellphone]