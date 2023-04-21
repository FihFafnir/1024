import re

def do_cipher_of_caesar(text, key, just_letters):
    encrypted_text = ""
        
    for char in text:
        if re.match(r"[A-Za-z]", char) or not just_letters:
            num = ord(char)
            char = chr(num + key)
        encrypted_text += char
        
    return encrypted_text

number_of_lines = range(int(input()))
encrypted_texts = []

for i in number_of_lines:
    text = input()
    first_phrase_encrypted_text = do_cipher_of_caesar(text, 3, True)

    second_phrase_encrypted_text = first_phrase_encrypted_text[::-1]

    half_text_index = len(second_phrase_encrypted_text)//2
    first_half_text = second_phrase_encrypted_text[:half_text_index]
    second_half_text = second_phrase_encrypted_text[half_text_index:]

    second_half_text = do_cipher_of_caesar(second_half_text, -1, False)
    
    third_phrase_encrypted_text = first_half_text + second_half_text
    encrypted_texts.append(third_phrase_encrypted_text)
    
for encrypted_text in encrypted_texts:
    print(encrypted_text)
