text = input("Enter the text to decrypt: ")
shift = int(input("Enter the shift value if known(leave blank for brute force): ") or 0)

def decrypt_known(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def decrypt_brute_force(text):
    for shift in range(1, 26):
        decrypt_text = ""
        for char in text:
            if char.isalpha():
                shift_amount = shift % 26
                if char.islower():
                    decrypted_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
                else:
                    decrypted_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
                decrypt_text += decrypted_char
            else:
                decrypt_text += char
        print(f"Shift {shift}: {decrypt_text}")
        print("If this looks correct, type 'y' to stop or press Enter to continue.")
        if input().lower() == 'y':
            break

if shift:
    decrypted = decrypt_known(text, shift)
    print("Decrypted text:", decrypted)
else:
    decrypt_brute_force(text)