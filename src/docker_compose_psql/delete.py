from docker_compose_psql.connect import connect

try:
    # PostgreSQL に接続
    connection = connect()
    cursor = connection.cursor()

    # usersテーブルを全削除
    cursor.execute("DELETE FROM users;")
    cursor.execute("END TRANSACTION;")  # commitだとvacuumがエラーになる。
    # connection.commit()

    # バキューム処理
    cursor.execute("VACUUM;")

except Exception as e:
    print("Error:", e)

finally:
    # 接続を閉じる
    if "cursor" in locals():
        cursor.close()
    if "connection" in locals():
        connection.close()
