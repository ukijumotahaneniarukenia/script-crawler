事前準備

https://pypi.org/project/termcolor/

```
pip3 install --user termcolor

pip3 install --user requests

pip3 install --user lxml

pip3 install --user bs4

pip3 install --user selenium
```


ページダウンロードし、リンク作成

CMD

```
$ time ./wrapper-prev-execute.sh
```

OUT

```
real	3m3.840s
user	0m8.204s
sys	0m2.513s
```

コンテンツ抽出

CMD


```
$ time ./wrapper-main-execute.sh
```


OUT

```

```


前回アクセスURLリストの作成

CMD

```
$ time ./wrapper-post-execute.sh
```

OUT

```

```

ないよーん

これが現れる場合はアプリで起動したブラウザ上でのXPATHを正しく指定できていないため

あるいは指定したページに対するXPATHを正しく定義できていないため

ユーザーが意図して起動する場合と少し異なる

メンテが必要

ここをうまくやりたい

```
$ ./mock.py 'https://qiita.com/yamaru/items/527ca7d814534beca56a'
```

起動してxpath確認してlist.jsonにパターン追加


下スクロールの場合

```
$ ./mock-scroll.py 'https://dev.to/t/react'
```
