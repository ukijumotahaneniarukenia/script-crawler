エクスポート

```
$ time groonga $HOME/groongadb/testdb dump >$HOME/groongadb/testdb-$(date "+%Y-%m-%dT%H-%M-%S").dump

real	0m0.028s
user	0m0.009s
sys	0m0.020s

$ ls -lh $HOME/groongadb/*dump
-rw-rw-r-- 1 aine aine 2.1K  9月 22 10:45 /home/aine/groongadb/testdb-2020-09-22T10-45-34.dump

$ cat /home/aine/groongadb/testdb-2020-09-22T10-45-34.dump
table_create Terms TABLE_PAT_KEY ShortText --default_tokenizer TokenBigram --normalizer NormalizerAuto

table_create test_tbl TABLE_HASH_KEY|KEY_LARGE UInt32
column_create test_tbl DATE_TIME COLUMN_SCALAR LongText
column_create test_tbl EXTRACT_BASE_NAME COLUMN_SCALAR LongText
column_create test_tbl EXTRACT_SITE_NAME COLUMN_SCALAR LongText
column_create test_tbl EXTRACT_SITE_URL COLUMN_SCALAR LongText
column_create test_tbl EXTRACT_URL_NAME COLUMN_SCALAR LongText
column_create test_tbl ID COLUMN_SCALAR UInt32
column_create test_tbl TITLE_NAME COLUMN_SCALAR LongText

load --table test_tbl
[
["_key","DATE_TIME","EXTRACT_BASE_NAME","EXTRACT_SITE_NAME","EXTRACT_SITE_URL","EXTRACT_URL_NAME","ID","TITLE_NAME"],
[1,"2020年9月19日 / 06:47 / 18時間前更新","com-reuters-jp","ロイター","https://jp.reuters.com/","https://jp.reuters.com////jp.reuters.com/article/usa-fed-framework-idJPKBN26936J",1,"米ＦＲＢ新戦略、国民に浸透せず　2重の責務も誤解＝調査"],
[2,"2020年9月18日","com-reuters-jp","ロイター","https://jp.reuters.com/","https://jp.reuters.com//article/health-coronavirus-britain-idJPKBN2691EU",2,"英、コロナ第2波不可避　新たな措置実施も＝ジョンソン首相"],
[3,"2020年9月18日","com-reuters-jp","ロイター","https://jp.reuters.com/","https://jp.reuters.com//article/health-coronavirus-britain-veteran-idJPKBN2690II",3,"医療支援の英退役軍人、自伝「明日はきっと良い日に」執筆"],
[4,"2020年9月19日","com-reuters-jp","ロイター","https://jp.reuters.com/","https://jp.reuters.com//article/health-coronavirus-usa-canada-idJPKBN2692T1",4,"米、加・メキシコとのコロナ渡航制限継続　来月21日まで"],
[5,"2020年9月19日","com-reuters-jp","ロイター","https://jp.reuters.com/","https://jp.reuters.com//article/health-coronavirus-usa-trump-idJPKBN26931V",5,"トランプ氏、来年4月までに全国民分のコロナワクチン確保へ"]
]

column_create Terms TITLE_NAME COLUMN_INDEX|WITH_POSITION test_tbl TITLE_NAME
```

インポート

```
$ ls $HOME/groongadb/* | grep -v dump | xargs rm -rf
```

CMD

```
$ groonga -n $HOME/groongadb/testdb < $HOME/groongadb/testdb-2020-09-22T10-45-34.dump
```

OUT

```
[[0,1600739384.024454,0.003414392471313477],true]
[[0,1600739384.027922,0.003383159637451172],true]
[[0,1600739384.031341,0.004183292388916016],true]
[[0,1600739384.035587,0.003495454788208008],true]
[[0,1600739384.039137,0.003490447998046875],true]
[[0,1600739384.0427,0.003648519515991211],true]
[[0,1600739384.046418,0.003588199615478516],true]
[[0,1600739384.050077,0.00331425666809082],true]
[[0,1600739384.053461,0.003468036651611328],true]
[[0,1600739384.057014,0.002407073974609375],5]
[[0,1600739384.05949,0.01646590232849121],true]
```

POST

```
$ groonga $HOME/groongadb/testdb select --table test_tbl | jq
[
  [
    0,
    1600739422.726028,
    0.0004065036773681641
  ],
  [
    [
      [
        5
      ],
      [
        [
          "_id",
          "UInt32"
        ],
        [
          "_key",
          "UInt32"
        ],
        [
          "DATE_TIME",
          "LongText"
        ],
        [
          "EXTRACT_BASE_NAME",
          "LongText"
        ],
        [
          "EXTRACT_SITE_NAME",
          "LongText"
        ],
        [
          "EXTRACT_SITE_URL",
          "LongText"
        ],
        [
          "EXTRACT_URL_NAME",
          "LongText"
        ],
        [
          "ID",
          "UInt32"
        ],
        [
          "TITLE_NAME",
          "LongText"
        ]
      ],
      [
        1,
        1,
        "2020年9月19日 / 06:47 / 18時間前更新",
        "com-reuters-jp",
        "ロイター",
        "https://jp.reuters.com/",
        "https://jp.reuters.com////jp.reuters.com/article/usa-fed-framework-idJPKBN26936J",
        1,
        "米ＦＲＢ新戦略、国民に浸透せず　2重の責務も誤解＝調査"
      ],
      [
        2,
        2,
        "2020年9月18日",
        "com-reuters-jp",
        "ロイター",
        "https://jp.reuters.com/",
        "https://jp.reuters.com//article/health-coronavirus-britain-idJPKBN2691EU",
        2,
        "英、コロナ第2波不可避　新たな措置実施も＝ジョンソン首相"
      ],
      [
        3,
        3,
        "2020年9月18日",
        "com-reuters-jp",
        "ロイター",
        "https://jp.reuters.com/",
        "https://jp.reuters.com//article/health-coronavirus-britain-veteran-idJPKBN2690II",
        3,
        "医療支援の英退役軍人、自伝「明日はきっと良い日に」執筆"
      ],
      [
        4,
        4,
        "2020年9月19日",
        "com-reuters-jp",
        "ロイター",
        "https://jp.reuters.com/",
        "https://jp.reuters.com//article/health-coronavirus-usa-canada-idJPKBN2692T1",
        4,
        "米、加・メキシコとのコロナ渡航制限継続　来月21日まで"
      ],
      [
        5,
        5,
        "2020年9月19日",
        "com-reuters-jp",
        "ロイター",
        "https://jp.reuters.com/",
        "https://jp.reuters.com//article/health-coronavirus-usa-trump-idJPKBN26931V",
        5,
        "トランプ氏、来年4月までに全国民分のコロナワクチン確保へ"
      ]
    ]
  ]
]
```
