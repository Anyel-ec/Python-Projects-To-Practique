from translate import Translator

def traducir_texto(texto, idioma_origen, idioma_destino):
    try:
        translator = Translator(from_lang=idioma_origen, to_lang=idioma_destino)
        traduccion = translator.translate(texto)
        return traduccion
    except Exception as e:
        return str(e)

# Ejemplo de uso
texto_a_traducir = "Hola, ¿cómo estás?"
idioma_origen = "es"
idioma_destino = "en"

traduccion = traducir_texto(texto_a_traducir, idioma_origen, idioma_destino)
print("Texto original:", texto_a_traducir)
print("Traducción:", traduccion)
