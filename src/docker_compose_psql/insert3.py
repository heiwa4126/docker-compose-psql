from docker_compose_psql.env_config import connect
from docker_compose_psql.utils import generate_random_user_data

try:
    # PostgreSQL に接続
    connection = connect()
    cursor = connection.cursor()

    # ランダムな名前とメールアドレスを生成する関数を呼び出し
    data = [generate_random_user_data() for _ in range(3)]

    # データを挿入
    insert_query = "INSERT INTO users (name, email) VALUES (%s, %s);"
    cursor.executemany(insert_query, data)
    connection.commit()

except Exception as e:
    print("Error:", e)

finally:
    # 接続を閉じる
    if "cursor" in locals():
        cursor.close()
    if "connection" in locals():
        connection.close()
