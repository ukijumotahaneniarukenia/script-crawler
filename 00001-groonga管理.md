インストール

```
#https://groonga.org/ja/docs/install/ubuntu.html#ppa-personal-package-archive

apt -y install software-properties-common

add-apt-repository -y universe

add-apt-repository -y ppa:groonga/ppa

apt update

apt -y install groonga

apt -y install groonga-tokenizer-mecab

```


データベースの削除


```
$ rm -rf $HOME/groongadb/testdb*
```

データベースの作成

CMD

```
$ mkdir -p $HOME/groongadb

$ groonga -n $HOME/groongadb/testdb
```


POST

Cntrl + Dでプロンプトから抜ける

```
$ tree -a -ugpfhqD --timefmt '%Y-%m-%dT%H:%M:%S' -J groongadb | jq
[
  {
    "type": "directory",
    "name": "groongadb",
    "contents": [
      {
        "type": "file",
        "name": "groongadb/testdb",
        "mode": "0640",
        "prot": "-rw-r-----",
        "user": "aine",
        "group": "aine",
        "size": 4096,
        "time": "2020-09-22T08:54:27"
      },
      {
        "type": "file",
        "name": "groongadb/testdb.0000000",
        "mode": "0640",
        "prot": "-rw-r-----",
        "user": "aine",
        "group": "aine",
        "size": 12857344,
        "time": "2020-09-22T08:54:27"
      },
      {
        "type": "file",
        "name": "groongadb/testdb.001",
        "mode": "0640",
        "prot": "-rw-r-----",
        "user": "aine",
        "group": "aine",
        "size": 1048576,
        "time": "2020-09-22T08:54:27"
      },
      {
        "type": "file",
        "name": "groongadb/testdb.conf",
        "mode": "0640",
        "prot": "-rw-r-----",
        "user": "aine",
        "group": "aine",
        "size": 12632064,
        "time": "2020-09-22T08:54:27"
      },
      {
        "type": "file",
        "name": "groongadb/testdb.options",
        "mode": "0640",
        "prot": "-rw-r-----",
        "user": "aine",
        "group": "aine",
        "size": 274432,
        "time": "2020-09-22T08:54:27"
      }
    ]
  },
  {
    "type": "report",
    "directories": 0,
    "files": 5
  }
]
```


テーブル一覧の確認

CMD

```
$ groonga $HOME/groongadb/testdb table_list | jq
```

OUT

```
[
  [
    0,
    1600732692.531381,
    5.53131103515625e-05
  ],
  [
    [
      [
        "id",
        "UInt32"
      ],
      [
        "name",
        "ShortText"
      ],
      [
        "path",
        "ShortText"
      ],
      [
        "flags",
        "ShortText"
      ],
      [
        "domain",
        "ShortText"
      ],
      [
        "range",
        "ShortText"
      ],
      [
        "default_tokenizer",
        "ShortText"
      ],
      [
        "normalizer",
        "ShortText"
      ]
    ]
  ]
]
```


テーブルの作成

DATE_TIMEは前処理頑張る気になればTIME型にするなど

CMD

```
groonga $HOME/groongadb/testdb table_create --name test_tbl --flags 'TABLE_HASH_KEY|KEY_LARGE' --key_type UInt32
groonga $HOME/groongadb/testdb column_create --table test_tbl --name ID --type UInt32
groonga $HOME/groongadb/testdb column_create --table test_tbl --name EXTRACT_URL_NAME --type LongText
groonga $HOME/groongadb/testdb column_create --table test_tbl --name EXTRACT_SITE_NAME --type LongText
groonga $HOME/groongadb/testdb column_create --table test_tbl --name EXTRACT_SITE_URL --type LongText
groonga $HOME/groongadb/testdb column_create --table test_tbl --name EXTRACT_BASE_NAME --type LongText
groonga $HOME/groongadb/testdb column_create --table test_tbl --name DATE_TIME --type LongText
groonga $HOME/groongadb/testdb column_create --table test_tbl --name TITLE_NAME --type LongText
```

EXE

