import nfc

def leer_nfc():
    clf = nfc.ContactlessFrontend('usb')
    print("Acerca la etiqueta NFC al lector...")
    try:
        while True:
            tag = clf.connect(rdwr={'on-connect': lambda tag: False})
            if tag:
                print("ID de la etiqueta NFC:", tag.identifier.hex())
                break
    finally:
        clf.close()

def escribir_nfc(data):
    clf = nfc.ContactlessFrontend('usb')
    print("Acerca la etiqueta NFC al lector para escribir...")
    try:
        while True:
            tag = clf.connect(rdwr={'on-connect': lambda tag: False})
            if tag:
                tag.write(data)
                print("Datos escritos en la etiqueta NFC.")
                break
    finally:
        clf.close()

# Ejemplo de uso
if __name__ == "__main__":
    opcion = input("¿Qué deseas hacer? (leer/escribir): ").lower()
    if opcion == "leer":
        leer_nfc()
    elif opcion == "escribir":
        data = input("Introduce los datos que deseas escribir en la etiqueta NFC: ")
        escribir_nfc(data.encode())
    else:
        print("Opción no válida.")
