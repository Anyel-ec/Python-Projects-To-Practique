# Inicializar una lista vacía para almacenar los datos
lista_de_elementos = []

# Función para crear un nuevo elemento
def crear_elemento(nombre, edad):
    nuevo_elemento = {'nombre': nombre, 'edad': edad}
    lista_de_elementos.append(nuevo_elemento)
    print(f'Se ha creado un nuevo elemento: {nuevo_elemento}')

# Función para leer todos los elementos
def leer_elementos():
    for elemento in lista_de_elementos:
        print(f'Nombre: {elemento["nombre"]}, Edad: {elemento["edad"]}')

# Función para actualizar un elemento existente
def actualizar_elemento(nombre, nueva_edad):
    for elemento in lista_de_elementos:
        if elemento['nombre'] == nombre:
            elemento['edad'] = nueva_edad
            print(f'Se ha actualizado el elemento: {elemento}')
            return
    print(f'Elemento con nombre "{nombre}" no encontrado.')

# Función para eliminar un elemento existente
def eliminar_elemento(nombre):
    for elemento in lista_de_elementos:
        if elemento['nombre'] == nombre:
            lista_de_elementos.remove(elemento)
            print(f'Se ha eliminado el elemento: {elemento}')
            return
    print(f'Elemento con nombre "{nombre}" no encontrado.')

# Ejemplos de uso
crear_elemento('Alice', 30)
crear_elemento('Bob', 25)
leer_elementos()
actualizar_elemento('Alice', 35)
eliminar_elemento('Bob')
leer_elementos()
