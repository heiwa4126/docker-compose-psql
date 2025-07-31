from docker_compose_psql.connect import connect
from docker_compose_psql.utils import generate_random_user_data

try:
    # PostgreSQL に接続
    connection = connect()
    cursor = connection.cursor()

    data_to_insert = generate_random_user_data()

    # データを挿入
    insert_query = "INSERT INTO users (name, email) VALUES (%s, %s);"
    cursor.execute(insert_query, data_to_insert)
    connection.commit()

except Exception as e:
    print("Error:", e)

finally:
    # 接続を閉じる
    if "cursor" in locals():
        cursor.close()
    if "connection" in locals():
        connection.close()
