# docker-load-test

負荷テストを行うヤツ

# 概要

- OSS の負荷テストツール [Locust](https://locust.io/) を利用
- Docker で起動、ブラウザで設定をして負荷テストを実施
- 結果をブラウザで確認できる

# How to Use

```
docker-compose up --scale worker=1
```

ブラウザより `http://localhost:8089` にアクセス

止める場合

`ctrl+c`

# configure

`src/locustfile.py` を編集することでテストシナリオを書くことができる。
宛先パスなどもここで。

# ref

[Runnning in Docker - Locast](https://docs.locust.io/en/stable/running-in-docker.html)

[参考](https://blog.future.ad.jp/%E8%B2%A0%E8%8D%B7%E3%83%86%E3%82%B9%E3%83%88%E3%83%84%E3%83%BC%E3%83%ABlocust%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F)
