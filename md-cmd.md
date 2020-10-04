クリーンするやつ
```
$ cat test-big-remove-comment.html | tr -d \\n | sed -r 's/> +</></g' | sed -r 's/>\t+</></g' | sed -r 's/\t//g' | sed -r 's/^\s+//' | awk 4| ruby -nle 'puts $_.gsub(/[^\u{0000}-\u{007F}]/){|e|numchar=e.ord;"#{"&#"+numchar.to_s+";"}"}'|tidy -i - 2>/dev/null >test-big-clean.html
```
