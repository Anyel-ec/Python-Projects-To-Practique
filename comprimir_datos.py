import zlib
import base64

def comprimir_dato(dato):
    dato_comprimido = zlib.compress(dato.encode('utf-8'))
    return base64.b64encode(dato_comprimido).decode('utf-8')

def descomprimir_dato(dato_comprimido):
    dato_base64 = base64.b64decode(dato_comprimido.encode('utf-8'))
    dato_descomprimido = zlib.decompress(dato_base64).decode('utf-8')
    return dato_descomprimido

# Ejemplo de uso
dato_original = "Datos de ejemplo que queremos comprimir y luego descomprimir"

# Comprimir los datos
dato_comprimido = comprimir_dato(dato_original)
print("Dato comprimido:", dato_comprimido)

# Descomprimir los datos
dato_descomprimido = descomprimir_dato(dato_comprimido)
print("Dato descomprimido:", dato_descomprimido)
