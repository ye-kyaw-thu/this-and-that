# Brief Explanation for find-several-nearest-with-voronoi.py

ဒီ code ကတော့ တကယ်က find-nearest-with-voronoi.py ကို distance calculation method လေးမျိုး ထပ်ဖြည့်ပြီးတော့ တွက်ပြထားတာပါ။ အဲဒါကြောင့် ဒီပရိုဂရမ်မှာတော့ distance တွက်တဲ့ အပိုင်းကို အောက်ပါ ၅မျိုးနဲ့ တွက်ပြပေးပါလိမ့်မယ်။  

1. Euclidean distance
2. Manhattan distance
3. Chebyshev distance
4. Minkowski distance
5. Cosine distance

## How to run

```
python find-nearest-with-voronoi.py
```

ဆေးရုံရဲ့ တည်နေရာ 2D x, y တန်ဖိုးတွေကို အရင်ပရိုဂရမ်နဲ့ အတူတူပေးထားတာမို့ ထွက်လာတဲ့ Voronoi diagram ကလည်း အောက်ပါအတိုင်း အတူတူပဲ ရရှိပါလိမ့်မယ်။ 

<p float="left">
   <img src="https://github.com/ye-kyaw-thu/this-and-that/blob/main/python/fig/voronoi-diagram.png" width="500" />
</p>

ကိုယ့် အိမ်ရဲ့ x, y coordinate တွေကို ၆၊ ၅ လို့ ပေးလိုက်ရင်တော့ အောက်ပါအတိုင်း အနီးဆုံး ဆေးရုံရဲ့ တည်နေရာ ရလဒ်တွေကို တွက်ထုတ်ပေးပါလိမ့်မယ်။  

```
Please input the coordinates of your residence (two numbers separated by a space):
6 5
The nearest location to your residence using euclidean distance is at [5. 4.]
The nearest location to your residence using manhattan distance is at [5. 4.]
The nearest location to your residence using chebyshev distance is at [5. 4.]
The nearest location to your residence using minkowski distance is at [5. 4.]
The nearest location to your residence using cosine distance is at [7. 6.]
```

မှတ်ချက်။ ။ Cosine distance ကတော့ တခြား distance calculation method တွေနဲ့ မတူတဲ့ ဆေးရုံကို ညွှန်ပြတာကို တွေ့ရပါလိမ့်မယ်။  
