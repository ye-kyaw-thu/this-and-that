# Finite Difference

```
(base) C:\Users\ye\.spyder-py3>python finite_difference.py 3
x       f(x)    1st diff        2nd diff
1       1       3       2
2       4       5       2
3       9       7

Calculation:
next_first_difference = first_differences[-1] + second_differences[-1]
9 = 7 + 2
next_fx_value = fx_values[-1] + next_first_difference
25 = 16 + 9

The square of 4 is 25 according to the method of finite differences.
```

```
(base) C:\Users\ye\.spyder-py3>python finite_difference.py 4
x       f(x)    1st diff        2nd diff
1       1       3       2
2       4       5       2
3       9       7       2
4       16      9

Calculation:
next_first_difference = first_differences[-1] + second_differences[-1]
11 = 9 + 2
next_fx_value = fx_values[-1] + next_first_difference
36 = 25 + 11

The square of 5 is 36 according to the method of finite differences.
```

```
(base) C:\Users\ye\.spyder-py3>python finite_difference.py 5
x       f(x)    1st diff        2nd diff
1       1       3       2
2       4       5       2
3       9       7       2
4       16      9       2
5       25      11

Calculation:
next_first_difference = first_differences[-1] + second_differences[-1]
13 = 11 + 2
next_fx_value = fx_values[-1] + next_first_difference
49 = 36 + 13

The square of 6 is 49 according to the method of finite differences.

(base) C:\Users\ye\.spyder-py3>
```
