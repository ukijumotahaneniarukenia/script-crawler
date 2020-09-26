#!/usr/bin/env bash

#サイト別カラムリストの一覧の作成
cat list.json | jq -cr '. as $in | $in | length as $cnt | [range(0;$cnt)]|foreach $in[.[]] as $item("";($item|(."SITE_URL"|gsub(".*//";"")|gsub("/.*";"")|split(".")|reverse|join("-")) + "\t" +($item|({"EXTRACT_COLUMN_LIST":(."EXTRACT_COLUMN_LIST"|keys)}|tojson))))'| while read base_name column_list;do echo $column_list > "extract-site-column-list-"$base_name".json";cat "extract-site-column-list-"$base_name".json"|jq '' |sponge "extract-site-column-list-"$base_name".json";done




#ベースファイル名リストの作成
cat list.json | jq -r 'map(."SITE_URL")|join("\n")'>base-file-name-list.txt



#ベースファイル名リストの正規化



cat base-file-name-list.txt | ruby -F'(?<=//)' -anle 'scheme=$F[0];domain=$F[1].split("/")[0]+"/";puts "#{scheme + domain}"' | sort | uniq | sponge base-file-name-list.txt





