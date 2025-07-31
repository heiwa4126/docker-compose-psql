import psycopg2

from docker_compose_psql.env import connect_param


def connect():
    conn = psycopg2.connect(**connect_param)
    conn.autocommit = False
    return conn
