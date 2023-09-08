class Empleado:
    def __init__(self, id, nombre, salario):
        self.id = id
        self.nombre = nombre
        self.salario = salario

class GestionEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def buscar_empleado(self, id):
        for empleado in self.empleados:
            if empleado.id == id:
                return empleado
        return None

    def listar_empleados(self):
        for empleado in self.empleados:
            print(f"ID: {empleado.id}, Nombre: {empleado.nombre}, Salario: {empleado.salario}")

    def actualizar_empleado(self, id, nombre, salario):
        empleado = self.buscar_empleado(id)
        if empleado:
            empleado.nombre = nombre
            empleado.salario = salario
            print("Empleado actualizado con éxito.")
        else:
            print("Empleado no encontrado.")

    def eliminar_empleado(self, id):
        empleado = self.buscar_empleado(id)
        if empleado:
            self.empleados.remove(empleado)
            print("Empleado eliminado con éxito.")
        else:
            print("Empleado no encontrado.")

# Crear una instancia de la clase GestionEmpleados
gestion_empleados = GestionEmpleados()

# Agregar empleados
empleado1 = Empleado(1, "Juan", 50000)
empleado2 = Empleado(2, "Ana", 60000)
gestion_empleados.agregar_empleado(empleado1)
gestion_empleados.agregar_empleado(empleado2)

# Listar empleados
print("Lista de empleados:")
gestion_empleados.listar_empleados()

# Actualizar empleado
gestion_empleados.actualizar_empleado(1, "Juan Pérez", 55000)

# Eliminar empleado
gestion_empleados.eliminar_empleado(2)

# Listar empleados actualizados
print("\nLista de empleados después de actualizar y eliminar:")
gestion_empleados.listar_empleados()
