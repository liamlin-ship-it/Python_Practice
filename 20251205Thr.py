msg = input()
offset = int(input())

encrypted_msg = ""

for char in msg:
    if char.isupper():
        new_ascii = (ord(char) - ord('A') + offset) % 26 + ord('A')
        encrypted_msg += chr(new_ascii)

    elif char.islower():
        new_ascii = (ord(char) - ord('a') + offset) % 26 + ord('a')
        encrypted_msg += chr(new_ascii)

    else:
        encrypted_msg += char

print(encrypted_msg)