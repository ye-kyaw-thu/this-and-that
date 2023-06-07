# How to Run pascal-triangle.py

```
(base) rnd@gpu:~/demo/pascal-triangle$ python ./pascal-triangle.py 5 standard out.txt
      1
     1   1
    1   2   1
   1   3   3   1
  1   4   6   4   1
 1   5   10   10   5   1
 ```
 
 ```
(base) rnd@gpu:~/demo/pascal-triangle$ python ./pascal-triangle.py 5 hypercubes out.txt
      1
     1   1
    1   3   1
   1   5   7   1
  1   7   17   15   1
 1   9   31   49   31   1
(base) rnd@gpu:~/demo/pascal-triangle$
```

out.txt ဖိုင်ကို ရိုက်ထုတ်ကြည့်လျင် ...  

```
(base) rnd@gpu:~/demo/pascal-triangle$ cat out.txt
      1
     1   1
    1   3   1
   1   5   7   1
  1   7   17   15   1
 1   9   31   49   31   1
(base) rnd@gpu:~/demo/pascal-triangle$
```

## Help Screen

```
(base) rnd@gpu:~/demo/pascal-triangle$ python ./pascal-triangle.py -h
usage: pascal-triangle.py [-h] n type file_name

positional arguments:
  n           Number of rows for Pascal's Triangle
  type        Type of Pascal's Triangle (standard, hypercubes)
  file_name   Name of the file to save the triangle

optional arguments:
  -h, --help  show this help message and exit
(base) rnd@gpu:~/demo/pascal-triangle$
```
