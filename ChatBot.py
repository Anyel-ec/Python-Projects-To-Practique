import nltk
import random
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Pares de patrones y respuestas
pares = [
    ["¿Cómo está el clima hoy?", ["El clima es soleado y cálido."]],
    ["¿Cuál es la temperatura actual?", ["La temperatura actual es de 25 grados Celsius."]],
    ["¿Qué tiempo hará mañana?", ["Mañana se espera un clima soleado con una temperatura máxima de 28 grados."]],
    ["Hola", ["¡Hola!", "Hola, ¿en qué puedo ayudarte?"]],
    ["Adiós", ["Hasta luego.", "Adiós."]],
]

# Crea un chatbot
chatbot = Chat(pares, reflections)

# Función principal para interactuar con el chatbot
def chat():
    print("Hola, soy un chatbot de clima hecho por Anyel EC . Puedes preguntarme sobre el clima o simplemente saludar.")
    print("Escribe 'salir' para finalizar la conversación.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'salir':
            print("Chatbot: Hasta luego.")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    chat()
