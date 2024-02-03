from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Definir el nombre del archivo JSON para almacenar los datos
json_file_path = "mantenimiento_vias_data.json"

# Función para cargar datos desde el archivo JSON
def cargar_datos_desde_json():
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            return json.load(json_file)
    else:
        return []

# Función para guardar datos en el archivo JSON
def guardar_datos_en_json(data):
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)

# Datos de inicio con un ID autoincremental
mantenimiento_vias_data = cargar_datos_desde_json()
id_counter = 1 if not mantenimiento_vias_data else max(m['id'] for m in mantenimiento_vias_data) + 1

# Rutas CRUD
@app.route('/api/v1/mantenimiento_vias', methods=['GET'])
def obtener_mantenimientos():
    return jsonify(mantenimiento_vias_data)

@app.route('/api/v1/mantenimiento_vias', methods=['POST'])
def agregar_mantenimiento():
    global id_counter
    nuevo_mantenimiento = request.json
    nuevo_mantenimiento["id"] = id_counter
    id_counter += 1
    mantenimiento_vias_data.append(nuevo_mantenimiento)
    guardar_datos_en_json(mantenimiento_vias_data)
    return jsonify({"mensaje": "Mantenimiento agregado exitosamente"})

@app.route('/api/v1/mantenimiento_vias/<int:mantenimiento_id>', methods=['GET'])
def obtener_mantenimiento(mantenimiento_id):
    mantenimiento = next((m for m in mantenimiento_vias_data if m['id'] == mantenimiento_id), None)
    return jsonify(mantenimiento)

@app.route('/api/v1/mantenimiento_vias/<int:mantenimiento_id>', methods=['PUT'])
def actualizar_mantenimiento(mantenimiento_id):
    nuevo_mantenimiento = request.json
    for mantenimiento in mantenimiento_vias_data:
        if mantenimiento['id'] == mantenimiento_id:
            mantenimiento.update(nuevo_mantenimiento)
            guardar_datos_en_json(mantenimiento_vias_data)
            return jsonify({"mensaje": "Mantenimiento actualizado exitosamente"})
    return jsonify({"error": "Mantenimiento no encontrado"}), 404

@app.route('/api/v1/mantenimiento_vias/<int:mantenimiento_id>', methods=['DELETE'])
def eliminar_mantenimiento(mantenimiento_id):
    global mantenimiento_vias_data
    mantenimiento_vias_data = [m for m in mantenimiento_vias_data if m['id'] != mantenimiento_id]
    guardar_datos_en_json(mantenimiento_vias_data)
    return jsonify({"mensaje": "Mantenimiento eliminado exitosamente"})

# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)
