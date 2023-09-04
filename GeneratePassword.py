import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    longitud = int(input("Ingresa la longitud de la contraseña: "))
    contraseña_generada = generar_contraseña(longitud)
    print("Contraseña generada:", contraseña_generada)
