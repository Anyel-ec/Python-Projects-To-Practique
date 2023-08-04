import mysql.connector

# Establecer la conexión con la base de datos
conexion = mysql.connector.connect(
    host='tu_host',
    user='tu_usuario',
    password='tu_contraseña',
    database='nombre_de_tu_base_de_datos'
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Operación de creación (CREATE)
def insertar_datos(nombre, edad, correo):
    consulta = "INSERT INTO tabla (nombre, edad, correo) VALUES (%s, %s, %s)"
    datos = (nombre, edad, correo)
    cursor.execute(consulta, datos)
    conexion.commit()

# Operación de lectura (READ)
def obtener_datos():
    consulta = "SELECT * FROM tabla"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    return resultados

# Operación de actualización (UPDATE)
def actualizar_datos(id, nuevo_nombre, nueva_edad, nuevo_correo):
    consulta = "UPDATE tabla SET nombre=%s, edad=%s, correo=%s WHERE id=%s"
    datos = (nuevo_nombre, nueva_edad, nuevo_correo, id)
    cursor.execute(consulta, datos)
    conexion.commit()

# Operación de eliminación (DELETE)
def eliminar_datos(id):
    consulta = "DELETE FROM tabla WHERE id=%s"
    datos = (id,)
    cursor.execute(consulta, datos)
    conexion.commit()

# Cerrar el cursor y la conexión al terminar
def cerrar_conexion():
    cursor.close()
    conexion.close()