```
$ groonga $HOME/groongadb/testdb table_create --name test_tbl --flags 'TABLE_HASH_KEY|KEY_LARGE' --key_type UInt32
[[0,1600733474.725882,0.01737856864929199],true]

$ groonga $HOME/groongadb/testdb column_create --table test_tbl --name ID --type UInt32
[[0,1600733474.753333,0.003874301910400391],true]

$ groonga $HOME/groongadb/testdb column_create --table test_tbl --name EXTRACT_URL_NAME --type LongText
[[0,1600733474.767495,0.004075765609741211],true]

$ groonga $HOME/groongadb/testdb column_create --table test_tbl --name EXTRACT_SITE_NAME --type LongText
[[0,1600733474.780555,0.004324674606323242],true]

$ groonga $HOME/groongadb/testdb column_create --table test_tbl --name EXTRACT_SITE_URL --type LongText
[[0,1600733474.794124,0.004263401031494141],true]

$ groonga $HOME/groongadb/testdb column_create --table test_tbl --name EXTRACT_BASE_NAME --type LongText
[[0,1600733474.809124,0.004140615463256836],true]

$ groonga $HOME/groongadb/testdb column_create --table test_tbl --name DATE_TIME --type LongText
[[0,1600733474.823845,0.003610372543334961],true]

$ groonga $HOME/groongadb/testdb column_create --table test_tbl --name TITLE_NAME --type LongText
[[0,1600733474.836133,0.004417896270751953],true]
```


テーブル一覧の確認

CMD

```
$ groonga $HOME/groongadb/testdb table_list | jq
```

OUT

```
[
  [
    0,
    1600733546.022743,
    0.0001370906829833984
  ],
  [
    [
      [
        "id",
        "UInt32"
      ],
      [
        "name",
        "ShortText"
      ],
      [
        "path",
        "ShortText"
      ],
      [
        "flags",
        "ShortText"
      ],
      [
        "domain",
        "ShortText"
      ],
      [
        "range",
        "ShortText"
      ],
      [
        "default_tokenizer",
        "ShortText"
      ],
      [
        "normalizer",
        "ShortText"
      ]
    ],
    [
      256,
      "test_tbl",
      "/home/aine/groongadb/testdb.0000100",
      "TABLE_HASH_KEY|KEY_LARGE|PERSISTENT",
      "UInt32",
      null,
      null,
      null
    ]
  ]
]
```


テーブル定義確認

CMD

```
$ groonga $HOME/groongadb/testdb column_list test_tbl | jq
```

OUT

```
[
  [
    0,
    1600733618.786711,
    0.0002393722534179688
  ],
  [
    [
      [
        "id",
        "UInt32"
      ],
      [
        "name",
        "ShortText"
      ],
      [
        "path",
        "ShortText"
      ],
      [
        "type",
        "ShortText"
      ],
      [
        "flags",
        "ShortText"
      ],
      [
        "domain",
        "ShortText"
      ],
      [
        "range",
        "ShortText"
      ],
      [
        "source",
        "ShortText"
      ]
    ],
    [
      256,
      "_key",
      "",
      "",
      "COLUMN_SCALAR",
      "test_tbl",
      "UInt32",
      []
    ],
    [
      262,
      "DATE_TIME",
      "/home/aine/groongadb/testdb.0000106",
      "var",
      "COLUMN_SCALAR|PERSISTENT",
      "test_tbl",
      "LongText",
      []
    ],
    [
      261,
      "EXTRACT_BASE_NAME",
      "/home/aine/groongadb/testdb.0000105",
      "var",
      "COLUMN_SCALAR|PERSISTENT",
      "test_tbl",
      "LongText",
      []
    ],
    [
      259,
      "EXTRACT_SITE_NAME",
      "/home/aine/groongadb/testdb.0000103",
      "var",
      "COLUMN_SCALAR|PERSISTENT",
      "test_tbl",
      "LongText",
      []
    ],
    [
      260,
      "EXTRACT_SITE_URL",
      "/home/aine/groongadb/testdb.0000104",
      "var",
      "COLUMN_SCALAR|PERSISTENT",
      "test_tbl",
      "LongText",
      []
    ],
    [
      258,
      "EXTRACT_URL_NAME",
      "/home/aine/groongadb/testdb.0000102",
      "var",
      "COLUMN_SCALAR|PERSISTENT",
      "test_tbl",
      "LongText",
      []
    ],
    [
      257,
      "ID",
      "/home/aine/groongadb/testdb.0000101",
      "fix",
      "COLUMN_SCALAR|PERSISTENT",
      "test_tbl",
      "UInt32",
      []
    ],
    [
      263,
      "TITLE_NAME",
      "/home/aine/groongadb/testdb.0000107",
      "var",
      "COLUMN_SCALAR|PERSISTENT",
      "test_tbl",
      "LongText",
      []
    ]
  ]
]
```

データ投入

PRE


