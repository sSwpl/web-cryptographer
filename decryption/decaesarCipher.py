from pyscript import document

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

def decrypt_action(event):
    text = document.querySelector("#input-dec-caesar").value
    shift_val = document.querySelector("#shift-dec-caesar").value
    output_element = document.querySelector("#output-dec-caesar")
    
    if shift_val:
        shift = int(shift_val)
        decrypted = decrypt_known(text, shift)
        output_element.innerText = f"Odszyfrowano (przesunięcie {shift}):\n{decrypted}"
    else:
        result_text = "=== WYNIKI BRUTE FORCE ===\n"
        for shift in range(1, 26):
            decrypted = decrypt_known(text, shift)
            result_text += f"Przesunięcie {shift}: {decrypted}\n"
            
        output_element.innerText = result_text