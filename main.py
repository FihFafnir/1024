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
encrypted_lines = []

for i in number_of_lines:
    line = input()
    first_phrase_encrypted_line = do_cipher_of_caesar(line, 3, True)

    second_phrase_encrypted_line = first_phrase_encrypted_line[::-1]

    half_line_index = len(second_phrase_encrypted_line)//2
    first_half_line = second_phrase_encrypted_line[:half_line_index]
    second_half_line = second_phrase_encrypted_line[half_line_index:]

    second_half_line = do_cipher_of_caesar(second_half_line, -1, False)
    
    third_phrase_encrypted_line = first_half_line + second_half_line
    encrypted_lines.append(third_phrase_encrypted_line)
    
for encrypted_line in encrypted_lines:
    print(encrypted_line)
