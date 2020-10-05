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

項目数が正しいデータ行のみ抽出

```
$ cat page-content-to-dev.tsv | awk -v FS='\t' 'NF==8{for(i=1;i<=NF;i++){printf $i"\t"}printf "\n"}' | sed -r 's/\t$//' >page-content-to-dev.tsv.success.tsv
```

項目数が正しくないデータ行のみ抽出

```
$ cat page-content-to-dev.tsv | awk -v FS='\t' 'NF!=8{for(i=1;i<=NF;i++){printf $i"\t"}printf "\n"}' | sed -r 's/\t$//' >page-content-to-dev.tsv-fail.tsv
```

存在チェック用のURLリストを抽出

前回成功時のURLに関してはアクセスしないロジックを組むために必要

```
$ cat page-content-to-dev.tsv.success.tsv | awk -v FS='\t' '$0=$1' | tail -n+2 | sort | uniq >page-content-to-dev.tsv-success-url.txt
```

前回失敗時のURLに関してはアクセスしないロジックを組むために必要


```
$ cat page-content-to-dev.tsv-fail.tsv | awk -v FS='\t' '$0=$1' | tail -n+2 | sort | uniq | grep -P 'https?' | sort | uniq >page-content-to-dev.tsv-fail-url.txt
```

上記２つのファイルをマージ


```
$ ls page-content-to-dev.tsv-fail-url.txt page-content-to-dev.tsv-success-url.txt | xargs cat | sort | uniq | jq -R '' | jq -s '' >page-content-to-dev-no-need-access-url.json
```

ないよーん

これが現れる場合はアプリで起動したブラウザ上でのXPATHを正しく指定できていないため

ユーザーが意図して起動する場合と少し異なる

```
$ ./mock.py 'https://qiita.com/yamaru/items/527ca7d814534beca56a'
```

起動してxpath確認してlist.jsonにパターン追加


下スクロールの場合

```
$ ./mock-scroll.py 'https://dev.to/t/react'
```
