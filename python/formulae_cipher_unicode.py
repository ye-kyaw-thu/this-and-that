## Testing by Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand
## ဒီ code ကို encryption/decription အတွက် တိုက်ရိုက်ယူ မသုံးသင့်ပါဘူး။ 
## လွယ်တဲ့ math formula တချို့နဲ့ ဗမာစာ အပါအဝင် Unicode text တွေကို encryption/decryption စမ်းလုပ်ကြည့်ထားတာပါ။  

# Encryption method 1: Add key to the Unicode code point of each character.
def encrypt1(message, key):
    return ''.join(chr((ord(c) + key) % 0x110000) for c in message)

# Decryption method 1: Subtract key from the Unicode code point of each character.
def decrypt1(message, key):
    return ''.join(chr((ord(c) - key) % 0x110000) for c in message)

# Encryption method 2: Add key multiplied by the index to the Unicode code point of each character.
def encrypt2(message, key):
    return ''.join(chr((ord(c) + key*i) % 0x110000) for i, c in enumerate(message))

# Decryption method 2: Subtract key multiplied by the index from the Unicode code point of each character.
def decrypt2(message, key):
    return ''.join(chr((ord(c) - key*i) % 0x110000) for i, c in enumerate(message))

# Encryption method 3: XOR the Unicode code point of each character with the key.
def encrypt3(message, key):
    return ''.join(chr((ord(c) ^ key) % 0x110000) for c in message)

# Decryption method 3: XOR the Unicode code point of each character with the key.
def decrypt3(message, key):
    return ''.join(chr((ord(c) ^ key) % 0x110000) for c in message)

# Encryption method 4: Add key squared to the Unicode code point of each character.
def encrypt4(message, key):
    return ''.join(chr((ord(c) + key**2) % 0x110000) for c in message)

# Decryption method 4: Subtract key squared from the Unicode code point of each character.
def decrypt4(message, key):
    return ''.join(chr((ord(c) - key**2) % 0x110000) for c in message)

# Encryption method 5: XOR the Unicode code point of each character with the key squared.
def encrypt5(message, key):
    return ''.join(chr((ord(c) ^ (key**2)) % 0x110000) for c in message)

# Decryption method 5: XOR the Unicode code point of each character with the key squared.
def decrypt5(message, key):
    return ''.join(chr((ord(c) ^ (key**2)) % 0x110000) for c in message)

# Encryption method 6: Add key cubed to the Unicode code point of each character.
def encrypt6(message, key):
    return ''.join(chr((ord(c) + (key**3)) % 0x110000) for c in message)

# Decryption method 6: Subtract key cubed from the Unicode code point of each character.
def decrypt6(message, key):
    return ''.join(chr((ord(c) - (key**3)) % 0x110000) for c in message)

# Encryption method 7: XOR the Unicode code point of each character with the key cubed
def encrypt7(message, key):
    return ''.join(chr((ord(c) ^ (key**3)) % 0x110000) for c in message)

# Decryption method 7: XOR the Unicode code point of each character with the key cubed.
def decrypt7(message, key):
    return ''.join(chr((ord(c) ^ (key**3)) % 0x110000) for c in message)

# Encryption method 8: Add the Unicode code point of each character with the key multiplied by the cube of the index.
def encrypt8(message, key):
    return ''.join(chr((ord(c) + key*(i**3)) % 0x110000) for i, c in enumerate(message))

# Decryption method 8: Subtract the Unicode code point of each character with the key multiplied by the cube of the index.
def decrypt8(message, key):
    return ''.join(chr((ord(c) - key*(i**3)) % 0x110000) for i, c in enumerate(message))

# Encryption method 9: Add the Unicode code point of each character with the key to the power of 4.
def encrypt9(message, key):
    return ''.join(chr((ord(c) + key**4) % 0x110000) for c in message)

# Decryption method 9: Subtract the Unicode code point of each character with the key to the power of 4.
def decrypt9(message, key):
    return ''.join(chr((ord(c) - key**4) % 0x110000) for c in message)

# Encryption method 10: Add key multiplied by the square of the index to the Unicode code point of each character.
def encrypt10(message, key):
    return ''.join(chr((ord(c) + key*(i**2)) % 0x110000) for i, c in enumerate(message))

# Decryption method 10: Subtract key multiplied by the square of the index from the Unicode code point of each character.
def decrypt10(message, key):
    return ''.join(chr((ord(c) - key*(i**2)) % 0x110000) for i, c in enumerate(message))

operations = [(encrypt1, decrypt1), (encrypt2, decrypt2), (encrypt3, decrypt3),
              (encrypt4, decrypt4), (encrypt5, decrypt5), (encrypt6, decrypt6), 
              (encrypt7, decrypt7), (encrypt8, decrypt8), (encrypt9, decrypt9),
              (encrypt10, decrypt10)]

def convert_to_operation_key(key):
    return key % len(operations), key % 0x110000

def shift_characters(message, shift):
    shifted_message = ""
    for c in message:
        shifted_ord = (ord(c) + shift) % 0x110000
        shifted_message += chr(shifted_ord)
    return shifted_message

def encrypt(message, key):
    operation_key, key = convert_to_operation_key(key)
    shifted_message = shift_characters(message, 1000)
    return operations[operation_key][0](shifted_message, key)

def decrypt(message, key):
    operation_key, key = convert_to_operation_key(key)
    decrypted_message = operations[operation_key][1](message, key)
    return shift_characters(decrypted_message, -1000)

# Main function
def main():
    message = "နေကောင်းလား။"
    #message = "Hi! ရဲကျော်သူ"
    #message = "自然言語処理"
    #message = "123 自然 language processing for ဗမာစာ"
    key = 12345
    
    # Run all encryption methods
    for i in range(10):
        print(f"\nEncryption Method {i+1}:")
        encrypted_message = encrypt(message, key)
        decrypted_message = decrypt(encrypted_message, key)
        
        print(f"Original message: {message}")
        print(f"Encrypted message: {encrypted_message}")
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
