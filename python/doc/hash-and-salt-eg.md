# How to Run

User နှစ်ယောက်က password ကို တူတာမျိုးလည်း ဖြစ်နိုင်တယ်လေ။ အဲဒီလို ပြဿနာမျိုးအတွက် password တစ်ခုတည်းကိုပဲ encrypt လုပ်ပြီး သိမ်းတာမျိုး လက်တွေ့မှာ မလုပ်ကြပါဘူး။ User ရဲ့ password အပြင် ကျပန်း hash code တစ်ခုကိုပါ ထပ်ဖြည့်ပြီးမှ တွဲပြီးသိမ်းလေ့ရှိပါတယ်။ အဲဒီ အလုပ်ကို python code နဲ့ ရေးကြည့်ထားတာပါ။  

Running example ကတော့ ...  
username နဲ့ password မှန်ရင် login ဝင်လို့ ရလိမ့်မယ်။  

```
>python hash-and-salt-eg.py
Enter your username: user1
Enter your password:
Login successful!
```

password ကို ဆက်တိုက်မှားရင် အဲဒီ user ကို အချိန်အတိုင်းအတာ တစ်ခုထိ login ဝင်လို့ မရအောင် လုပ်ရလိမ့်မယ်။  

```
>python hash-and-salt-eg.py
Enter your username: user2
Enter your password:
Incorrect password.
Enter your password:
Incorrect password.
Enter your password:
Incorrect password.
Too many failed attempts. Try again later.
```

username, salt, password တွေကို plain json ဖိုင်နဲ့ သိမ်းပြထားတာပါ။  
လက်တွေ့မှာက encryption သေသေချာချာ လုပ်ပြီးမှ သိမ်းထားတာပါ။  

```
>type user_data.json
{"user1": {"salt": "acc697ad1a2b4eae460243505532ae76", "hash": "2d415fadb8aa1af70fd8e1b2a12517338ae1850f72da7a7f27d2be1e46a9cfec"}, "user2": {"salt": "6621ee17c38aac3f800c73424d82250a", "hash": "85814273a0b2384be19777f243075582741de0813bc4792ccc15b93829bbae88"}, "user3": {"salt": "556882c9469f659bb58c752ff7913cd5", "hash": "5740ed384b3cf692e20b115e92ef9a193854b1dd3bf3936bbd393ca929c118dc"}}
```
