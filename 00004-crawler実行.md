事前準備

```
pip3 install --user requests

pip3 install --user lxml

pip3 install --user bs4

pip3 install --user selenium
```

サイト別カラムリストの一覧の作成

```
$ cat list.json | jq -cr '. as $in | $in | length as $cnt | [range(0;$cnt)]|foreach $in[.[]] as $item("";($item|(."SITE_URL"|gsub(".*//";"")|gsub("/.*";"")|split(".")|reverse|join("-")) + "\t" +($item|({"EXTRACT_COLUMN_LIST":(."EXTRACT_COLUMN_LIST"|keys)}|tojson))))'| while read base_name column_list;do echo $column_list > "extract-site-column-list-"$base_name".json";cat "extract-site-column-list-"$base_name".json"|jq '' |sponge "extract-site-column-list-"$base_name".json";done
```

ベースファイル名リストの作成

```
$ cat list.json | jq -r 'map(."SITE_URL")|join("\n")'>base-file-name-list.txt
```

ベースファイル名リストの正規化


```
$ cat base-file-name-list.txt | ruby -F'(?<=//)' -anle 'scheme=$F[0];domain=$F[1].split("/")[0]+"/";puts "#{scheme + domain}"' | sort | uniq | sponge base-file-name-list.txt
```


ページのダウンロード

```
$ time ./download-detail-page-spa.py
```

リンクの作成

```
$ time ./link-create.py
```


取得項目の抽出
```
$ time ./extract-page-content.py
```

項目数が正しいデータ行のみ抽出

```
$ cat page-content-to-dev.tsv | awk -v FS='\t' 'NF==8{for(i=1;i<=NF;i++){printf $i"\t"}printf "\n"}' | sed -r 's/\t$//' >page-content-to-dev.tsv.success.tsv
```

項目数が正しくないデータ行のみ抽出

```
$ cat page-content-to-dev.tsv | awk -v FS='\t' 'NF!=8{for(i=1;i<=NF;i++){printf $i"\t"}printf "\n"}' | sed -r 's/\t$//' >page-content-to-dev.tsv.fail.tsv
```

存在チェック用のURLリストを抽出

前回成功時のURLに関してはアクセスしないロジックを組むために必要

```
$ cat page-content-to-dev.tsv.success.tsv | awk -v FS='\t' '$0=$1' | tail -n+2 | sort | uniq >page-content-to-dev.tsv.success-url.txt
```

前回失敗時のURLに関してはアクセスしないロジックを組むために必要


```
$ cat page-content-to-dev.tsv.fail.tsv | awk -v FS='\t' '$0=$1' | tail -n+2 | sort | uniq | grep -P 'https?' | sort | uniq >page-content-to-dev.tsv.fail-url.txt
```

上記２つのファイルをマージ


```
$ ls page-content-to-dev.tsv.fail-url.txt page-content-to-dev.tsv.success-url.txt | xargs cat | sort | uniq | jq -R '' | jq -s '' >page-content-to-dev.tsv.no-need-access-url.json
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
