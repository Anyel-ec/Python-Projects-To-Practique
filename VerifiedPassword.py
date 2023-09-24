import re

def verificar_contraseña(password):
    # Verificar que la contraseña tenga al menos 8 caracteres
    if len(password) < 8:
        return "La contraseña debe tener al menos 8 caracteres."

    # Verificar que la contraseña contenga al menos una letra mayúscula
    if not any(c.isupper() for c in password):
        return "La contraseña debe contener al menos una letra mayúscula."

    # Verificar que la contraseña contenga al menos una letra minúscula
    if not any(c.islower() for c in password):
        return "La contraseña debe contener al menos una letra minúscula."

    # Verificar que la contraseña contenga al menos un número
    if not any(c.isdigit() for c in password):
        return "La contraseña debe contener al menos un número."

    # Verificar que la contraseña contenga al menos un carácter especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "La contraseña debe contener al menos un carácter especial."

    # La contraseña parece segura
    return "La contraseña es segura."

if __name__ == "__main__":
    contraseña = input("Ingrese una contraseña: ")
    resultado = verificar_contraseña(contraseña)
    print(resultado)
