# atcoder

atcoder のソースコード置き場

ディレクトリ構成はこちらを参考にした
https://qiita.com/chokoryu/items/4b31ffb89dbc8cb86971

## oj の使い方

```
$ poetry run oj login -u {ユーザー名} -p {パスワード} "https://atcoder.jp/"
```

- problems/abc{回数}\_{難易度} のような python ファイルを作成
  - example: abc313_a.py
- shift + ctrl + b = サンプルテストケースでのテスト
- F5 = input.txt による手動入力

## ブログテンプレートの生成方法

```
$ python makeBlog.py -d abc170
```
