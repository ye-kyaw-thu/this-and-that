# Mutual Information Scores Calculation

## --help

Help screen ခေါ်ကြည့်ရင် ...  

```
python information_theory3.py --help
usage: information_theory3.py [-h] -c CORPUS_FILENAME -n TOP_N_WORDS

Compute top N words with highest mutual information.

optional arguments:
  -h, --help            show this help message and exit
  -c CORPUS_FILENAME, --corpus_filename CORPUS_FILENAME
                        Path to the input CSV corpus file.
  -n TOP_N_WORDS, --top_N_words TOP_N_WORDS
                        Number of top words to be extracted based on MI.

```

## Small Corpus Info

Example run ပြဖို့အတွက် positive/negative sentiment dataset အသေးလေးတစ်ခုကို သုံးပါမယ်။  

```
text,sentiment
အရမ်း လှ နေ ပါလား,positive
ရုပ်ဆိုး ကြီး,negative
အပေါက် ဆိုး တယ်,negative
စောက် သုံး မကျ,negative
မင်္ဂလာ ပါ,positive
စား လို့ ကောင်း တယ်,positive
အိပ် လို့ ကောင်း တယ်,positive
လိမ္မာ တယ်,positive
မ လိမ္မာ ဘူး,negative
အလုပ် လုပ် တာ အရမ်း နှေး,negative
သွက်သွက်လက်လက် ရှိ တယ်,positive
အပြော ချို ပေမဲ့ ယုတ်မာ တယ်,negative
အပြော မချို ပေမဲ့ စိတ်ထား ကောင်း,positive
မိန်းမ အလိမ္မာ ပါ,positive
မိန်းမ က မိုက် တယ်,negative
သား လူမိုက်,negative
စိတ် တို တယ်,negative
စိတ် ရှည် တယ်,positive
ဝမ်းနည်း တယ်,negative
ဝမ်းသာ တယ်,positive
ဗိုက် နာ တယ်,negative
နေမကောင်း ဘူး,negative
နေကောင်း ပါ တယ်,positive
စိတ် မကောင်း ဘူး,negative
စာမေးပွဲ ကျ တယ်,negative
စာမေးပွဲ အောင် တယ်,positive
အမှတ် များ တယ်,positive
အမှတ် နည်း တယ်,negative
အရမ်း ညံ့ တယ်,negative
အရမ်း တော် တယ်,positive
အရမ်း ညံ့ဖျင်း တယ်,negative
ဆရာ့ စကား နားထောင် တယ်,positive
ဆရာ့ စကား နားမထောင် ဘူး,negative
ခိုင်း တာ လုပ် တယ်,positive
ခိုင်း တာ မလုပ် ဘူး,negative
သာကူး တွေ ပါ,negative
စာ ကြိုးစား တယ်,positive
စာ မကြိုးစား ဘူး,negative
သူ က ချစ်စရာ ကောင်း တယ်,positive
သူ က ချစ်စရာ မကောင်း ဘူး,negative
ဒီနေ့ ပျော် တယ်,positive
ဒီ တပတ် လုံး အရမ်း ပင်ပန်း တယ်,negative
ဒီနေ့ စိတ်ညစ် တယ်,positive
မနှစ် က ပျော် ခဲ့ တယ်,positive
စိတ်ထား ကောင်း မှ ဖြစ် မယ်,negative
ကျန်းမာရေး က မကောင်း ဘူး,negative
ကင်ဆာ ရောဂါ ဖြစ် နေ တယ်,negative
ရောဂါ မရှိ ဘူး လို့ ဆရာဝန် က ပြော ပါ တယ်,positive
ကြိုးစား တယ် ဒါပေမဲ့ အောင်မြင် သင့် သလောက် မအောင်မြင် တာ,negative
```

## Example Running  

-c option က corpus ဖိုင်နာမည်ပါ။ -n option ကတော့ top N words အတွက်ပါ။  
Run လို့ error မရှိရင်တော့ အောက်ပါအတိုင်း MI scores တွေထဲကနေ top 30 words ကို ဆွဲထုတ်ပေးပါလိမ့်မယ်။  

```
python information_theory3.py -c .\corpus\sentiment\sentiment_my_dataset.csv -n 30
C:\Users\ye\Anaconda3\lib\site-packages\sklearn\feature_extraction\text.py:528: UserWarning: The parameter 'token_pattern' will not be used since 'tokenizer' is not None'
  warnings.warn(
ဘူး: 0.0590
လို့: 0.0515
တယ်: 0.0455
မကောင်း: 0.0381
ပျော်: 0.0338
ဒီနေ့: 0.0338
ကောင်း: 0.0294
ပါ: 0.0294
ဖြစ်: 0.0250
မရှိ: 0.0166
ရှိ: 0.0166
တော်: 0.0166
များ: 0.0166
မင်္ဂလာ: 0.0166
နားထောင်: 0.0166
မနှစ်: 0.0166
မချို: 0.0166
နေကောင်း: 0.0166
အောင်: 0.0166
ပြော: 0.0166
လိမ္မာတယ်: 0.0166
ရှည်: 0.0166
စား: 0.0166
ဆရာဝန်: 0.0166
အိပ်: 0.0166
အလိမ္မာ: 0.0166
သွက်သွက်လက်လက်: 0.0166
ခဲ့: 0.0166
စိတ်ညစ်: 0.0166
ပါလား: 0.0166
```

