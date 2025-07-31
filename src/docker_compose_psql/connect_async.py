import asyncpg

from docker_compose_psql.env import connect_param


async def connect_async():
    conn = await asyncpg.connect(**connect_param)
    return conn
