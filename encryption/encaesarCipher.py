from pyscript import document

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_action(event):
    text = document.querySelector("#input-enc-caesar").value
    shift_val = document.querySelector("#shift-enc-caesar").value
    
    shift = int(shift_val) if shift_val else 0
        
    encrypted = encrypt(text, shift)
    
    document.querySelector("#output-enc-caesar").innerText = encrypted