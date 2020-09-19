事前準備

CMD

```
pip3 install --user requests

pip3 install --user lxml

pip3 install --user bs4

pip3 install --user selenium
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
