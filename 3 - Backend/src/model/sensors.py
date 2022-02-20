#!/usr/bin/env python

import uuid


class Sensors(object):
    def __init__(self, created_at, property, description=None, id=None):
        self.id = id
        self.created_at = created_at
        self.property = property
        self.description = description

    def get_sql_values(self):
        return [self.created_at, self.property, self.description]

    def get_values(self):
        return [self.id, self.created_at, self.property, self.description]