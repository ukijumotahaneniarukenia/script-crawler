サイトページだうんろーど

```
$ echo https://jp.reuters.com/ | while read url;do curl -fsSL "$url" -o $(echo $url | grep -Po '(?<=//).*?(?=/)' | jq -Rr '(split(".")|reverse|join("-"))+".html"');done
```



```
$ pip3 install --user lxml

$ pip3 install --user bs4

pip3 install --user selenium

```
