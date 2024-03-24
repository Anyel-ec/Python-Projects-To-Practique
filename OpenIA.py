import openai

# Configura tu clave de API de OpenAI
openai.api_key = 'HJJEYU3232WEWEYUGDS67WETEREDFSGDCUYGD84GFYUEWDVSEXGD' #Utiliza tu clave real de la API 

def generar_descripcion_psicologia_color(color):
    prompt = f"Describe la psicología del color {color}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Ejemplo de uso
color = "rojo"
descripcion = generar_descripcion_psicologia_color(color)
print(f"Descripción de la psicología del color {color}:")
print(descripcion)
