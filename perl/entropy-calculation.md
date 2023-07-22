# Entropy Calculation

Entropy ဆိုတာက information theory မှာ အရေးကြီးတဲ့ တွက်ချက်မှုတစ်ခုပါ။ Entropy ဆိုတဲ့ သိပ္ပံဆိုင်ရင်ရာ အတွေးအခေါ်ကို ပထမဆုံး propose လုပ်ခဲ့တဲ့သူက information theory ရဲ့ ဖခင်လို့ တင်စားပြောကြတဲ့ ဒေါက်တာ Claude Elwood Shannon ပါ။ အဲဒါကြောင့်မို့လို့ Shannon Entropy လို့လည်း သုံးကြပါတယ်။ စာတမ်းက ၁၉၄၈ခုနှစ်မှာ ထုတ်ဝေခဲ့ပြီး "A Mathematical Theory of Communication" ဆိုတဲ့ ခေါင်းစဉ်နဲ့ပါ။ ကွန်ပျူတာလောကမှာ ဒေတာတွေကို သိမ်းဖို့ ပို့ဖို့ (i.e. communication) လုပ်တဲ့အခါမှာ သုံးကြတဲ့ 0, 1 (bits) ဆိုတာကလည်း ဒီဆရာကြီးရဲ့ သုတေသန ကနေ လာတာပါပဲ။     

Wiki မှာတော့ entorpy ဆိုတာကို အင်္ဂလိပ်လိုတော့ အောက်ပါအတိုင်း ရှင်းပြထားပါတယ်။  

In information theory, the entropy of a random variable is the average level of "information", "surprise", or "uncertainty" inherent to the variable's possible outcomes.  

ကွန်ပျူတာသမားတွေအတွက် နားလည်သလို ပြန်ရှင်းပြရရင် communication လုပ်မယ့် (ဥပမာ။ ။ အဲဒီခေတ်အချိန်ကအတိုင်း ပြောရရင် တနေရာကနေ တနေရာကို စာကြောင်းတစ်ကြောင်း ပို့ဖို့အတွက် ...) စာကြောင်းကို encode လုပ်ဖို့အတွက် ပျမ်းမျှ bit အနည်းဆုံး ဘယ်လောက် လိုအပ်မလဲ ဆိုတာကို ခန့်မှန်းတွက်ချက်တာပါ။ Estimation of average minimum number of bits ပါ။ ဖော်မြူလာ အနေနဲ့ ဆိုရင်တော့ အောက်ပါပုံစံမျိုး ရေးလို့ ရပါတယ်။  

$$
\begin{align}
\Huge H(X) = \sum_\limits{i=1}^{n} p(x_{i}) I(x_{i})    
\Huge = \sum_\limits{i=1}^{n} p(x_{i}) \log_b \frac{1}{p(x_{i})}    
\Huge = - \sum_\limits{i=1}^{n} \log_{b}p(x_{i})   
\end{align}
$$

y ဆိုတဲ့ စာလုံး (ရဲကျော်သူ ရဲ့ အတိုကောက်အနေနဲ့ သုံးတာပါ) ကို တနေရာရာကို ပို့မယ် ဆိုပြီး စဉ်းစားကြည့်ကြရအောင်။  
y က binary လိုပြောင်းရေးရင် 01111001 ပါ။  

binary system ကို သုံးတာမို့လို့ ငါတို့ရဲ့ input string မှာက သင်္ကတေ နှစ်မျိုးပဲ ရှိပါတယ်။ အဲဒါကတော့ "0" နဲ့ "1" ပါပဲ။
Entropy တွက်မယ် ဆိုရင် အရင်ဆုံး input လုပ်လိုက်တဲ့ စာကြောင်းထဲမှာ ပါနေတဲ့ စာလုံး သို့မဟုတ် သင်္ကေတတွေအတွက် frequencies ကို တွက်ရပါတယ်။ အကြိမ်အရေအတွက်ကို စာကြောင်းရဲ့ အရှည် (string length) နဲ့ စားတာပါ။    

သုည က input string မှာ သုံးခါပါတာမို့၊ သုညအတွက် frequency က 3/8 = 0.375 ပါ။  
တစ် စာလုံးအတွက်က စုစုပေါင်း ငါးခါ ပါနေတာမို့လို့၊ တစ်အတွက် frequency က 5/8 = 0.625 ပါ။   

အထက်က ဖော်မြူလာကို သုံးပြီးတော့ Shannon entropy ကို အောက်ပါအတိုင်း တွက်လို့ ရပါတယ်။  

$H(X) = -[(0.375*\log_{2}(0.375))+(0.625*\log_{2}(0.625))]$  
$H(X) = -[(-0.531)+(-0.424)]$  
$H(X) = -[-0.95443]$  
$H(X) = 0.95443$  

perl ပရိုဂရမ်မှာတော့ input ကို text file ကနေ ယူထားပါတယ်။  
text ဖိုင်ထဲမှာတော့ "မမဝဝထထကအကပထမ" နဲ့ "entropy" ဆိုတဲ့ စာကြောင်းနှစ်ကြောင်းကို ရိုက်ထည့်ထားပါတယ်။  
(ဗမာစာကြောင်းမှာက space ထည့်ရိုက်ရင်လည်း တွက်ပေးမှာ ဖြစ်ပေမဲ့ p for  ဆိုပြီး ဖြစ်နေမှာမို့ တမင်တကာ ဖြုတ်ထားခဲ့တာပါ)  
```
(base) ye@ykt-pro:/media/ye/project1/4github/calc-entropy$ cat input.txt 
မမဝဝထထကအကပထမ
entropy
```

perl program ကို command line ကနေ run လိုက်ရင် အောက်ပါအတိုင်း Shannon entropy ကို input စာကြောင်း နှစ်ကြောင်းအတွက် တွက်ပေးသွားပါလိမ့်မယ်။  

```
(base) ye@ykt-pro:/media/ye/project1/4github/calc-entropy$ cat input.txt | perl ./calc-entropy.pl 
p for က: 0.166666666666667
p for ထ: 0.25
p for ပ: 0.0833333333333333
p for မ: 0.25
p for ဝ: 0.166666666666667
p for အ: 0.0833333333333333
Entropy: 2.45914791702724

p for e: 0.142857142857143
p for n: 0.142857142857143
p for o: 0.142857142857143
p for p: 0.142857142857143
p for r: 0.142857142857143
p for t: 0.142857142857143
p for y: 0.142857142857143
Entropy: 2.8073549220576
```

Enjoy learning entropy!  

y@CADT  
12 June 2022  
 
## Reference

1. https://en.wikipedia.org/wiki/Claude_Shannon
2. https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf

