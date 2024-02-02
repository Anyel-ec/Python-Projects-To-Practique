from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos de inicio
mantenimiento_vias_data = [
    {
        "ubicacion": "Carretera Panamericana Sur",
        "tipo": "Mantenimiento preventivo",
        "inicio": "2024-04-01",
        "fin": "2024-04-15"
    }
]

# Rutas CRUD
@app.route('/api/v1/mantenimiento_vias', methods=['GET'])
def obtener_mantenimientos():
    return jsonify({"mantenimiento_vias": mantenimiento_vias_data})

@app.route('/api/v1/mantenimiento_vias', methods=['POST'])
def agregar_mantenimiento():
    nuevo_mantenimiento = request.json
    mantenimiento_vias_data.append(nuevo_mantenimiento)
    return jsonify({"mensaje": "Mantenimiento agregado exitosamente"})

@app.route('/api/v1/mantenimiento_vias/<ubicacion>', methods=['GET'])
def obtener_mantenimiento(ubicacion):
    mantenimiento = next((m for m in mantenimiento_vias_data if m['ubicacion'] == ubicacion), None)
    return jsonify({"mantenimiento": mantenimiento})

@app.route('/api/v1/mantenimiento_vias/<ubicacion>', methods=['PUT'])
def actualizar_mantenimiento(ubicacion):
    nuevo_mantenimiento = request.json
    for mantenimiento in mantenimiento_vias_data:
        if mantenimiento['ubicacion'] == ubicacion:
            mantenimiento.update(nuevo_mantenimiento)
            return jsonify({"mensaje": "Mantenimiento actualizado exitosamente"})
    return jsonify({"error": "Mantenimiento no encontrado"}), 404

@app.route('/api/v1//mantenimiento_vias/<ubicacion>', methods=['DELETE'])
def eliminar_mantenimiento(ubicacion):
    global mantenimiento_vias_data
    mantenimiento_vias_data = [m for m in mantenimiento_vias_data if m['ubicacion'] != ubicacion]
    return jsonify({"mensaje": "Mantenimiento eliminado exitosamente"})

# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)
