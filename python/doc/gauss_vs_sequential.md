# The formula for the sum of an arithmetic progression or arithmetic series

ငယ်ရွယ်သေးတဲ့ သင်္ချာပညာရှင် Carl Friedrich Gauss ကို သူ့ဆရာက လေးစားခဲ့ရတယ်လို့ သင်္ချာသမိုင်းမှာ တွင်ကျန်ရစ်ခဲ့တဲ့ ဂဏန်းတွေကို အစဉ်လိုက်ပေါင်းဖို့အတွက် သုံးခဲ့တဲ့ ဖြတ်လမ်း နည်းတစ်ခုရှိတယ်။   
ဥပမာ အောက်ပါလိုမျိုး ၁ ကနေ ၁၀ အထိ ဂဏန်းတွေကို အစဉ်လိုက် ပေါင်းခိုင်းတယ် ဆိုပါစို့ ...  

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10  

အဲဒါကို Gauss က နံပါတ်တွေကို တဝက်ဖြတ်ချလိုက်ပြီးရင် အတွဲတစ်တွဲစီကို အောက်ပါအတိုင်း တွဲပေါင်းရင် တူတဲ့ နံပါတ်တွေ ထွက်တယ်ဆိုတာကို ဂရုပြုမိပါတယ်။    

1 + 10 = 11  
2 + 9 = 11  
3 + 8 = 11  
4 + 7 = 11  
5 + 6 = 11  

အဲဒီပေါင်းလဒ်ကိုမှ စုစုပေါင်း နံပါတ်အတွဲက ဒီဥပမာမှာ ဆိုရင် ၅တွဲရှိတာမို့လို့၊ ၅နဲ့မြှောက်ရင် ၁ ကနေ ၁၀ အထိကို တစ်လုံးချင်းပေါင်းတဲ့ အဖြေနဲ့ အတူတူပဲ ဆိုပြီးတွက်တဲ့နည်းလမ်းပါ။  

5 x 11 = 55  

၁ ကနေ ၁၀ အထိ ပေါင်းတဲ့ကိစ္စမှာ တွက်ရတဲ့အချိန်က သိပ်ကွာမှာ မဟုတ်ပေမဲ့ ၁ ကနေ ၁၀၀ တို့ ၁၀၀၀ တို့ ပေါင်းမယ် ဆိုရင်တော့ Gauss ရဲ့ နည်းလမ်းက တကယ်အသုံးဝင်ပါတယ်။  
ဖော်မြူလာ အနေနဲ့က အောက်ပါလိုမျိုး ချရေးနိုင်တယ်။  

50 (pairs) x 101 (sum of each pair) = 5050

1 to n အတွက် generalized လုပ်ထားတဲ့ formula က အောက်ပါအတိုင်း။  

Sum = n/2 * (first number + last number)  

ဒီ formula ကို သုံးပြီးတော့ ၁ ကနေ ၁၀၀ အထိ ပေါင်းတာကို တွက်မယ် ဆိုရင် အောက်ပါအတိုင်း တွက်လို့ ရပါလိမ့်မယ်။  

Sum = 100/2 * (1 + 100)  
Sum = 50 * 101  
Sum = 5050  

## Complexity Measurement

Python code ရေးကြည့်ပြီးတော့ နံပါတ်တွေကို အစဉ်းလိုက် အမျိုးမျိုး ပေါင်းခိုင်းကြည့်ရင် ပုံမှန်ပေါင်းတာနဲ့ Gauss ရဲ့ နည်းနဲ့ ပေါင်းတာမှာ ကြာချိန်မတူတာကို ရှင်းရှင်လင်းလင်း မြင်ရပါလိမ့်မယ်။   
ကွန်ပျူတာ သမားတွေအနေနဲ့ algorithm complexity ကို Big O notation နဲ့ ရေးရင်တော့ 

### Gauss' Method (gauss_sum function):

Time Complexity: O(1) - ဘာကြောင့်လဲ ဆိုတော့ Gauss function မှာက n (which is end - start) က ပြောင်းသွားသည့်တိုင်အောင် operation က အမြဲတမ်း constant မို့လို့ပါ။   
Space Complexity: O(1) - Memory/space အနေနဲ့ ကြည့်မယ် ဆိုရင်လည်း သူယူမယ့် space size က သတ်မှတ်ပြီးသားပါ။ ဆိုလိုတာက n တန်ဖိုးက ပြောင်းလဲရင်လည်း သက်ရောက်မှု မရှိလို့ပါ။  

### Sequential Method (sequential_sum function):

Time Complexity: O(n) - ဘာကြောင့်လဲ ဆိုတော့ ဒီ function မှာက loop ရှိနေပြီးတော့ loop ပတ်ရမယ့် အရေအတွက်က n တန်ဖိုး (i.e. start to end) ပေါ်မူတည်နေလို့ပါ။  
Space Complexity: O(1) - operation အရေအတွက်မှာက n ပေါ်ကို မူတည်ပြီး အပြောင်းအလဲ ရှိပေမဲ့၊ memory/space အနေနဲ့ကတော့ အပြောင်းအလဲ မရှိပါဘူး။ ဘာကြောင့်လဲ ဆိုတော့ စုစုပေါင်း ပေါင်းလို့ ရလာတဲ့ တန်ဖိုးကိုသိမ်းဖို့ တနေရာပဲ သုံးမှာ မလို့ပါ။  

## Running Examples

```
(base) ye@lst-gpu-3090:~/exp/demo$ python ./gauss_vs_sequential.py 1 100
Gauss Method: Sum = 5050, Time = 0.000001 seconds, Complexity: O(1)
Sequential Method: Sum = 5050, Time = 0.000003 seconds, Complexity: O(n)
```

```
(base) ye@lst-gpu-3090:~/exp/demo$ python ./gauss_vs_sequential.py 1 1000000
Gauss Method: Sum = 500000500000, Time = 0.000001 seconds, Complexity: O(1)
Sequential Method: Sum = 500000500000, Time = 0.016882 seconds, Complexity: O(n)
```

```
(base) ye@lst-gpu-3090:~/exp/demo$ python ./gauss_vs_sequential.py 1 100000000
Gauss Method: Sum = 5000000050000000, Time = 0.000001 seconds, Complexity: O(1)
Sequential Method: Sum = 5000000050000000, Time = 1.659063 seconds, Complexity: O(n)
```

```
(base) ye@lst-gpu-3090:~/exp/demo$ python ./gauss_vs_sequential.py 1 1000000000
Gauss Method: Sum = 500000000500000000, Time = 0.000001 seconds, Complexity: O(1)
Sequential Method: Sum = 500000000500000000, Time = 16.644614 seconds, Complexity: O(n)
```

