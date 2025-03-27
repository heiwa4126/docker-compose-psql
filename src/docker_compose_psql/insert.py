import random
import string

from docker_compose_psql.env_config import connect

try:
    # PostgreSQL に接続
    connection = connect()
    cursor = connection.cursor()

    # ランダムな名前とメールアドレスを生成
    random_name = "".join(random.choices(string.ascii_letters, k=8))
    random_email = f"{random_name.lower()}@example.com"
    data_to_insert = (random_name, random_email)

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
