# script-crawler
汎用クローラに昇華させたい（ふり）

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


こういうの便利

```
$ echo 'https://tabelog.com/kanagawa/rstLst/?vs=1&sa=%E7%A5%9E%E5%A5%88%E5%B7%9D%E7%9C%8C&sk=%25E7%2584%25BC%25E8%2582%2589&lid=top_navi1&vac_net=&svd=20200926&svt=1900&svps=2&hfc=1&Cat=RC&LstCat=RC13&LstCatD=RC1301&LstCatSD=RC130101&cat_sk=%E7%84%BC%E8%82%89' | jq -R 'split("&")'
[
  "https://tabelog.com/kanagawa/rstLst/?vs=1",
  "sa=%E7%A5%9E%E5%A5%88%E5%B7%9D%E7%9C%8C",
  "sk=%25E7%2584%25BC%25E8%2582%2589",
  "lid=top_navi1",
  "vac_net=",
  "svd=20200926",
  "svt=1900",
  "svps=2",
  "hfc=1",
  "Cat=RC",
  "LstCat=RC13",
  "LstCatD=RC1301",
  "LstCatSD=RC130101",
  "cat_sk=%E7%84%BC%E8%82%89"
]
```
