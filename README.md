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


自動制御する場合としない場合、SPAかSPAじゃないかの場合でXPATHに相関あるかないか気付けるか


- https://askubuntu.com/questions/763612/importerror-no-module-named-pyqt5-qtwebenginewidgets
```
Traceback (most recent call last):
  File "mybrowser.py", line 77, in <module>
    from PyQt5 import QtWebKitWidgets
ImportError: cannot import name 'QtWebKitWidgets' from 'PyQt5' (/usr/local/lib/python3.7/site-packages/PyQt5/__init__.py)

```

```
$ sudo apt install python3-pyqt5.qtwebengine

$ sudo pip3 install PyQtWebEngine

$ pip3 uninstall PyQt5


$ pip3 uninstall PyQtWebEngine


$ pip3 install PyQt5==5.13

$ pip3 install PyQtWebEngine

```
