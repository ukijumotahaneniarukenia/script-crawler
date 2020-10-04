クリーンするやつ
```
$ cat test-big-remove-comment.html | tr -d \\n | sed -r 's/> +</></g' | sed -r 's/>\t+</></g' | sed -r 's/\t//g' | sed -r 's/^\s+//' | awk 4| ruby -nle 'puts $_.gsub(/[^\u{0000}-\u{007F}]/){|e|numchar=e.ord;"#{"&#"+numchar.to_s+";"}"}'|tidy -i - 2>/dev/null >test-big-clean.html
```


うまく行ったらこうしたい

```
$ cat test-big-clean.html | xmllint --html --xpath '/html/body/div[1]/div/div[1]/div/main/article/header/h1' - 2>/dev/null
<h1 class="entry-title">記事一覧</h1>
```


部分整形

```
$ cat test-ng.html | tidy -i - 2>/dev/null | sponge test-ng.html
```
