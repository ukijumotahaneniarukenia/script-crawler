#!/usr/bin/env bash

BASE_FILE_NAME=base-file-name-list.txt
INPUT_DIR_NAME=page-xpath-list
INPUT_FILE_SUFFIX=txt
OUTPUT_DIR_NAME=page-partial-dom
OUTPUT_FILE_SUFFIX=html


cat $BASE_FILE_NAME | grep -Po '(?<=//).*?(?=/)' | ruby -F'\.' -anle 'puts $F.reverse.join("-")' | \

  while read base_name;do

    #出力結果格納ディレクトリの作成
    mkdir -p $OUTPUT_DIR_NAME/$base_name

    #サブディレクトリ単位で結果格納
    ls $INPUT_DIR_NAME/$base_name/*$INPUT_FILE_SUFFIX | grep $base_name | \

      while read INPUT_FILE_NAME;do

        OUTPUT_FILE_NAME=$(echo $INPUT_FILE_NAME | sed "s/$INPUT_DIR_NAME/$OUTPUT_DIR_NAME/g" | sed "s;xpath-list;partial-dom;g" | sed "s;$INPUT_FILE_SUFFIX;$OUTPUT_FILE_SUFFIX;" | sed "s;$OUTPUT_DIR_NAME/;;")

				echo $INPUT_FILE_NAME

				#cat -n $INPUT_FILE_NAME | \

				#	while read num xpath;do

				#		cat test-big-tidy.html | xmllint --html --xpath $xpath - 2>/dev/null | tidy -i - 2>/dev/null >test-big-tidy/test-big-tidy-$(printf "%05d" $num)-partial-dom.html;done

      done

  done


