# Demo of Appling Turing Machine for Searching Padsints

PadsintTuringMachine လို့နာမည်ပေးထားတဲ့ python class ထဲက အရေးကြီးတဲ့ အပိုင်းနှစ်ပိုင်းကို နားလည်ရင် ရပါပြီ။  
ပထမ အပိုင်းက initialization လုပ်တဲ့ အပိုင်းပါ။  

```python
    def __init__(self, input_file):
        self.state = 'START'
        self.buffer = []
        self.subscripts = [] # List to collect found subscript consonants
        self.input_file = input_file
```
Python code ကို ဖတ်တတ်တဲ့ သူဆိုရင် နားလည်ပြီးသားလို့ ယူဆပေမဲ့...  
Initialize လုပ်သွားတာတွေကို Pseudo code အနေနဲ့ ရေးပြရရင်တော့ အောက်ပါအတိုင်းပါ။  

    - Set `state` to 'START'
    - Initialize `buffer` as an empty list
    - Initialize `subscripts` as an empty list for collecting found subscript consonants
    - Store `input_file`

ဒုတိယ process_char လို့ နာမည်ပေးထားတဲ့ function ပါ။  

```python
    def process_char(self, char):
        # START state: Normal reading until we find a subscript marker
        if self.state == 'START':
            if char == '္':
                self.state = 'FOUND_SUBSCRIPT'
            else:
                self.buffer.append(char)
        # FOUND_SUBSCRIPT state: When we detect a subscript marker, we process the next char
        elif self.state == 'FOUND_SUBSCRIPT':
            if char != '\n' and len(self.buffer) > 0:
                stacked_syllable = f"{self.buffer[-1]}္{char}"
                self.subscripts.append(stacked_syllable)
            self.state = 'START'
```

Pseudo code လိုမျိုး ရေးပြရရင်တော့ အောက်ပါအတိုင်းဖြစ်ပါလိမ့်မယ်။  

    - **If** `state` is 'START':
        - **If** `char` is '္':
            - Set `state` to 'FOUND_SUBSCRIPT'
        - **Else**:
            - Append `char` to `buffer`
    - **ElseIf** `state` is 'FOUND_SUBSCRIPT':
        - **If** `char` is not a newline and `buffer` is not empty:
            - Construct `stacked_syllable` as the last character of `buffer` followed by '္' and `char`
            - Append `stacked_syllable` to `subscripts`
        - Set `state` to 'START'
        
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
