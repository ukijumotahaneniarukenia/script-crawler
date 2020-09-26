#!/usr/bin/env bash

#前回アクセスURLリストの作成
cat base-file-name-list.txt | grep -Po '(?<=//).*?(?=/)' | ruby -F'\.' -anle 'puts $F.reverse.join("-")' | \
  while read base_name;do

    echo $base_name

    if [ -f page-content-$base_name.tsv ];then

      #項目数が正しいデータ行のみ抽出
      cat page-content-$base_name.tsv | awk -v FS='\t' 'NF==8{for(i=1;i<=NF;i++){printf $i"\t"}printf "\n"}' | sed -r 's/\t$//' >page-content-$base_name.success.tsv

      #項目数が正しくないデータ行のみ抽出
      cat page-content-$base_name.tsv | awk -v FS='\t' 'NF!=8{for(i=1;i<=NF;i++){printf $i"\t"}printf "\n"}' | sed -r 's/\t$//' >page-content-$base_name.fail.tsv

      if [ -f page-content-$base_name.success.tsv -a -s page-content-$base_name.success.tsv ];then

        #前回成功時のURLに関してはアクセスしないロジックを組むために必要
        cat page-content-$base_name.success.tsv | awk -v FS='\t' '$0=$1' | tail -n+2 | sort | uniq >page-content-$base_name.success-url.txt

      fi

      if [ -f page-content-$base_name.fail.tsv -a -s page-content-$base_name.fail.tsv ];then

        #前回失敗時のURLに関してはアクセスしないロジックを組むために必要
        cat page-content-$base_name.fail.tsv | awk -v FS='\t' '$0=$1' | tail -n+2 | sort | uniq | grep -P 'https?' >page-content-$base_name.fail-url.txt

      fi

      if [ -f page-content-$base_name.success-url.txt -o -f page-content-$base_name.fail-url.txt ];then

        #上記２つのファイルをマージ
        ls page-content-$base_name*-url.txt | xargs cat | sort | uniq | jq -R '' | jq -s '' >page-content-$base_names-no-need-access-url.json

      fi


    fi


  done