```
$ curl -fsSL https://raw.githubusercontent.com/ukijumotahaneniarukenia/script-crawler/master/page-content-com-reuters-jp.tsv -o test.tsv

$ cat test.tsv | awk -v FS='\t' 'END{print NR,NF}'
6 8

$ cat test.tsv | tail -n+2 | awk -v FS='\t' '{print NR,NR,$1,$2,$3,$4,$5,$7}' OFS='\t' | sed '1i_key\tID\tEXTRACT_URL_NAME\tEXTRACT_SITE_NAME\tEXTRACT_SITE_URL\tEXTRACT_BASE_NAME\tDATE_TIME\tTITLE_NAME' >test-done.tsv

$ cat test-done.tsv | awk -v FS='\t' 'END{print NR,NF}'
6 7

$ tsv2json-jq test-done.tsv 

$ cat test-done.json | jq 'map(._key|=tonumber)|map(.ID|=tonumber)' | sponge test-done.json

$ cat test-done.json | jq ''
[
  {
    "_key": 1,
    "ID": 1,
    "EXTRACT_URL_NAME": "https://jp.reuters.com////jp.reuters.com/article/usa-fed-framework-idJPKBN26936J",
    "EXTRACT_SITE_NAME": "ロイター",
    "EXTRACT_SITE_URL": "https://jp.reuters.com/",
    "EXTRACT_BASE_NAME": "com-reuters-jp",
    "DATE_TIME": "2020年9月19日 / 06:47 / 18時間前更新",
    "TITLE_NAME": "米ＦＲＢ新戦略、国民に浸透せず　2重の責務も誤解＝調査"
  },
  {
    "_key": 2,
    "ID": 2,
    "EXTRACT_URL_NAME": "https://jp.reuters.com//article/health-coronavirus-britain-idJPKBN2691EU",
    "EXTRACT_SITE_NAME": "ロイター",
    "EXTRACT_SITE_URL": "https://jp.reuters.com/",
    "EXTRACT_BASE_NAME": "com-reuters-jp",
    "DATE_TIME": "2020年9月18日",
    "TITLE_NAME": "英、コロナ第2波不可避　新たな措置実施も＝ジョンソン首相"
  },
  {
    "_key": 3,
    "ID": 3,
    "EXTRACT_URL_NAME": "https://jp.reuters.com//article/health-coronavirus-britain-veteran-idJPKBN2690II",
    "EXTRACT_SITE_NAME": "ロイター",
    "EXTRACT_SITE_URL": "https://jp.reuters.com/",
    "EXTRACT_BASE_NAME": "com-reuters-jp",
    "DATE_TIME": "2020年9月18日",
    "TITLE_NAME": "医療支援の英退役軍人、自伝「明日はきっと良い日に」執筆"
  },
  {
    "_key": 4,
    "ID": 4,
    "EXTRACT_URL_NAME": "https://jp.reuters.com//article/health-coronavirus-usa-canada-idJPKBN2692T1",
    "EXTRACT_SITE_NAME": "ロイター",
    "EXTRACT_SITE_URL": "https://jp.reuters.com/",
    "EXTRACT_BASE_NAME": "com-reuters-jp",
    "DATE_TIME": "2020年9月19日",
    "TITLE_NAME": "米、加・メキシコとのコロナ渡航制限継続　来月21日まで"
  },
  {
    "_key": 5,
    "ID": 5,
    "EXTRACT_URL_NAME": "https://jp.reuters.com//article/health-coronavirus-usa-trump-idJPKBN26931V",
    "EXTRACT_SITE_NAME": "ロイター",
    "EXTRACT_SITE_URL": "https://jp.reuters.com/",
    "EXTRACT_BASE_NAME": "com-reuters-jp",
    "DATE_TIME": "2020年9月19日",
    "TITLE_NAME": "トランプ氏、来年4月までに全国民分のコロナワクチン確保へ"
  }
]


tojsonしてから入れるのがみそ

$ groonga $HOME/groongadb/testdb load --table test_tbl $(cat test-done.json | jq 'tojson')

[[0,1600737422.805915,0.0157930850982666],5]

```


データ確認

