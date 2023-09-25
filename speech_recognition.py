import speech_recognition as sr

# Inicializa el reconocedor
recognizer = sr.Recognizer()

# Captura audio del micrófono
with sr.Microphone() as source:
    print("Habla algo...")
    audio = recognizer.listen(source)

# Intenta reconocer el audio
try:
    # Reconoce el audio usando Google Web Speech API
    texto = recognizer.recognize_google(audio, language="es-ES")
    print(f"Texto reconocido: {texto}")
except sr.UnknownValueError:
    print("No se pudo entender el audio")
except sr.RequestError as e:
    print(f"Error en la solicitud: {e}")
