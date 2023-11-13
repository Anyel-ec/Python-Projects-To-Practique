import secrets

def generar_contrasena_con_token(longitud=12, token='MiTokenSecreto'):
    # Genera una cadena aleatoria de longitud especificada
    cadena_aleatoria = secrets.token_hex(longitud // 2)

    # Combina la cadena aleatoria con el token
    contrasena_con_token = f'{cadena_aleatoria}{token}'

    return contrasena_con_token

# Ejemplo de uso con una longitud de 16 caracteres y un token personalizado
contrasena_generada = generar_contrasena_con_token(longitud=16, token='MiTokenSecreto')
print(f'Contraseña generada: {contrasena_generada}')
