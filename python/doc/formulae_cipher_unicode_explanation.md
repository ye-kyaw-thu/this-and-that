# Brief Explanation

ရေးထားတဲ့ code မှာ သုံးထားတဲ့ encryption, decryption နည်းလမ်း တစ်ခုချင်းစီအတွက် သင်္ချာအပိုင်းက အောက်ပါအတိုင်းပါ။  
ဒီနေရာမှာ   

`n` = index of the character in the message    
`c` = character to be encrypted or decrypted  
`key` = the encryption key  

Encryption လုပ်တဲ့အခါမှာ `c` ကနေ `c'` ကို ပြောင်းပါတယ်။  ထိုနည်းလည်းကောင်း decryption လုပ်တဲ့အခါမှာ `c'` ကနေ `c` ပြန်ရအောင် ပြောင်းပါတယ်။  

1. **Method 1:**

    - Encryption: `c' = (c + key) mod 0x110000`
    - Decryption: `c = (c' - key) mod 0x110000`
    - This method simply adds the key to the Unicode code point of the character for encryption, and subtracts it for decryption.

2. **Method 2:**

    - Encryption: `c' = (c + key * n) mod 0x110000`
    - Decryption: `c = (c' - key * n) mod 0x110000`
    - This method is similar to Method 1, but it also includes a multiplication by the index of the character.

3. **Method 3:**

    - Encryption: `c' = (c XOR key) mod 0x110000`
    - Decryption: `c = (c' XOR key) mod 0x110000`
    - This method uses the bitwise XOR operation with the key. It is its own inverse, so the decryption formula is the same as the encryption formula.

4. **Method 4:**

    - Encryption: `c' = (c + key²) mod 0x110000`
    - Decryption: `c = (c' - key²) mod 0x110000`
    - This method is similar to Method 1, but the key is squared before it's added to/subtracted from the Unicode code point.

5. **Method 5:**

    - Encryption: `c' = (c XOR key²) mod 0x110000`
    - Decryption: `c = (c' XOR key²) mod 0x110000`
    - This is similar to Method 3, but with the key squared.

6. **Method 6:**

    - Encryption: `c' = (c + key³) mod 0x110000`
    - Decryption: `c = (c' - key³) mod 0x110000`
    - This is similar to Method 1, but the key is cubed.

7. **Method 7:**

    - Encryption: `c' = (c XOR key³) mod 0x110000`
    - Decryption: `c = (c' XOR key³) mod 0x110000`
    - This is similar to Method 3, but with the key cubed.

8. **Method 8:**

    - Encryption: `c' = (c + key * n³) mod 0x110000`
    - Decryption: `c = (c' - key * n³) mod 0x110000`
    - This is similar to Method 2, but the index is cubed.

9. **Method 9:**

    - Encryption: `c' = (c + key⁴) mod 0x110000`
    - Decryption: `c = (c' - key⁴) mod 0x110000`
    - This is similar to Method 1, but the key is raised to the power of 4.

10. **Method 10:**

    - Encryption: `c' = (c + key * n²) mod 0x110000`
    - Decryption: `c = (c' - key * n²) mod 0x110000`
    - This is similar to Method 2, but the index is squared.

**အခု စမ်းရေးထားတဲ့ code က တကယ့် application တွေအတွက် မသုံးသင့်ပါဘူး။**  
**တကယ့် simple encryption ဖြစ်ပြီးတော့ စမ်းကြည့်ထားတာ သက်သက်ပါ။**  

