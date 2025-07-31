from docker_compose_psql.connect_async import connect_async
from docker_compose_psql.utils import generate_random_user_data


async def insert_data():
    connection = None
    try:
        # PostgreSQL に非同期接続
        connection = await connect_async()

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
