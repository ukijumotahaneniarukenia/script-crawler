IN

```
$ groonga $HOME/groongadb/testdb select --table test_tbl | jq 
[
  [
    0,
    1600740737.768951,
    0.0003948211669921875
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

CMD

```
$ groonga $HOME/groongadb/testdb select --table test_tbl | jq '.[1][] as $result|$result[1]|map(.[0]) as $column_list|$column_list|$column_list | length as $column_cnt|$result[1]|map(.[1]) as $type_list|$type_list|$result[2:] as $row_list|$row_list | length as $row_cnt | [range(0;$row_cnt)]|map(. as $row|[range(0;$column_cnt)]|map(. as $col|{($column_list[$col]):($row_list[$row][$col])}))[]|reduce .[] as $entry({};.+$entry)'
```

OUT
```
{
  "_id": 1,
  "_key": 1,
  "DATE_TIME": "2020年9月19日 / 06:47 / 18時間前更新",
  "EXTRACT_BASE_NAME": "com-reuters-jp",
  "EXTRACT_SITE_NAME": "ロイター",
  "EXTRACT_SITE_URL": "https://jp.reuters.com/",
  "EXTRACT_URL_NAME": "https://jp.reuters.com////jp.reuters.com/article/usa-fed-framework-idJPKBN26936J",
  "ID": 1,
  "TITLE_NAME": "米ＦＲＢ新戦略、国民に浸透せず　2重の責務も誤解＝調査"
}
{
  "_id": 2,
  "_key": 2,
  "DATE_TIME": "2020年9月18日",
  "EXTRACT_BASE_NAME": "com-reuters-jp",
  "EXTRACT_SITE_NAME": "ロイター",
  "EXTRACT_SITE_URL": "https://jp.reuters.com/",
  "EXTRACT_URL_NAME": "https://jp.reuters.com//article/health-coronavirus-britain-idJPKBN2691EU",
  "ID": 2,
  "TITLE_NAME": "英、コロナ第2波不可避　新たな措置実施も＝ジョンソン首相"
}
{
  "_id": 3,
  "_key": 3,
  "DATE_TIME": "2020年9月18日",
  "EXTRACT_BASE_NAME": "com-reuters-jp",
  "EXTRACT_SITE_NAME": "ロイター",
  "EXTRACT_SITE_URL": "https://jp.reuters.com/",
  "EXTRACT_URL_NAME": "https://jp.reuters.com//article/health-coronavirus-britain-veteran-idJPKBN2690II",
  "ID": 3,
  "TITLE_NAME": "医療支援の英退役軍人、自伝「明日はきっと良い日に」執筆"
}
{
  "_id": 4,
  "_key": 4,
  "DATE_TIME": "2020年9月19日",
  "EXTRACT_BASE_NAME": "com-reuters-jp",
  "EXTRACT_SITE_NAME": "ロイター",
  "EXTRACT_SITE_URL": "https://jp.reuters.com/",
  "EXTRACT_URL_NAME": "https://jp.reuters.com//article/health-coronavirus-usa-canada-idJPKBN2692T1",
  "ID": 4,
  "TITLE_NAME": "米、加・メキシコとのコロナ渡航制限継続　来月21日まで"
}
{
  "_id": 5,
  "_key": 5,
  "DATE_TIME": "2020年9月19日",
  "EXTRACT_BASE_NAME": "com-reuters-jp",
  "EXTRACT_SITE_NAME": "ロイター",
  "EXTRACT_SITE_URL": "https://jp.reuters.com/",
  "EXTRACT_URL_NAME": "https://jp.reuters.com//article/health-coronavirus-usa-trump-idJPKBN26931V",
  "ID": 5,
  "TITLE_NAME": "トランプ氏、来年4月までに全国民分のコロナワクチン確保へ"
}
```
