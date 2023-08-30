import hashlib

def calcular_hash_sha256(mensaje):
    # Crear un objeto hashlib de tipo SHA-256
    sha256_hash = hashlib.sha256()

    # Convertir el mensaje a bytes antes de alimentarlo al objeto hash
    mensaje_bytes = mensaje.encode('utf-8')
    
    # Alimentar el mensaje en el objeto hash
    sha256_hash.update(mensaje_bytes)
    
    # Obtener el hash en formato hexadecimal
    hash_resultado = sha256_hash.hexdigest()
    
    return hash_resultado

mensaje = "Hola, esto es un mensaje de prueba."
hash_resultado = calcular_hash_sha256(mensaje)
print("Mensaje:", mensaje)
print("Hash SHA-256:", hash_resultado)
