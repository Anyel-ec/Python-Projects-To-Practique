import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "computadora", "tecnologia", "inteligencia", "robotica"]
    return random.choice(palabras)
def mostrar_ahorcado(intentos):
    graficos_ahorcado = [
        """
           +---+
           |   |
               |
               |
               |
               |
        ============
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        ============
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        ============
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        ============
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        ============
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        ============
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        ============
        """
    ]
    return graficos_ahorcado[intentos]
def jugar_ahorcado():
    palabra = seleccionar_palabra()
    palabra = palabra.lower() #M m
    palabra_adivinada = ['_' if letra.isalpha() else letra for letra in palabra]
    intentos = 6
    letras_adivinadas = [] # A A
    palabra_adivinada[0] = palabra[0] # a__-__
    palabra_adivinada[-1] = palabra[-1] #_______d
    print(f"La palabra es: {' '.join(palabra_adivinada)}")

    while intentos > 0 and "_" in palabra_adivinada:
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            for idx, l in enumerate(palabra):
                if l == letra:
                    palabra_adivinada[idx] = letra
                    # A
        else:
            intentos -= 1
            print(f"La letra '{letra}' no está en la palabra. Te quedan {intentos} intentos.")
            print(mostrar_ahorcado(6 - intentos))

        print(f"Palabra: {' '.join(palabra_adivinada)}")
        print(f"Letras adivinadas: {', '.join(letras_adivinadas)}")

    if "_" not in palabra_adivinada:
        print("¡Felicidades! Has adivinado la palabra.")
    else:
        print(f"Perdiste. La palabra era '{palabra}'.")

print("Juego del Ahorcado")
jugar_ahorcado()
