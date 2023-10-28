# Week 6
def substitution_cipher(text, shift):
    encrypted_text = ""
    for c in text:
        if c.isalpha():
            offset = ord('A') if c.isupper() else ord('a')
            new_letter = chr(((ord(c) - offset + shift) % 26) + offset)
            encrypted_text += new_letter
        else:
            encrypted_text += c
    return encrypted_text

text = "Hello, World!"
shift = 3  # Define the shift value
encrypted_text = substitution_cipher(text, shift)

print("Original Text:", text)
print("Encrypted Text:", encrypted_text)
