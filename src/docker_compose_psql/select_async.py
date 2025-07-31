from docker_compose_psql.connect_async import connect_async


async def main():
    connection = None
    try:
        connection = await connect_async()

        record = await connection.fetch("SELECT * from users;")
        for row in record:
            print(row)

    except Exception as e:
        print("Error:", e)

    finally:
        # 接続を閉じる
        if connection:
            await connection.close()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main(), debug=True)
