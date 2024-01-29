import csv
import json

# Tu JSON de ejemplo (puedes reemplazarlo con tu propio JSON)
json_data = '{"nombre": "Juan", "edad": 25, "ciudad": "Ejemplo"}'

# Parsear el JSON
data = json.loads(json_data)

# Especificar el nombre del archivo CSV de salida
csv_filename = 'salida.csv'

# Abrir el archivo CSV en modo de escritura
with open(csv_filename, 'w', newline='') as csvfile:
    # Crear un objeto escritor CSV
    csv_writer = csv.writer(csvfile)

    # Escribir las claves (encabezados) como la primera fila en el CSV
    csv_writer.writerow(data.keys())

    # Escribir los valores como filas en el CSV
    csv_writer.writerow(data.values())

print(f'Se ha convertido el JSON a CSV en {csv_filename}')
