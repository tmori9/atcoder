# atcoder

atcoder のソースコード置き場

ディレクトリ構成はこちらを参考にした
https://qiita.com/chokoryu/items/4b31ffb89dbc8cb86971

## oj の使い方

```
$ poetry run oj login -u {ユーザー名} -p {パスワード} "https://atcoder.jp/"
```

- shift + ctrl + b = サンプルテストケースでのテスト
- F5 = input.txt による手動入力

## ブログテンプレートの生成方法

```
$ python makeBlog.py -d abc170
```
