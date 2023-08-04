import psycopg2
from psycopg2 import Error

# Configura la información de conexión a la base de datos
db_params = {
    'host': 'tu_host',
    'database': 'tu_base_de_datos',
    'user': 'tu_usuario',
    'password': 'tu_contraseña'
}

# Función para insertar un nuevo registro
def insert_record(connection, cursor, name, age):
    try:
        query = "INSERT INTO personas (nombre, edad) VALUES (%s, %s);"
        cursor.execute(query, (name, age))
        connection.commit()
        print("Registro insertado correctamente.")
    except Error as e:
        print("Error al insertar el registro:", e)

# Función para leer todos los registros
def read_records(connection, cursor):
    try:
        query = "SELECT * FROM personas;"
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Error as e:
        print("Error al leer los registros:", e)

# Función para actualizar un registro
def update_record(connection, cursor, record_id, new_age):
    try:
        query = "UPDATE personas SET edad = %s WHERE id = %s;"
        cursor.execute(query, (new_age, record_id))
        connection.commit()
        print("Registro actualizado correctamente.")
    except Error as e:
        print("Error al actualizar el registro:", e)

# Función para eliminar un registro
def delete_record(connection, cursor, record_id):
    try:
        query = "DELETE FROM personas WHERE id = %s;"
        cursor.execute(query, (record_id,))
        connection.commit()
        print("Registro eliminado correctamente.")
    except Error as e:
        print("Error al eliminar el registro:", e)

# Función principal
def main():
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Ejemplos de uso de las funciones
        insert_record(connection, cursor, "Ejemplo 1", 25)
        insert_record(connection, cursor, "Ejemplo 2", 30)
        read_records(connection, cursor)
        update_record(connection, cursor, 1, 26)
        delete_record(connection, cursor, 2)

        cursor.close()
        connection.close()
    except Error as e:
        print("Error de conexión:", e)


main()
