
def do_cipher_of_caesar(text, key, just_letters):
    encrypted_text = ""
        
    for char in text:
        num = ord(char)
        if (num >= 65 and num <= 90) or (num >= 97 and num <= 122) or not just_letters:
            num = ord(char)
            char = chr(num + key)
        encrypted_text += char
        
    return encrypted_text

number_of_lines = range(int(input()))

for i in number_of_lines:
    text = input()
    encrypted_text = do_cipher_of_caesar(text, 3, True)

    encrypted_text = encrypted_text[::-1]

    half_text_index = len(encrypted_text)//2
    first_half_text = encrypted_text[:half_text_index]
    second_half_text = encrypted_text[half_text_index:]

    second_half_text = do_cipher_of_caesar(second_half_text, -1, False)
    
    encrypted_text = first_half_text + second_half_text

    print(encrypted_text)
