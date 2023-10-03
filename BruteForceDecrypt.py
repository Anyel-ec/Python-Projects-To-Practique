# Encrypted message
encrypted_message = "Xlmw irgvctxih jmrhxl, csy xlmw mw qiwweki mr xli viwmhirx. Liv svok?"

# Function for brute force decryption
def brute_force_decrypt(ciphertext):
    for key in range(1, 26):
        decrypted_message = ""
        for char in ciphertext:
            if char.isalpha():
                # Perform reverse shift
                new_char = chr(((ord(char) - key - 65) % 26) + 65) if char.isupper() else chr(((ord(char) - key - 97) % 26) + 97)
                decrypted_message += new_char
            else:
                decrypted_message += char
        print(f"Key {key}: {decrypted_message}")

# Decrypt the message using brute force
brute_force_decrypt(encrypted_message)
