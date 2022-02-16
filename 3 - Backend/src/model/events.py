#!/usr/bin/env python

from enum import Enum


class Event(Enum):
    SENSOR_UP = 1
    SENSOR_DOWN = 2
    SENSOR_SHUTDOWN = 3
    INTRUDER = 4
    USER_NOTIFIED = 5


class Events(object):
    def __init__(self, created_at, event: Event, sensor, id=None):
        self.id = id
        self.created_at = created_at
        self.event = event
        self.sensor = sensor

    def get_sql_values(self):
        return [self.created_at, self.event, self.sensor]

    def get_values(self):
        return [self.id, self.created_at, self.event, self.sensor]