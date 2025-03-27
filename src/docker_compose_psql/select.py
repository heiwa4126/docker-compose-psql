from docker_compose_psql.env_config import connect

try:
    # PostgreSQL に接続
    connection = connect()
    cursor = connection.cursor()

    # クエリを実行
    cursor.execute("SELECT * from users;")

    # 結果を表示
    for row in cursor.fetchall():
        print(row)

except Exception as e:
    print("Error:", e)

finally:
    # 接続を閉じる
    if "cursor" in locals():
        cursor.close()
    if "connection" in locals():
        connection.close()
