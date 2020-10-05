#!/usr/bin/env bash

ZERO_PAD_DIGIT="%010d"

COMMON_DIR_NAME_PREFIX=page
BASE_FILE_NAME=base-file-name-list.txt

SOURCE_DIR_NAME_SUFFIX=-detail
SOURCE_DIR_NAME=$COMMON_DIR_NAME_PREFIX$SOURCE_DIR_NAME_SUFFIX
SOURCE_FILE_SUFFIX=html

INPUT_DIR_NAME_SUFFIX=-xpath-list
INPUT_DIR_NAME=$COMMON_DIR_NAME_PREFIX$INPUT_DIR_NAME_SUFFIX
INPUT_FILE_SUFFIX=txt

OUTPUT_DIR_NAME_SUFFIX=-partial-dom
OUTPUT_DIR_NAME=$COMMON_DIR_NAME_PREFIX$OUTPUT_DIR_NAME_SUFFIX
OUTPUT_FILE_SUFFIX=html

cat $BASE_FILE_NAME | grep -Po '(?<=//).*?(?=/)' | ruby -F'\.' -anle 'puts $F.reverse.join("-")' | \

  while read base_name;do

    #出力結果格納ディレクトリの作成
    mkdir -p $OUTPUT_DIR_NAME/$base_name

    #サブディレクトリ単位で結果格納
    ls $INPUT_DIR_NAME/$base_name/*$INPUT_FILE_SUFFIX | grep $base_name | \

      while read INPUT_FILE_NAME;do


        TARGET_FILE_NAME=$(echo $INPUT_FILE_NAME | ruby -F'/' -anle 'puts $F[2]' | sed "s/$INPUT_DIR_NAME//g" | sed "s/$INPUT_DIR_NAME_SUFFIX.$INPUT_FILE_SUFFIX//g")

        SOURCE_FILE_NAME=$SOURCE_DIR_NAME/$base_name/$SOURCE_DIR_NAME$TARGET_FILE_NAME.$SOURCE_FILE_SUFFIX

        cat -n $INPUT_FILE_NAME | \

          while read num xpath;do

            OUTPUT_FILE_NAME=$OUTPUT_DIR_NAME/$base_name/$OUTPUT_DIR_NAME$TARGET_FILE_NAME-$(printf $ZERO_PAD_DIGIT $num).$OUTPUT_FILE_SUFFIX

            cat $SOURCE_FILE_NAME | xmllint --html --xpath $xpath - 2>/dev/null | tidy -i - 2>/dev/null >$OUTPUT_FILE_NAME

          done


      done

  done
