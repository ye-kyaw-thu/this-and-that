# Demo of Appling Turing Machine for Searching Padsints



## How to run

An Example of input file that contained Burmese subscripts.  

```
(base) ye@lst-gpu-3090:~/exp/4teaching/turing_machine$ cat input.txt
ကျွန်တော်က တက္ကသိုလ် ကျောင်းသားပါ။
သစ္စာရှိမှ သစ္စာပန်း ပွင့်လိမ့်မယ်
ဒုက္ခသစ္စာ
(base) ye@lst-gpu-3090:~/exp/4teaching/turing_machine$
```

run လိုက်ရင် ရလာမယ့် output က အောက်ပါအတိုင်းပါ ...  

```
(base) ye@lst-gpu-3090:~/exp/4teaching/turing_machine$ python ./padsint_turing.py ./input.txt
က္က
စ္စ, စ္စ
က္ခ, စ္စ
(base) ye@lst-gpu-3090:~/exp/4teaching/turing_machine$
```
