def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, key):
    return encrypt(encrypted_message, -key)

def main():
    choice = input("¿Quieres encriptar (E) o desencriptar (D) un mensaje? ").upper()
    if choice == "E":
        message = input("Ingrese el mensaje a encriptar: ")
        key = int(input("Ingrese el valor de la clave: "))
        encrypted_message = encrypt(message, key)
        print("Mensaje encriptado:", encrypted_message)
    elif choice == "D":
        encrypted_message = input("Ingrese el mensaje a desencriptar: ")
        key = int(input("Ingrese el valor de la clave: "))
        decrypted_message = decrypt(encrypted_message, key)
        print("Mensaje desencriptado:", decrypted_message)
    else:
        print("Opción no válida. Por favor, elige 'E' o 'D'.")

if __name__ == "__main__":
    main()
