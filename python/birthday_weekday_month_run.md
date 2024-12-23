# Same Birthday, Weekday, Month Probability

မွေးနေ့ မွေးလ မွေးရက် တူနိုင်တဲ့ chance ကို probability နဲ့ တွက်ကြည့်ခဲ့တယ်။ ပြီးတော့ Monte Carlo Simulation နဲ့လည်း ပြန် confirmation လုပ်ကြည့်ခဲ့တယ်။  

## for birthday_weekday_month_prob.py

```
(base) ye@lst-gpu-server-197:~/ye/exp/this-and-that$ python ./birthday_weekday_month_prob.py --help
usage: birthday_weekday_month_prob.py [-h] [--days_in_year DAYS_IN_YEAR] [--days_in_week DAYS_IN_WEEK]
                                      [--months_in_year MONTHS_IN_YEAR]
                                      num_people

Calculate the probability of shared birthdays, weekdays, or months.

positional arguments:
  num_people            Number of people to consider.

optional arguments:
  -h, --help            show this help message and exit
  --days_in_year DAYS_IN_YEAR
                        Number of days in a year (default: 365).
  --days_in_week DAYS_IN_WEEK
                        Number of days in a week (default: 7).
  --months_in_year MONTHS_IN_YEAR
                        Number of months in a year (default: 12).
(base) ye@lst-gpu-server-197:~/ye/exp/this-and-that$
```

```
(base) ye@lst-gpu-server-197:~/ye/exp/this-and-that$ python ./birthday_weekday_month_prob.py 2
Probability of at least two people sharing the same day of the week among 2 people: 0.142857
That is approximately 14.29% chance.
Probability of at least two people sharing the same month of birth among 2 people: 0.083333
That is approximately 8.33% chance.
Probability of at least two people sharing the same birthday among 2 people: 0.002740
That is approximately 0.27% chance.
(base) ye@lst-gpu-server-197:~/ye/exp/this-and-that$
```

```
(base) ye@lst-gpu-server-197:~/ye/exp/this-and-that$ python ./birthday_weekday_month_prob.py 10
Probability of at least two people sharing the same day of the week among 10 people: 1.000000
That is approximately 100.00% chance.
Probability of at least two people sharing the same month of birth among 10 people: 0.996132
That is approximately 99.61% chance.
Probability of at least two people sharing the same birthday among 10 people: 0.116948
That is approximately 11.69% chance.
(base) ye@lst-gpu-server-197:~/ye/exp/this-and-that$
```

## for shared_date_simulation.py

```
(base) ye@lst-gpu-server-197:~/ye/exp/this-and-that$ python ./shared_date_simulation.py --help
usage: shared_date_simulation.py [-h] [--trials TRIALS] num_people

Simulate probabilities of shared dates.

positional arguments:
  num_people       Number of people for the simulation.

optional arguments:
  -h, --help       show this help message and exit
  --trials TRIALS  Number of simulation trials to run (default: 100,000).
(base) ye@lst-gpu-server-197:~/ye/exp/this-and-that$
```

```
(base) ye@lst-gpu-server-197:~/ye/exp/this-and-that$ python ./shared_date_simulation.py 2
Simulated Probability (Same Day of Week, 2 people): 0.146030
Simulated Probability (Same Month, 2 people): 0.084070
Simulated Probability (Same Birthday, 2 people): 0.002870
(base) ye@lst-gpu-server-197:~/ye/exp/this-and-that$
```

```
(base) ye@lst-gpu-server-197:~/ye/exp/this-and-that$ python ./shared_date_simulation.py 10
Simulated Probability (Same Day of Week, 10 people): 1.000000
Simulated Probability (Same Month, 10 people): 0.995700
Simulated Probability (Same Birthday, 10 people): 0.117600
(base) ye@lst-gpu-server-197:~/ye/exp/this-and-that$
```
