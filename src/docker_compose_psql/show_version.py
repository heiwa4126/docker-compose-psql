import docker_compose_psql.connect as connect

try:
    # PostgreSQL に接続
    connection = connect.connect()
    cursor = connection.cursor()

    # クエリを実行
    cursor.execute("SELECT version();")
    version = cursor.fetchone()

    # 結果を表示
    print("PostgreSQL version:", version[0])

except Exception as e:
    print("Error:", e)

finally:
    # 接続を閉じる
    if "cursor" in locals():
        cursor.close()
    if "connection" in locals():
        connection.close()
