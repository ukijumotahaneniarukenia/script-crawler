#!/usr/bin/env bash

SOURCE_DIR_NAME=extract-column-list
SOURCE_FILE_NAME_SUFFIX=json

INPUT_DIR_NAME=page-content
INPUT_FILE_NAME_SUFFIX=tsv

OUTPUT_DIR_NAME=no-need-access-url
OUTPUT_FILE_NAME_SUFFIX=json

#前回アクセスURLリストの作成
cat base-file-name-list.txt | grep -Po '(?<=//).*?(?=/)' | ruby -F'\.' -anle 'puts $F.reverse.join("-")' | \

  while read base_name;do

    COLUMN_CNT=

    if [ -f $SOURCE_DIR_NAME/extract-column-list-common.$SOURCE_FILE_NAME_SUFFIX -a -f $SOURCE_DIR_NAME/extract-column-list-site-$base_name.$SOURCE_FILE_NAME_SUFFIX ];then

      COLUMN_CNT=$(cat $SOURCE_DIR_NAME/extract-column-list-common.$SOURCE_FILE_NAME_SUFFIX $SOURCE_DIR_NAME/extract-column-list-site-$base_name.$SOURCE_FILE_NAME_SUFFIX | jq 'add' | jq -s '(.[0]|length)+((.[1]|length)*2)')

    fi

    mkdir -p $OUTPUT_DIR_NAME/$base_name

    if [ -f $INPUT_DIR_NAME/$base_name/$INPUT_DIR_NAME-$base_name.$INPUT_FILE_NAME_SUFFIX ];then

      #項目数が正しいデータ行のみ抽出
      cat $INPUT_DIR_NAME/$base_name/$INPUT_DIR_NAME-$base_name.$INPUT_FILE_NAME_SUFFIX | \
        awk -v FS='\t' -v CNT=$COLUMN_CNT 'NF==CNT{for(i=1;i<=NF;i++){printf $i"\t"}printf "\n"}' | \
        sed -r 's/\t$//' | \
        sponge $INPUT_DIR_NAME/$base_name/$INPUT_DIR_NAME-$base_name.$INPUT_FILE_NAME_SUFFIX

      #前回アクセスのURLに関してはアクセスしないロジックを組むために必要
      cat $INPUT_DIR_NAME/$base_name/$INPUT_DIR_NAME-$base_name.$INPUT_FILE_NAME_SUFFIX | \
        awk -v FS='\t' '$0=$1' | \
        tail -n+2 | \
        sort | \
        uniq | \
        grep -P 'https?' | \
        jq -R '' | \
        jq -s '' >>$OUTPUT_DIR_NAME/$base_name/$OUTPUT_DIR_NAME-$base_name.$OUTPUT_FILE_NAME_SUFFIX

      #前回分とのマージ
      cat $OUTPUT_DIR_NAME/$base_name/$OUTPUT_DIR_NAME-$base_name.$OUTPUT_FILE_NAME_SUFFIX | jq -s 'reduce .[] as $item([];.+$item)'

    fi

  done
