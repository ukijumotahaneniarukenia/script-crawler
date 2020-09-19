サイトページだうんろーど

```
echo https://jp.reuters.com/  | xargs -n1 | \
    while read url;do
      output_web_page_name = $(echo $url | grep -Po '(?<=//).*?(?=/)' | jq -Rr '(split(".")|reverse|join("-"))+".html"')
      curl -fsSL "$url" -o "$output_web_page_name";
      nkf -Lu "$output_web_page_name" | sponge "$output_web_page_name"
    done
```



```
pip3 install --user requests

pip3 install --user lxml

pip3 install --user bs4

pip3 install --user selenium
```
