def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a' ) + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A' ) + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a' ) - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A' ) - shift) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def main():
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")
    key = int(input("Enter the encryption key (shift value): "))
    action = input("Encrypt or Decrypt? (e/d): ")

    try:
        with open(input_file, 'r') as file:
            text = file.read()

        if action == 'e':
            encrypted_text = encrypt(text, key)
            with open(output_file, 'w') as file:
                file.write(encrypted_text)
            print("File encrypted successfully!")
        elif action == 'd':
            decrypted_text = decrypt(text, key)
            with open(output_file, 'w') as file:
                file.write(decrypted_text)
            print("File decrypted successfully!")
        else:
            print("Invalid action. Please choose 'e' for encryption or 'd' for decryption.")
    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    main()
