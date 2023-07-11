# Time Zone Converter

Time Zone တွေနဲ့ ပတ်သက်ပြီး ပထမဆုံး သင်ကြားပေးခဲ့တဲ့သူကတော့ ငါ့ အဖေ ပါ။ ပါပါက ကိုယ်တိုင်လည်း သင်္ဘောသား ဆိုတော့ နိုင်ငံပေါင်းစုံ သွားရင်း နာရီညှိရတဲ့ ကိစ္စတွေကို ပြောပြဖူးတယ်။ အဲဒါကြောင့် ငါ့အတွက်က အလယ်တန်း ကျောင်းသား ဘဝမှာကတည်းက ဒီ time zone တွေနဲ့ ပတ်သက်ပြီး အခြေခံ ဗဟုသုတာက ရှိနေခဲ့ပါတယ်။  

သို့သော်လည်း တကယ်တန်း time zone တွေကို သတ်မှတ်ပုံ၊ တွက်ချက်ပုံတွေက ဂျပန်ရောက်တဲ့အခါမှပဲ ပိုနားလည်ခဲ့ပါတယ်။ ခန့်မှန်းခြေအားဖြင့် time zone သတ်မှတ်ချက်တွေက ၃၈ ခုလောက်ထိ ရှိပါတယ်။ တကယ်တမ်း လက်ရှိမှာ ကမ္ဘာတဝှမ်း တွင်တွင်ကျယ်ကျယ် သုံးနေကြတဲ့ system နှစ်ခုကတော့ Greenwich Mean Time (GMT) နဲ့ Coordinated Universal Time (UTC) ဆိုတဲ့ နှစ်မျိုးပါ။ GMT ကတော့ လောင်ဂျီတွဒ် လိုင်းတွေအပေါ်ကို အခြေခံပြီး တွက်တာ ဖြစ်ပြီးတော့၊ UTC ကတော့ ကမ္ဘာကြီးရဲ့ လှည့်ပတ်တဲ့နှုန်း အပေါ်ကို ညှိပြီး တွက်တဲ့ စနစ်ဖြစ်ပါတယ်။  

## How to run

အရင်ဆုံး --help option နဲ့ help screen ကို ခေါ်ကြည့်ရအောင် ...  

```
python tz_converter.py --help
usage: tz_converter.py [-h] [-l] [Time]

Convert time between timezones.

positional arguments:
  Time        the time to be converted in the format "HH:MM AM/PM TZ" or "HH:MM, AM/PM, TZ"

optional arguments:
  -h, --help  show this help message and exit
  -l, --list  List countries associated with each timezone
```

ကိုယ့်က EST အချိန်ကို သတ်မှတ်ထားတဲ့ format အတိုင်း ရိုက်ထည့်လိုက်ရင် သူနဲ့ ညီတဲ့ တခြား time zone တွေရဲ့ အချိန်တွေကို ဖော်ပြပေးပါလိမ့်မယ်။  

```
python tz_converter.py "10:57 PM EST"
08:00 PM PST
03:53 AM UTC
09:46 AM IST
03:53 AM GMT
```

am, pm တို့ကို အကြီးနဲ့ ရိက်ရိုက်၊ အသေးနဲ့ ရိုက်ရိုက် လက်ခံပါတယ်။ ထိုနည်းလည်းကောင်း gmp, GMT, pst, PST, est, EST, utc, UTC, ist, IST တို့ကိုလည်း အကြီးနဲ့ပဲ ရိုက်ရိုက်၊ အသေးနဲ့ပဲ ရိုက်ရိုက်၊ အကြီးအသေး ရောပြီးပဲ ရိုက်ရိုက် ပရိုဂရမ်က လက်ခံပြီး အလုပ်လုပ်ပါတယ်။  

```
python tz_converter.py "03:53 am GMT"
08:00 PM PST
10:57 PM EST
03:53 AM UTC
09:46 AM IST
```

ဒီတခါတော့ Pacific Standard Time ကို ပြောင်းခိုင်းကြည့်ရအောင် ...  

```
python tz_converter.py "8:00 pm pst"
10:57 PM EST
03:53 AM UTC
09:46 AM IST
03:53 AM GMT
```

ဒီတခါတော့ Coordinated Universal Time သို့မဟုတ် Universal Time Coordinated (UTC) အချိန်ကို ရိုက်ထည့်ပြီး ပြောင်းခိုင်းကြည့်ရအောင် ...  

```
python tz_converter.py "8:00, AM, UTC"
12:07 AM PST
03:04 AM EST
01:53 PM IST
08:00 AM GMT
```

-l or --list option နဲ့ အဓိက ဆက်စပ်နေတဲ့ နိုင်ငံတချို့ကို ရိုက်ထုတ်ကြည့်ရအောင်။  

```
python tz_converter.py -l
PST: United States, Canada, Mexico
EST: United States, Canada, Mexico, Panama, Ecuador, Peru, Colombia
UTC: Ghana, Iceland, Côte d'Ivoire, Burkina Faso, Gambia, Senegal, Mali, Guinea, Guinea-Bissau, Sierra Leone, Liberia
IST: India
GMT: United Kingdom, Ireland, Portugal, Iceland, Ghana, Côte d'Ivoire, Burkina Faso, Gambia, Senegal, Mali, Guinea, Guinea-Bissau, Sierra Leone, Liberia
```

