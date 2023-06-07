# How to run pascal-triangle-sql.py

```
(base) rnd@gpu:~/demo/pascal-triangle$ python pascal-triangle-sql.py 5 standard
```

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

```

```

```

```

```

```
