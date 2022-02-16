#!/usr/bin/env python

import os
from dotenv import load_dotenv
import pymysql

DATABASE_NAME = 'sensors'
USERS = 'users'
PROPERTIES = 'properties'
SENSORS = 'sensors'
EVENTS = 'events'


def init_database():
    try:
        load_dotenv()

        user = os.getenv('USERNAME')
        pwd = os.getenv('PASSWD')

        cursor = pymysql.connect(user=user, password=pwd).cursor()
        create_database(cursor)
        create_users_table(cursor)
        create_properties_table(cursor)
        create_sensors_table(cursor)
        create_events_table(cursor)
        return True
    except Exception as e:
        print(f'Error executing creation of database due to: [{e}]')
        return False


def create_database(cursor):
    db = cursor.execute(f"SHOW DATABASES LIKE '{DATABASE_NAME}';")
    if db <= 0:
        print(f"Database {DATABASE_NAME} don't exists, so I'll create this.")
        cursor.execute(f"CREATE DATABASE {DATABASE_NAME};")
    cursor.execute(f"USE {DATABASE_NAME};")


def create_users_table(cursor):
    sql = f"""
    CREATE TABLE `{USERS}` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `created_at` datetime NOT NULL,
      `cpf` varchar(11) NOT NULL,
      `fullname` text NOT NULL,
      `email` text NOT NULL,
      `phone` bigint(20) unsigned,
      `removed` datetime DEFAULT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `users_cpf` (`cpf`),
      KEY `users_id_IDX` (`id`) USING BTREE,
      KEY `users_cpf_IDX` (`cpf`) USING BTREE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """

    create_if_necessary(cursor, USERS, sql)


def create_sensors_table(cursor):
    sql = f"""
    CREATE TABLE `{SENSORS}` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `created_at` datetime NOT NULL,
      `property` int(11) NOT NULL,
      `description` text DEFAULT NULL,
      `removed` datetime DEFAULT NULL,
      PRIMARY KEY (`id`),
      KEY `sensors_id_IDX` (`id`) USING BTREE,
      CONSTRAINT `property_FK` FOREIGN KEY (`property`) REFERENCES `properties` (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """
    create_if_necessary(cursor, SENSORS, sql)


def create_properties_table(cursor):
    sql = f"""
        CREATE TABLE `{PROPERTIES}` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `created_at` datetime NOT NULL,
          `cep` varchar(8) NOT NULL,
          `street` text NOT NULL,
          `neighborhood` text NOT NULL,
          `city` text NOT NULL,
          `state` text NOT NULL,
          `country` text NOT NULL,
          `number` int(11) NOT NULL,
          `complement` text DEFAULT NULL,
          `user` int(11) NOT NULL,
          `removed` datetime DEFAULT NULL,
          PRIMARY KEY (`id`),
          KEY `sensors_id_IDX` (`id`) USING BTREE,
          CONSTRAINT `user_FK` FOREIGN KEY (`user`) REFERENCES `users` (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
    create_if_necessary(cursor, PROPERTIES, sql)


def create_events_table(cursor):
    sql = f"""
            CREATE TABLE `{EVENTS}` (
              `id` int(11) NOT NULL AUTO_INCREMENT,
              `created_at` datetime NOT NULL,
              `event` int(11) NOT NULL,
              `sensor` int(11) NOT NULL,
              `removed` datetime DEFAULT NULL,
              PRIMARY KEY (`id`),
              KEY `event_id_IDX` (`id`) USING BTREE,
              CONSTRAINT `sensor_FK` FOREIGN KEY (`sensor`) REFERENCES `sensors` (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
            """
    create_if_necessary(cursor, EVENTS, sql)


def create_if_necessary(cursor, table, sql):
    result = cursor.execute(f"SHOW TABLES LIKE '{table}';")
    if result <= 0:
        print(f"Table {table} don't exists, so I'll create then.")
        cursor.execute(sql)
