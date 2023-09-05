# Declaración de un array con valores iniciales
nombres = ["Juan", "María", "Carlos", "Ana"]

# Acceso a un elemento específico por índice
primer_nombre = nombres[0]
print("Primer nombre:", primer_nombre)

# Modificación de un elemento
nombres[1] = "Luis"

# Iteración usando un bucle for
print("Iteración con for:")
for nombre in nombres:
    print(nombre)

# Iteración usando un bucle while
print("Iteración con while:")
i = 0
while i < len(nombres):
    print(nombres[i])
    i += 1

# Añadir un elemento al final del array
nombres.append("Elena")

# Insertar un elemento en una posición específica
nombres.insert(2, "Pedro")

# Eliminar un elemento por valor
nombres.remove("Carlos")

# Eliminar un elemento por índice
del nombres[0]

# Eliminar y obtener el último elemento
ultimo_nombre = nombres.pop()
print("Último nombre eliminado:", ultimo_nombre)

# Obtener la longitud del array
cantidad_de_nombres = len(nombres)
print("Cantidad de nombres:", cantidad_de_nombres)

# Ordenar el array alfabéticamente
nombres.sort()

# Ordenar el array en orden inverso
nombres.reverse()

# Buscar un elemento en el array
if "María" in nombres:
    print("María está en la lista.")
else:
    print("María no está en la lista.")
