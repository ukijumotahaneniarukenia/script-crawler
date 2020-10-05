#!/usr/bin/env bash

INPUT_DIR_NAME=extract-column-list
OUTPUT_DIR_NAME=link

#サイト別カラムリストの一覧の作成
cat list.json | \
  jq -cr '
    . as $in |
      $in | length as $cnt |
      [range(0;$cnt)] |
      foreach $in[.[]] as $item("";
        (
          $item|(."SITE_URL"|gsub(".*//";"")|gsub("/.*";"")|split(".")|reverse|join("-"))
        + "\t"
        + ($item|({"EXTRACT_COLUMN_LIST":(."EXTRACT_COLUMN_LIST"|keys)}|tojson))
        )
      )' | \
        while read base_name column_list;do
          echo $column_list > "$INPUT_DIR_NAME/extract-column-list-site-"$base_name".json";
          cat "$INPUT_DIR_NAME/extract-column-list-site-"$base_name".json" | jq '' | sponge "$INPUT_DIR_NAME/extract-column-list-site-"$base_name".json";
        done

wait $!

#ベースファイル名リストの作成
cat list.json | jq -r 'map(."SITE_URL")|join("\n")'>base-file-name-list.txt

wait $!

#ベースファイル名リストの正規化
cat base-file-name-list.txt | ruby -F'(?<=//)' -anle 'scheme=$F[0];domain=$F[1].split("/")[0]+"/";puts "#{scheme + domain}"' | sort | uniq | sponge base-file-name-list.txt

wait $!

#ページのダウンロード
time ./download-detail-page.py

while [ -n "$(ps aux | grep -P 'download-detail-page.py' | grep -v grep | awk '$0=$2')" ];do

  :

done

#リンクの作成
time ./link-create.py

wait $!
