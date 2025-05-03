import string 
alphabet = list(string.ascii_lowercase)
direction = input("type encode to encrypt or decode to decrypt ")
text = input("type your message ")
shift = int(input("type the shift number "))

def encrypt(original_text : str, shift : int) -> str:
    encrypted_text = ""
    for char in original_text:
        if char in alphabet:
            index = alphabet.index(char)
            shifted_index = (index + shift) % 26
            encrypted_text += alphabet[shifted_index]
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt(encrypted_text : str, shift : int) -> str:
    original_text = ""
    for char in encrypted_text:
        if char in alphabet:
            index = alphabet.index(char)
            shifted_index = (index - shift) % 26
            original_text += alphabet[shifted_index]
        else:
            original_text += char
    
    return original_text

if direction == "encode":
    encrypted_text = encrypt(text, shift)
    print("encrypted text:" + encrypted_text)
else:
    original_text = decrypt(text, shift)
    print("original text: " +original_text)
