import tkinter as tk

def mostrar_hola_mundo():
    etiqueta.config(text="¡Hola Mundo!")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Hola Mundo GUI")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Presiona el botón para saludar")

# Crear un botón que llama a la función mostrar_hola_mundo al hacer clic
boton_saludar = tk.Button(ventana, text="Saludar", command=mostrar_hola_mundo)

# Colocar la etiqueta y el botón en la ventana
etiqueta.pack(pady=10)
boton_saludar.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()
