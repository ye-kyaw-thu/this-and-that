# What is Voronoi Diagram

Voronoi diagrams ဆိုတာက Georgy Voronoy ဆိုတဲ့ ရုရှား (ယူကရိန်း လူမျိုး) သင်္ချာပညာရှင် က ပေးခဲ့တဲ့ နာမည်ပါ။ Computational geometry (တွက်ချက်မှုဆိုင်ရာ ဂျီဩမေတြီ) မှာတော့ တော်တော်လေး ထင်ရှားတဲ့ အယူအဆ တစ်ခုဖြစ်ပါတယ်။ အတိုရှင်းပြရရင်တော့ space တစ်ခုကို ပေးလိုက်တဲ့ seed point တွေပေါ်ကို မူတည်ပြီး partition တွေ ခွဲပြီး ဆွဲပြပေးထားတဲ့ ပုံပါ။ ဒီနေရာမှာ seed point ဆိုတာက အမျိုးမျိုး ဖြစ်နိုင်ပါတယ်။ ဥပမာ 2D seed point အနေနဲ့ ဆိုရင် x, y ပွိုင့်တွေလည်း ဖြစ်နိုင်ပါတယ်။ Partition တွေခွဲထားတဲ့ ဧရိယာ တစ်ပိုင်း တစ်ပိုင်းချင်းစီက ပေးထားတဲ့ x, y ပွိုင့်တွေ ရဲ့ တစ်ခုနဲ့ တစ်ခုအကြား အနီးဆုံး ဆိုတဲ့ ပွိုင့်တွေကို အခြေခံပြီးတော့မှ ခွဲထားတာ ဖြစ်ပါတယ်။ သင်္ချာမှာတော့ proximity to seed points လို့ ခေါ်ပါတယ်။ အဲဒီလို Voronoi diagram ဆွဲဖို့အတွက် နာမည်ကြီးတဲ့ algorithm တွေ ရှိပါတယ်။ အဲဒါတွေကတော့ အောက်ပါအတိုင်းပါ။   

1. Fortune's Algorithm
2. Bowyer-Watson Algorithm
3. Incremental Algorithm
4. Divide and Conquer Algorithm

အဲဒီ လေးမျိုးအထဲမှာ ဆိုရင်တော့ နံပါတ် (၁) Fortune's Algorithm ကတော့ လူသိအများဆုံးလို့ ပြောကြပါတယ်။ ကိုယ်တိုင် ဒီ algorithm တွေကို code ရေးပြီး implementation လုပ်မယ် ဆိုရင်တော့ သင်္ချာအပိုင်းရော coding အပိုင်းရော အချိန်ယူပြီး လုပ်ကြရပါလိမ့်မယ်။ Python မှာတော့ Voronoi diagram ဆွဲဖို့အတွက်က library တွေ ရှိပြီးသားမို့လို့ ယူသုံးပြီး Voronoi diagram ကို အလွယ်တကူ ဆွဲလို့ ရပါတယ်။

```python
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 11:51:18 2023

@author: Ye Kyaw Thu, LST, NECTEC, Thailand
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Generate random points
points = np.random.rand(15, 2)

# Calculate Voronoi Diagram
vor = Voronoi(points)

# Plot Voronoi diagram
voronoi_plot_2d(vor)

# Also plot the input points
plt.plot(points[:,0], points[:,1], 'ro')

plt.show()
```

အထက်ပါ Python code ကို run ရင် အောက်ပါလိုမျိုး Voronoi diagram တွေကို ဆွဲပေးပါလိမ့်မယ်။  

<p float="left">
  <img src="https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/random-voronoi-diagram1.png" width="500" />
  <img src="https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/random-voronoi-diagram2.png" width="500" /> 
  <img src="https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/random-voronoi-diagram3.png" width="500" />
   <img src="https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/random-voronoi-diagram4.png" width="500" />
</p>

## Brief Explanation of How to Run find-nearest-with-voronoi.py

ဒီ ဥပမာ Python code ကတော့ ဧရိယာ တစ်ခုမှာ ရှိတဲ့ ဆေးရုံ ခြောက်လုံး နေရာတွေကို 2D x, y position တွေ ပေးလိုက်ပြီးတော့ Vonoroi diagram ဆွဲကြည့်ပါတယ်။ ပြီးတော့မှ user ကပြောတဲ့ သူ့ အိမ်နေရာ x, y point ကို လက်ခံယူပြီး သူ့အိမ်နဲ့ အနီးဆုံး ဆေးရုံရဲ့ နေရာကို တွက်ချက်ပေးတာပါ။ Nearest distance ကို တွက်တဲ့ နေရာမှာတော့ Euclidean distances ကို သုံးထားပါတယ်။

[find-nearest-with-voronoi.py](https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/find-nearest-with-voronoi.py) ပရိုဂရမ်ရဲ့ runnning example ကတော့ အောက်ပါအတိုင်းပါ။  

python find-nearest-with-voronoi.py

The following Voronoi diagram will plot:  

<p float="left">
   <img src="https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/voronoi-diagram.png" width="500" />
</p>

## After that, you will get the following prompt for asking two numbers

```
Please input the coordinates of your residence (two numbers separated by a space):
5 3
The nearest location to your residence is at [5. 4.]
```

ရိုက်ထည့်ပေးလိုက်တဲ့ 5, 3 အတွက် အနီးဆုံး ဆေးရုံက 5, 4 နေရာလို့ ပရိုဂရမ်က တွက်ပေးပါတယ်။  

## If you typed 5 and 5.5 

```
Please input the coordinates of your residence (two numbers separated by a space):
5 5.5
The nearest location to your residence is at [5. 4.]
```

ရိုက်ထည့်ပေးလိုက်တဲ့ 5, 5.5 အတွက် အနီးဆုံး ဆေးရုံကိုလည်း 5, 4 နေရာလို့ ပရိုဂရမ်က တွက်ပေးပါတယ်။  

## Reference

1. https://en.wikipedia.org/wiki/Voronoi_diagram
