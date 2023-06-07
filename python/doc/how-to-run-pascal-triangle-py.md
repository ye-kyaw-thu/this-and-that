# How to run pascal-triangle-sql.py

Help screen ကတော့ -h or --help option နဲ့ ခေါ်ကြည့်လို့ ရပါတယ်။  

```
(base) rnd@gpu:~/demo/pascal-triangle$ python ./pascal-triangle-sql.py -h
usage: pascal-triangle-sql.py [-h] n type

positional arguments:
  n           Number of rows for Pascal's Triangle
  type        Type of Pascal's Triangle (standard, hypercubes)

optional arguments:
  -h, --help  show this help message and exit
(base) rnd@gpu:~/demo/pascal-triangle$
```

Standard သို့မဟုတ် ပုံမှန် Pascal's Triangle ကို Row ၅ခုနဲ့ ဆောက်မယ် ဆိုရင် ...  

```
(base) rnd@gpu:~/demo/pascal-triangle$ python pascal-triangle-sql.py 5 standard
```

output file အဖြစ် ရလာတဲ့ pascal.db SQLite database ကို access လုပ်တဲ့ ဥပမာ က အောက်ပါအတိုင်းပါ။  

```
(base) rnd@gpu:~/demo/pascal-triangle$ sqlite3 pascal.db
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> SELECT * FROM PascalTriangle ORDER BY Row, Column;
0|0|1
1|0|1
1|1|1
2|0|1
2|1|2
2|2|1
3|0|1
3|1|3
3|2|3
3|3|1
4|0|1
4|1|4
4|2|6
4|3|4
4|4|1
5|0|1
5|1|5
5|2|10
5|3|10
5|4|5
5|5|1
sqlite> .exit
(base) rnd@gpu:~/demo/pascal-triangle$
```

ဒီတစ်ခါတော့ hypercubes ဆိုတဲ့ option ပေးပြီးတော့ Pascal's Triangle ကို ဆောက်ခိုင်းကြည့်မယ်။  
မဆောက်ခင်မှာ အရင် ရှိပြီးသား pascal.db ဖိုင်ကိုတော့ ဖျက်ပေးဖို့တော့ လိုအပ်လိမ်မယ်။  

```
(base) rnd@gpu:~/demo/pascal-triangle$ rm pascal.db
(base) rnd@gpu:~/demo/pascal-triangle$ python pascal-triangle-sql.py 5 hypercubes
```

output ဖိုင်အဖြစ် ထွက်လာတဲ့ pascal.db SQLite database ဖိုင်နဲ့ အထက်မှာတုန်းက standard option နဲ့ run ပြီးထွက်လာတာကို နှိုင်းယှဉ်ကြည့်ပါ။  

```
(base) rnd@gpu:~/demo/pascal-triangle$ sqlite3 pascal.db
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> SELECT * FROM PascalTriangle ORDER BY Row, Column;
0|0|1
1|0|1
1|1|1
2|0|1
2|1|3
2|2|1
3|0|1
3|1|5
3|2|7
3|3|1
4|0|1
4|1|7
4|2|17
4|3|15
4|4|1
5|0|1
5|1|9
5|2|31
5|3|49
5|4|31
5|5|1
sqlite> .exit
(base) rnd@gpu:~/demo/pascal-triangle$
```

SQLite database အနေနဲ့ သိမ်းထားတဲ့ ရည်ရွယ်ချက်က triangle အကြီးကြီးတွေအတွက် ဖြစ်တာမို့လို့ ကိုယ့် access လုပ်ချင်တဲ့ row ကို ခေါ်ကြည့်တာမျိုး လုပ်လို့ ရပါတယ်။  

```
(base) rnd@gpu:~/demo/pascal-triangle$ sqlite3 pascal.db
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> SELECT * FROM PascalTriangle WHERE Row = 4;
4|0|1
4|1|7
4|2|17
4|3|15
4|4|1
sqlite> SELECT * FROM PascalTriangle WHERE Row = 2;
2|0|1
2|1|3
2|2|1
sqlite> .exit
(base) rnd@gpu:~/demo/pascal-triangle$
```

