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




```
$ time ./download-detail-page-spa.py


$ time ./link-create.py


$ time ./extract-page-content.py

```


ないよーん

これが現れた場合は

```

$ ./mock.py 'https://qiita.com/yamaru/items/527ca7d814534beca56a'


```

起動してxpath確認してlist.jsonにパターン追加
