import asyncpg

from docker_compose_psql.connect import connect
from docker_compose_psql.utils import generate_random_user_data


async def insert_data():
    connection = None
    try:
        # PostgreSQL に非同期接続
        connection = await asyncpg.connect(
            host="localhost",
            database="your_database",
            user="your_user",
            password="your_password",
        )

        data_to_insert = generate_random_user_data()

        # データを挿入
        insert_query = "INSERT INTO users (name, email) VALUES ($1, $2);"
        await connection.execute(insert_query, *data_to_insert)

    except Exception as e:
        print("Error:", e)

    finally:
        # 接続を閉じる
        if connection:
            await connection.close()


if __name__ == "__main__":
    import asyncio

    asyncio.run(insert_data())