## Brief Explanation

1. **Higher MI Scores**: Higher MI score ရတဲ့ ဗမာစာလုံးတွေက အချက်အလက်အနေနဲ့ တန်ဖိုး ရှိတယ် (i.e. more informative) သို့မဟုတ် classification လို အလုပ်မျိုးအတွက် ဆိုရင်လည်း class ခွဲခြားဖို့အတွက် အချက်အလက်အဖြစ် အသုံးဝင်နိုင်တယ်။  

2. **Lower MI Scores**: တကယ်လို့ MI score က နည်းနေပြီ ဆိုရင်တော့ အဲဒီ ဗမာစာလုံးတွေကို less informative ဖြစ်တယ်လို့ အကြမ်းဖျဉ်းအားဖြင့် ယူဆနိုင်တယ်။ တကယ်လို့ MI score က သုည ဆိုတဲ့ တန်ဖိုး ရတယ် ဆိုရင် ဒီလို စာလုံးမျိုးက လက်ရှိ သုံးထားတဲ့ ဥပမာ dataset အတွက် ဆိုရင်တော့ positive မှာရော negative ဘက်မှာရော နှစ်ဘက်စလုံးမှာ ရှိနေနိုင်တယ်လို့ ဖော်ပြနေတာပါ။  

3. **Interpreting the Range**: MI score တွေကို ဘယ်လိုဖတ်ရမလဲ၊ ဘယ်လို နားလည်ရမလဲ ဆိုရင် ရလာတဲ့ score တွေကို တစ်ခုနဲ့ တစ်ခု နှိုင်းယှဉ်ကြည့်ပြီးပဲ ဘယ်တန်ဖိုးက များတယ်၊ ဘယ်တန်ဖိုးက နည်းတယ် ဆိုပြီး ပြောလို့ ရပါလိမ့်မယ်။ ဆိုလိုတာက တန်ဖိုးတွေက သုညကနေ စပြီးတော့ ဘယ်တန်ဖိုးမှာ ဆုံးမလဲ ဆိုတာက ကိုယ် input လုပ်လိုက်တဲ့ dataset ပေါ်မှာ မူတည်ပါလိမ့်မယ်။ 0 to positive values ဆိုတဲ့ ပုံစံနဲ့ ပြသပေးမှာပါ။ အဲဒီ positive value က ဘယ်မှာ ဆုံးမလဲ ဆိုတာက က အတအကျ မရှိပါဘူး။ လက်တွေ့ တွက်ကြည့်ရင်က အရမ်း များတဲ့ တန်ဖိုးတွေကို ရလေ့ မရှိပါဘူး။   

လက်ရှိ ငါတို့ သုံးခဲ့တဲ့ dataset အတွက် ဆိုရင်တော့ "ဘူး" ဆိုတဲ့ စာလုံးအတွက် ရလာတဲ့ MI score 0.0590 က အမြင့်ဆုံး တန်ဖိုးပါပဲ။ ဆိုလိုတာက ဒီ စာလုံးက ဆွဲထုတ်လိုက်တဲ့ စာလုံး စုစုပေါင်း အလုံး သုံးဆယ်ထဲမှာမှ informative အဖြစ်ဆုံး စာလုံးဆိုတဲ့ အဓိပ္ပါယ်ပါ။ ဒီစာလုံးက positive/negative ဆိုတဲ့ polarity class ကို ခွဲခြားဖို့အတွက် အထောက်အကူဖြစ်နိုင်တယ် ဆိုတဲ့ အဓိပ္ပါယ်ပါ။ တကယ်လည်း ဟုတ်ပါတယ်။ လက်ရှိ သုံးခဲ့တဲ့ example dataset ထဲက "ဘူး" ပါနေတဲ့ စာကြောင်း သုံးကြောင်းကို ဆွဲထုတ်ကြည့်ရင် ပိုပြီး မြင်သာနိုင်ပါလိမ့်မယ်။ အောက်ပါအတိုင်းပါ။  

- ဆရာ့ စကား နားမထောင် ဘူး,negative
- စာ မကြိုးစား ဘူး,negative
- သူ က ချစ်စရာ မကောင်း ဘူး,negative

တခြားရှုထောင့်ကနေ ကြည့်ကြည့်မယ် ဆိုရင်လည်း MI score တန်ဖိုး 0.0166 ရှိတဲ့ စာလုံးတွေကိုလည်း တော်တော်များများ တွေ့ရမှာ ဖြစ်ပါတယ်။ လက်ရှိ ဒေတာအတွက် သေချာပေါက် ပြောနိုင်တာကတော့ အဲဒီ စာလုံးတွေက MI score တန်ဖိုး 0.0590 သို့မဟုတ် 0.0515 ရရှိထားတဲ့စာလုံးတွေထက်စာရင်တော့ less informative ဖြစ်တယ်ဆိုတာပါပဲ။  

တကယ့် dataset အကြီးကြီးနဲ့ MI score တွေကို တွက်ကြည့်ရင် စိတ်ဝင်စားဖို့ ကောင်းပါတယ်။ Feature selection အတွက် အသုံးဝင်ပါတယ်။  



