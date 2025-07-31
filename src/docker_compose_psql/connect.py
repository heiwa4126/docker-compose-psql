import psycopg2

from docker_compose_psql.env import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


def connect():
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )
    conn.autocommit = False
    return conn
