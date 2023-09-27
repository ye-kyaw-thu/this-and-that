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

```pseudo
BEGIN

    SET state TO 'START'
    INITIALIZE buffer AS EMPTY LIST
    INITIALIZE subscripts AS EMPTY LIST
    STORE input_file

END
```

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

```pseudo
IF state IS 'START' THEN
    IF char IS '္' THEN
        SET state TO 'FOUND_SUBSCRIPT'
    ELSE
        APPEND char TO buffer
    END IF
ELSE IF state IS 'FOUND_SUBSCRIPT' THEN
    IF char IS NOT NEWLINE AND buffer IS NOT EMPTY THEN
        CONSTRUCT stacked_syllable FROM LAST CHARACTER OF buffer + '္' + char
        APPEND stacked_syllable TO subscripts
    END IF
    SET state TO 'START'
END IF
```
        
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
