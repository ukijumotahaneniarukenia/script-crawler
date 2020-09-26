# script-crawler
汎用クローラに昇華させたい（ふり）

プログラムで起動したブラウザのXPATHを調べること

Qt等でウェブブラウザ機能を持つアプリを立ち上げる

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
