class Estudiante:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

class RegistroEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def crear_estudiante(self, id, nombre, edad):
        estudiante = Estudiante(id, nombre, edad)
        self.estudiantes.append(estudiante)
        print(f"Estudiante {nombre} creado satisfactoriamente.")

    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
        else:
            print("Lista de Estudiantes:")
            for estudiante in self.estudiantes:
                print(f"ID: {estudiante.id}, Nombre: {estudiante.nombre}, Edad: {estudiante.edad}")

    def actualizar_estudiante(self, id, nombre, edad):
        for estudiante in self.estudiantes:
            if estudiante.id == id:
                estudiante.nombre = nombre
                estudiante.edad = edad
                print(f"Estudiante {nombre} actualizado satisfactoriamente.")
                return
        print(f"No se encontró un estudiante con ID {id}.")

    def eliminar_estudiante(self, id):
        for estudiante in self.estudiantes:
            if estudiante.id == id:
                self.estudiantes.remove(estudiante)
                print(f"Estudiante con ID {id} eliminado satisfactoriamente.")
                return
        print(f"No se encontró un estudiante con ID {id}.")

# Ejemplo de uso del proyecto
registro = RegistroEstudiantes()

registro.crear_estudiante(1, "Juan Perez", 20)
registro.crear_estudiante(2, "Ana Gomez", 22)
registro.mostrar_estudiantes()

registro.actualizar_estudiante(1, "Juanita Perez", 21)
registro.mostrar_estudiantes()

registro.eliminar_estudiante(2)
registro.mostrar_estudiantes()
