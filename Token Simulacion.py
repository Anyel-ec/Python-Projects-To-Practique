import secrets
import time

# Función para generar un token aleatorio con tiempo de expiración de 30 segundos
def generar_token_con_expiracion():
    token = secrets.token_hex(16)  # Genera un token hexadecimal de 16 bytes (32 caracteres)
    tiempo_expiracion = int(time.time()) + 30  # Tiempo actual + 30 segundos
    return token, tiempo_expiracion

# Simulación de inicio de sesión
def iniciar_sesion():
    usuario = input("Ingresa tu nombre de usuario: ")
    contrasena = input("Ingresa tu contraseña: ")

    # Verificar las credenciales (simulación básica)
    if usuario == "anyel" and contrasena == "anyel":
        print("¡Inicio de sesión exitoso!")

        while True:
            token_esperado, tiempo_expiracion = generar_token_con_expiracion()
            print(f"Tu token de sesión es válido por 30 segundos: {token_esperado}")

            for i in range(5, 0, -1):
                print(f"Ingresa el token en {i} segundos: ", end="")
                time.sleep(1)
                print("\r", end="")  # Borra la línea actual en la consola

            # Simulación de uso del token en la sesión
            token_ingresado = input("\nIngresa tu token de sesión para continuar: ")
            tiempo_actual = int(time.time())

            if tiempo_actual <= tiempo_expiracion and token_ingresado == token_esperado:
                print("Token válido. ¡Sesión iniciada correctamente!")
                break
            else:
                print("Token inválido o expirado. Intenta de nuevo.")
    else:
        print("Credenciales incorrectas. Inicio de sesión fallido.")

if __name__ == "__main__":
    iniciar_sesion()
