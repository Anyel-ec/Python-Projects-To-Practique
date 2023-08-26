# importar la biblioteca hashlib
import hashlib

# función para verificar la fortaleza de la contraseña
def verificar_contrasena(contrasena):
    # convertir la contraseña a una cadena de bytes
    contrasena_bytes = contrasena.encode('utf-8')

    # calcular el hash de la contraseña utilizando la función SHA-256
    hash_contrasena = hashlib.sha256(contrasena_bytes)

    # convertir el hash a una cadena hexadecimal
    hash_contrasena_hex = hash_contrasena.hexdigest()

    # verificar la longitud de la contraseña
    if len(contrasena) < 8:
        print("La contraseña es demasiado corta.")
        return False

    # verificar si la contraseña contiene números
    if not any(char.isdigit() for char in contrasena):
        print("La contraseña debe contener al menos un número.")
        return False

    # verificar si la contraseña contiene letras mayúsculas
    if not any(char.isupper() for char in contrasena):
        print("La contraseña debe contener al menos una letra mayúscula.")
        return False

    # verificar si la contraseña contiene letras minúsculas
    if not any(char.islower() for char in contrasena):
        print("La contraseña debe contener al menos una letra minúscula.")
        return False

    # verificar si la contraseña contiene caracteres especiales
    caracteres_especiales = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    if not any(char in caracteres_especiales for char in contrasena):
        print("La contraseña debe contener al menos un caracter especial.")
        return False

        # verificar si la contraseña es segura (no se encuentra en una lista de contraseñas comunes)
    contrasenas_comunes = ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "qwerty", "abc123", "111111", "123123", "admin", "letmein", "welcome", "monkey", "password1", "123qwe", "shadow", "sunshine", "master", "football", "baseball", "chelsea", "qwertyuiop", "ashley", "superman", "696969", "dragon", "654321", "mustang", "trustno1", "michael", "jesus", "password2", "jordan", "liverpool", "buster", "loveme", "babygirl", "jennifer", "computer", "iloveyou", "princess", "hello", "freedom", "whatever", "solo", "maggie", "harley", "hannah", "password3", "cowboy", "samsung", "cookie", "summer", "killer", "charlie", "password4", "sweety", "snoopy", "jessica", "pepper", "daniel", "starwars", "1q2w3e4r", "ferrari", "george", "blablabla", "a1b2c3", "222222", "tigger", "rabbit", "7777777", "abcd1234", "123abc", "pokemon", "jason", "zxcvbnm", "security"]
    if contrasena in contrasenas_comunes:
        print("Esta contraseña es muy común y no es segura.")
        return False

    # si la contraseña pasa todas las verificaciones, se considera segura
    print("La contraseña es segura.")
    return True



contrasena = input("Introduzca su contraseña: ")
verificar_contrasena(contrasena)
