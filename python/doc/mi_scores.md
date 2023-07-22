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

##