```
$ groonga $HOME/groongadb/testdb select --table test_tbl | jq
[
  [
    0,
    1600737577.452482,
    0.0004298686981201172
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

ID検索

```
$ groonga $HOME/groongadb/testdb select --table test_tbl --query _id:1 | jq
[
  [
    0,
    1600737677.958802,
    0.02032470703125
  ],
  [
    [
      [
        1
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
      ]
    ]
  ]
]
```




全文検索用の語彙表の作成

語彙表の名前：Terms

CMD


```
$ groonga $HOME/groongadb/testdb table_create --name Terms --flags TABLE_PAT_KEY --key_type ShortText --default_tokenizer TokenBigram --normalizer NormalizerAuto
```

OUT

```
[[0,1600737946.472945,0.006040096282958984],true]
```


全文検索用のインデックスカラムの作成

CMD

```
$ groonga $HOME/groongadb/testdb column_create --table Terms --name TITLE_NAME --flags 'COLUMN_INDEX|WITH_POSITION' --type test_tbl --source TITLE_NAME
```

OUT

```
[[0,1600737950.133021,0.01353645324707031],true]
```



全文検索


CMD

```
$ groonga $HOME/groongadb/testdb select --table test_tbl --query 'TITLE_NAME:@米' | jq
```

OUT

```
[
  [
    0,
    1600738063.65273,
    0.02017593383789062
  ],
  [
    [
      [
        2
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
        4,
        4,
        "2020年9月19日",
        "com-reuters-jp",
        "ロイター",
        "https://jp.reuters.com/",
        "https://jp.reuters.com//article/health-coronavirus-usa-canada-idJPKBN2692T1",
        4,
        "米、加・メキシコとのコロナ渡航制限継続　来月21日まで"
      ]
    ]
  ]
]
```


出力カラムの指定

CMD
```
$ groonga $HOME/groongadb/testdb select --table test_tbl --output_columns _key,TITLE_NAME,_score --query 'TITLE_NAME:@米' | jq
```

OUT

```
[
  [
    0,
    1600738271.38379,
    0.02041912078857422
  ],
  [
    [
      [
        2
      ],
      [
        [
          "_key",
          "UInt32"
        ],
        [
          "TITLE_NAME",
          "LongText"
        ],
        [
          "_score",
          "Int32"
        ]
      ],
      [
        1,
        "米ＦＲＢ新戦略、国民に浸透せず　2重の責務も誤解＝調査",
        1
      ],
      [
        4,
        "米、加・メキシコとのコロナ渡航制限継続　来月21日まで",
        1
      ]
    ]
  ]
]
```

表示範囲指定


CMD

```
$ groonga $HOME/groongadb/testdb select --table test_tbl --output_columns _key,TITLE_NAME,_score --query 'EXTRACT_SITE_NAME:@ロイター' --offset 0 --limit 3 | jq
```

OUT

```
[
  [
    0,
    1600738403.178998,
    0.0207679271697998
  ],
  [
    [
      [
        5
      ],
      [
        [
          "_key",
          "UInt32"
        ],
        [
          "TITLE_NAME",
          "LongText"
        ],
        [
          "_score",
          "Int32"
        ]
      ],
      [
        1,
        "米ＦＲＢ新戦略、国民に浸透せず　2重の責務も誤解＝調査",
        1
      ],
      [
        2,
        "英、コロナ第2波不可避　新たな措置実施も＝ジョンソン首相",
        1
      ],
      [
        3,
        "医療支援の英退役軍人、自伝「明日はきっと良い日に」執筆",
        1
      ]
    ]
  ]
]
```

CMD

```
$ groonga $HOME/groongadb/testdb select --table test_tbl --output_columns _key,TITLE_NAME,_score --query 'EXTRACT_SITE_NAME:@ロイター' --offset 2 --limit 3 | jq
```

OUT

```
[
  [
    0,
    1600738407.527044,
    0.01985764503479004
  ],
  [
    [
      [
        5
      ],
      [
        [
          "_key",
          "UInt32"
        ],
        [
          "TITLE_NAME",
          "LongText"
        ],
        [
          "_score",
          "Int32"
        ]
      ],
      [
        3,
        "医療支援の英退役軍人、自伝「明日はきっと良い日に」執筆",
        1
      ],
      [
        4,
        "米、加・メキシコとのコロナ渡航制限継続　来月21日まで",
        1
      ],
      [
        5,
        "トランプ氏、来年4月までに全国民分のコロナワクチン確保へ",
        1
      ]
    ]
  ]
]
```

検索結果の並べ替え


CMD
```
$ groonga $HOME/groongadb/testdb select --table test_tbl --output_columns _key,TITLE_NAME,DATE_TIME,_score --query 'EXTRACT_SITE_NAME:@ロイター' --offset 2 --limit 3 --sort_keys _score,-DATE_TIME,_id | jq
```

OUT

```
[
  [
    0,
    1600738659.282179,
    0.02016258239746094
  ],
  [
    [
      [
        5
      ],
      [
        [
          "_key",
          "UInt32"
        ],
        [
          "TITLE_NAME",
          "LongText"
        ],
        [
          "DATE_TIME",
          "LongText"
        ],
        [
          "_score",
          "Int32"
        ]
      ],
      [
        5,
        "トランプ氏、来年4月までに全国民分のコロナワクチン確保へ",
        "2020年9月19日",
        1
      ],
      [
        2,
        "英、コロナ第2波不可避　新たな措置実施も＝ジョンソン首相",
        "2020年9月18日",
        1
      ],
      [
        3,
        "医療支援の英退役軍人、自伝「明日はきっと良い日に」執筆",
        "2020年9月18日",
        1
      ]
    ]
  ]
]
```
