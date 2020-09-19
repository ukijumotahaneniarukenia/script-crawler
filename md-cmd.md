事前準備

CMD

```
pip3 install --user requests

pip3 install --user lxml

pip3 install --user bs4

pip3 install --user selenium
```

サイト別カラムリストの一覧の作成

CMD

```
$ cat list-non-spa.json | jq -cr '. as $in | $in | length as $cnt | [range(0;$cnt)]|foreach $in[.[]] as $item("";($item|(."SITE_URL"|gsub(".*//";"")|gsub("/.*";"")|split(".")|reverse|join("-")) + "\t" +($item|({"EXTRACT_COLUMN_LIST":(."EXTRACT_COLUMN_LIST"|keys)}|tojson)) ))' | while read base_name column_list;do echo $column_list > "list-column-"$base_name".json";cat "list-column-"$base_name".json"|jq '' |sponge "list-column-"$base_name".json";done
```

OUT

```
$ ls -lh list-column*json
-rw-r--r-- 1 aine aine 69  9月 19 21:18 list-column-com-asahi-www.json
-rw-r--r-- 1 aine aine 69  9月 19 21:18 list-column-com-reuters-jp.json
```





ベースファイル名リストの作成

CMD

```
$ cat list.json | jq -r 'map(."SITE_URL")|join("\n")'>base-file-name-list.txt
```

OUT

```
$ cat base-file-name-list.txt
https://jp.reuters.com/
https://www.asahi.com/
```


エントリページのダウンロード

CMD

```
$ cat base-file-name-list  | while read url;do output_web_page_name=$(echo $url | grep -Po '(?<=//).*?(?=/)' | jq -Rr '"page-"+(split(".")|reverse|join("-"))+".html"');curl -fsSL "$url" -o "$output_web_page_name";nkf -Lu "$output_web_page_name" | sponge "$output_web_page_name";done
```

OUT

```
$ ls -lh page*html
-rw-r--r-- 1 aine aine 161K  9月 19 15:02 page-com-asahi-www.html
-rw-r--r-- 1 aine aine 207K  9月 19 15:02 page-com-reuters-jp.html
```

リンクページの作成

CMD

```
./link-create.py
```

OUT

```
$ ls -lh link*txt
-rw-r--r-- 1 aine aine 53K  9月 19 15:36 link-com-asahi-www.txt
-rw-r--r-- 1 aine aine 12K  9月 19 15:36 link-com-reuters-jp.txt
```

個別ページのダウンロード


CMD

```
./download-detail-page.py
```

OUT

```
$ ls -lh page-detail-*html
-rw-r--r-- 1 aine aine 109K  9月 19 18:21 page-detail-https---com-asahi-www--articles-ASN9373V6N93UBQU00B.html-iref-comtop_list_api_f02.html
-rw-r--r-- 1 aine aine 107K  9月 19 18:21 page-detail-https---com-asahi-www--articles-ASN966Q4TN8DUBQU008.html-iref-comtop_list_api_f03.html
-rw-r--r-- 1 aine aine 112K  9月 19 18:21 page-detail-https---com-asahi-www--articles-ASN994FGQN98PTFC001.html-iref-comtop_list_cul_n03.html
-rw-r--r-- 1 aine aine 107K  9月 19 18:21 page-detail-https---com-asahi-www--articles-ASN9D0D3RKD5ULFA010.html-iref-comtop_list_obi_n05.html
-rw-r--r-- 1 aine aine 102K  9月 19 18:21 page-detail-https---com-asahi-www--articles-ASN9D74BKN9CUJHB008.html-iref-comtop_list_sci_f02.html
-rw-r--r-- 1 aine aine 100K  9月 19 18:21 page-detail-https---com-asahi-www--articles-ASN9G25LCN9DUHBI01P.html-iref-comtop_list_obi_n04.html
-rw-r--r-- 1 aine aine 231K  9月 19 18:21 page-detail-https---com-reuters-jp----com-reuters-jp-article-usa-fed-framework-idJPKBN26936J.html
-rw-r--r-- 1 aine aine 290K  9月 19 18:21 page-detail-https---com-reuters-jp--article-health-coronavirus-britain-idJPKBN2691EU.html
-rw-r--r-- 1 aine aine 287K  9月 19 18:21 page-detail-https---com-reuters-jp--article-health-coronavirus-britain-veteran-idJPKBN2690II.html
-rw-r--r-- 1 aine aine 275K  9月 19 18:21 page-detail-https---com-reuters-jp--article-health-coronavirus-usa-canada-idJPKBN2692T1.html
-rw-r--r-- 1 aine aine 278K  9月 19 18:21 page-detail-https---com-reuters-jp--article-health-coronavirus-usa-trump-idJPKBN26931V.html
-rw-r--r-- 1 aine aine 208K  9月 19 18:21 page-detail-https---com-reuters-jp.html
```


シングルページアプリケーションでない場合の取得項目の抽出

CMD

```
./extract-non-spa-page-content.py
```


