# script-crawler

めも

- タグ名が同一であるかにかかわらず、同一階層にあるすべてのタグリストに対して処理をする。その際、同一であれば番号を振っていく。

- 訪れたことのあるノードは再訪問しないようにするロジックが必要

再訪問ロジックを組み込む前まではこれで対応できるがダサい

```
$ python3 list-up-xpath-mash-up.py test-ng.html | sort | uniq >a
```

得られたパスから対象ノード取得するには以下でいける文字コードをいい感じに。

普段とイメージが異なるが、うまく行くのはこのパターンだった

ラテン系に戻すと読めるようになる

```
$ cat test-ng.html| xmllint --html --xpath '/html/body/article/div/div/div[1]/div[1]/div/div/div[1]' - 2>/dev/null |iconv -f UTF-8 -t iso-8859-1
```


XPATHで指定したDOMのポジション位置X座標とY座標を記憶しておき、相対位置付近をクリックして求めたXPATHをつかってテキストを抽出し、抽出パタンにマッチするかどうか判定する

相対位置は各抽出項目ごとに上下左右の距離を管理しておくと実現できると思う

プログラムで起動したブラウザのXPATHを調べること

Qt等でウェブブラウザ機能を持つアプリを立ち上げる

nodeであるらしいので、そっち試すpuppeteer

- https://qiita.com/tomi_linka/items/a68cf7840c3da002c6e0

- https://www.youtube.com/watch?v=j1FQ0IsLpEg&list=LLSY1WsXXQAPCUNSm7SocZcQ&index=2

- https://stackoverflow.com/questions/52656526/how-to-insert-a-web-browser-in-python-qt-designer

- https://www.youtube.com/watch?v=8dImqP_JR-c

- youtube.com/watch?v=nnLkf5UK0cg

ユーザーがURLを指定する

指定したURLに遷移する

htmlファイルをはじめとするキャッシュファイル等をアプリ側で管理する

アプリ側で管理したhtmlファイルにnodejsのユーザークリックした項目のXPATHを取得するようなスクリプトを埋め込む

項目をクリック後、クリック名とXPATHをファイルに書き出す（JSONファイル）

seleniumで指定した項目を抜き出す

リンクの再帰処理が必要な気がする
