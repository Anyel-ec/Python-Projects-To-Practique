import pyodbc # pip install pyodbc

try: 
    conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=localhost;'
                            'Database=Estudiante;'
                            'UID: Hola;'
                            'PWD: Hola;'
                            'Trusted_Connection=yes;')
    print("Conexion exitosa")
except Exception as e:
    print("Ocurrio un error al conectar a SQL Server: ", e)
    
# Create
def crear (id, nombre, apellido):
    cursor = conn.cursor()
    cursor.execute(' INSERT INTO ESTUDIANTE VALUES (?,?,?)', (id, nombre, apellido))
    cursor.commit()
    print("Estudiante creado con exito")
    cursor.close()
    return 'Estudiante creado con exito HTML'
