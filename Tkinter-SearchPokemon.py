import tkinter as tk
from tkinter import messagebox

# Arreglo de Pokémon
pokemons = {
    "Bulbasaur": "Planta",
    "Charmander": "Fuego",
    "Squirtle": "Agua",
    "Pikachu": "Eléctrico",
    "Jigglypuff": "Normal",
    "Eevee": "Normal",
    "Snorlax": "Normal",
    "Mewtwo": "Psíquico",
    "Gengar": "Fantasma",
    "Dragonite": "Dragón"
}

def buscar_pokemon():
    nombre = entry.get()
    if nombre in pokemons:
        tipo = pokemons[nombre]
        messagebox.showinfo("Resultado", f"{nombre} es de tipo {tipo}.")
    else:
        messagebox.showerror("Error", f"No se encontró el Pokémon {nombre}.")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Buscar Pokémon")

# Etiqueta y entrada para ingresar el nombre del Pokémon
label = tk.Label(ventana, text="Nombre del Pokémon:")
label.pack(pady=10)
entry = tk.Entry(ventana)
entry.pack()

# Botón para buscar el Pokémon
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_pokemon)
boton_buscar.pack(pady=5)

# Ejecutar la ventana
ventana.mainloop()
