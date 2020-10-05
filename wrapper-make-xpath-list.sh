#!/usr/bin/env bash

COMMON_DIR_NAME_PREFIX=page
BASE_FILE_NAME=base-file-name-list.txt

INPUT_DIR_NAME_SUFFIX=-detail
INPUT_DIR_NAME=$COMMON_DIR_NAME_PREFIX$INPUT_DIR_NAME_SUFFIX
INPUT_FILE_SUFFIX=html

OUTPUT_DIR_NAME_SUFFIX=-xpath-list
OUTPUT_DIR_NAME=$COMMON_DIR_NAME_PREFIX$OUTPUT_DIR_NAME_SUFFIX
OUTPUT_FILE_SUFFIX=txt

cat $BASE_FILE_NAME | grep -Po '(?<=//).*?(?=/)' | ruby -F'\.' -anle 'puts $F.reverse.join("-")' | \

  while read base_name;do

    #出力結果格納ディレクトリの作成
    mkdir -p $OUTPUT_DIR_NAME/$base_name

    #コメントの除去
    ls $INPUT_DIR_NAME/$base_name/*$INPUT_FILE_SUFFIX | xargs -I@ -n1 bash -c 'cat @ | rm-html-comment-bash | sponge @'

    #サブディレクトリ単位で結果格納
    ls $INPUT_DIR_NAME/$base_name/*$INPUT_FILE_SUFFIX | grep $base_name | \

      while read INPUT_FILE_NAME;do

        OUTPUT_FILE_NAME=$(echo $INPUT_FILE_NAME | sed "s/$INPUT_DIR_NAME/$OUTPUT_DIR_NAME/g" | sed "s/.$INPUT_FILE_SUFFIX/$OUTPUT_DIR_NAME_SUFFIX.$OUTPUT_FILE_SUFFIX/g")

        xpath-gen-python $INPUT_FILE_NAME > $OUTPUT_FILE_NAME

      done

  done
