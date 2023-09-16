import tkinter as tk

# Función para imprimir "Hola Mundo" en la consola
def imprimir_hola_mundo():
    print("Hola Mundo")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Aplicación")

# Crear un botón que llama a la función imprimir_hola_mundo cuando se hace clic
boton_hola = tk.Button(ventana, text="Imprimir Hola Mundo", command=imprimir_hola_mundo)
boton_hola.pack()

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()
