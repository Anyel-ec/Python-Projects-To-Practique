import pandas as pd

# Crear un DataFrame de empleados
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'María', 'Pedro'],
    'Edad': [30, 28, 35, 25, 32],
    'Salario': [50000, 48000, 60000, 45000, 55000],
    'Departamento': ['Ventas', 'Recursos Humanos', 'Ventas', 'Tecnología', 'Tecnología']
}

df_empleados = pd.DataFrame(data)

# Operaciones en el DataFrame

# 1. Calcular el salario promedio de los empleados:
salario_promedio = df_empleados['Salario'].mean()
print(f"Salario promedio: ${salario_promedio:.2f}")

# 2. Encontrar al empleado más joven:
empleado_mas_joven = df_empleados[df_empleados['Edad'] == df_empleados['Edad'].min()]
print("Empleado más joven:")
print(empleado_mas_joven)

# Consultas en el DataFrame

# 1. Filtrar empleados del departamento de Tecnología:
empleados_tecnologia = df_empleados[df_empleados['Departamento'] == 'Tecnología']
print("Empleados del departamento de Tecnología:")
print(empleados_tecnologia)

# 2. Ordenar los empleados por salario de forma descendente:
empleados_ordenados = df_empleados.sort_values(by='Salario', ascending=False)
print("Empleados ordenados por salario descendente:")
print(empleados_ordenados)
