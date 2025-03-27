# docker-compose-psql

docker compose で開発用 PostgreSQL を動かすサンプルコード。

Python 3.12。

## 注意

### .env

このレポジトリには .env が含まれていますが、
本番(?)では .gitignore に記述して除外したほうがいい場合もありそう。

### psycopg2-binary

[psycopg2-binary](https://pypi.org/project/psycopg2-binary/) を使っています(サンプルだから)。
[psycopg2](https://pypi.org/project/psycopg2/)
を使うべき場合もあるので、ご注意ください。

## 実行

uv + Poe the Poet (uv と poe はプロジェクトに含まれてません)。

```sh
uv sync
poe up				# PostgreSQL起動。最初の1回だけ init.sqlが実行される
poe version		# PostgreSQLのバージョン表示
poe select
poe insert
poe insert3
poe select
poe delete		# userテーブル全部消し & バキューム
poe down

# その他
poe log				# PostgreSQLのログ表示
poe clean			# PostgreSQLを停止して、composeで使っていたボリュームも消す
```
