# docker-compose-psql

docker compose で開発用 PostgreSQL を動かすサンプルコード。

Python 3.12。コンテナは postgres:17([参照](https://hub.docker.com/_/postgres))

## 注意

### .env

このレポジトリには .env が含まれていますが、
本番(?)では .gitignore に記述して除外したほうがいい場合もありそう。

### psycopg2-binary

[psycopg2-binary](https://pypi.org/project/psycopg2-binary/) を使っています(サンプルだから)。
[psycopg2](https://pypi.org/project/psycopg2/)
を使うべき場合もあるので、ご注意ください。

## 実行

[uv](https://docs.astral.sh/uv/getting-started/installation/) +
[Poe the Poet](https://poethepoet.natn.io/index.html)
(uv と poe はプロジェクトに含まれてません)。

```sh
# 準備
uv sync
uv tool install poethepoet
# PostgreSQL起動。最初の1回だけ init.sqlが実行される
poe up
# PostgreSQLのログ表示 (tail -f的に)
poe log
# PostgreSQLのバージョン表示
poe version
# 以下 pythonを呼んでいろいろテスト
poe select
poe insert
poe insert3
poe select
# userテーブル全部消し & バキューム
poe delete
# PostgreSQL終了
poe down
# PostgreSQLを停止して、composeで使っていたボリュームも消す
poe clean
```

### psql 関連

`poe up` で起動したコンテナに接続して、
その中の psql からいろいろやるサンプルタスクをいくつか用意した。

```sh
# `select version();`
poe psql_ver3
# `select * from users;`
poe psql_select
# log_statement = 'all'にしてログに全クエリが出るようにする
poe log_all
# log_statement = 'none'にもどす
poe log_none
# psqlで入る
poe psql
# bashで入る
poe shell
```

[PostgreSQL 公式コンテナ](https://hub.docker.com/_/postgres)では
中の psql からは localhost は trust 認証なのでパスワード不要
の設定になっている
(`poe shell` して `less /var/lib/postgresql/data# less pg_hba.conf` してみて)。
