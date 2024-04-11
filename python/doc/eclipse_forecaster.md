# Try to Predict Next Eclipse Date

## 1st Version

[eclipse_forecaster.py](https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/eclipse_forecaster.py)    

```python

```

## Example Usage or Running Results with the Code (1st version)

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py "Phnom Penh" Cambodia
Next solar eclipse visible from Phnom Penh, Cambodia: 2031-05-21 10:05:35.789874
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py Mandalay Myanmar
Next solar eclipse visible from Mandalay, Myanmar: 2053-09-12 10:05:45.561972
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py Kyoto Japan
Next solar eclipse visible from Kyoto, Japan: 2059-11-05 10:05:58.648681
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py "New York" American
Next solar eclipse visible from New York, American: 2025-03-29 10:06:10.459513
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py Bagan Myanmar
Next solar eclipse visible from Bagan, Myanmar: 2053-09-12 10:06:19.684058
```

## Note

သတိထားစေချင်တာက ဒီ တွက်ထားတဲ့ ပရိုဂရမ်က ကျွန်တော်စိတ်ဝင်စားလို့ Python library သုံးခုကို သုံးပြီးစမ်းထားတာပါ။ အချိန်တို့ ရက်တို့က အမှန်တကယ် eclipse ဖြစ်တာနဲ့လွဲသွားနိုင်တာတွေ ရှိနိုင်ပါတယ်။ တကယ်ကတော့ eclipse ရက်ကို တွက်တဲ့ နည်းလမ်းတွေက တစ်မျိုးထက်မကရှိပါတယ်။ ပြီးတော့ sea level ကို ထည့်တာနဲ့ မထည့်တာနဲ့မှာ ရလဒ်က ကွဲသွားနိုင်တယ်။ ဥပမာ ဒီအောက်က ရလဒ်တွေက sea level ကို ထည့်မစဉ်းစားပဲ ရေးထားတဲ့ code ကို run ကြည့်တုန်းက ရတဲ့ ရလဒ်တွေပါ။ ဗဟုသုတရအောင်လို့ ယှဉ်ကြည့်နိုင်အောင်လို့ ...  

### Results without Sea level Information

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py "Phnom Penh" Cambodia
Next solar eclipse visible from Phnom Penh, Cambodia: 2031-05-21 09:57:32.352972
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py Mandalay Myanmar
Next solar eclipse visible from Mandalay, Myanmar: 2059-11-05 09:57:44.626437
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py Kyoto Japan
Next solar eclipse visible from Kyoto, Japan: 2059-11-05 09:57:56.366491
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py "New York" American
Next solar eclipse visible from New York, American: 2025-03-29 09:58:13.720870
```

```
(base) yekyaw.thu@gpu:~/tmp$ python ./eclipse_forecaster.py Bagan Myanmar
Next solar eclipse visible from Bagan, Myanmar: 2059-11-05 09:58:24.353944
```

