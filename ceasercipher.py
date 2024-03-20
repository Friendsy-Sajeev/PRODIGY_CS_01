def encrypt(message, shift):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

    if choice == 'e':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = encrypt(message, shift)
        print("Encrypted text:", encrypted_text)

    elif choice == 'd':
        encrypted_text = input("Enter the encrypted text to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = decrypt(encrypted_text, shift)
        print("Decrypted text:", decrypted_text)

    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
