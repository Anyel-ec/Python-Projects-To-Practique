from pymongo import MongoClient

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {"name": self.name, "age": self.age, "grade": self.grade}

class MongoDBCRUD:
    def __init__(self, connection_string, database_name, collection_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def create(self, obj):
        data = obj.to_dict()
        result = self.collection.insert_one(data)
        return result.inserted_id

    def read(self, query=None):
        if query is None:
            query = {}
        return list(self.collection.find(query))

    def update(self, query, update_data):
        result = self.collection.update_many(query, {"$set": update_data})
        return result.modified_count

    def delete(self, query):
        result = self.collection.delete_many(query)
        return result.deleted_count

# Ejemplo de uso
if __name__ == "__main__":
    # Conéctate a la base de datos MongoDB (asegúrate de tener MongoDB en ejecución)
    connection_string = "mongodb://localhost:27017/"
    database_name = "school"
    collection_name = "students"

    # Crea instancias de la clase Student
    student1 = Student("John Doe", 20, "A")
    student2 = Student("Jane Smith", 22, "B")

    # Crea una instancia de MongoDBCRUD
    crud = MongoDBCRUD(connection_string, database_name, collection_name)

    # Crea estudiantes en la base de datos
    student1_id = crud.create(student1)
    student2_id = crud.create(student2)

    print(f"Estudiantes creados con IDs: {student1_id}, {student2_id}")

    # Lee todos los estudiantes
    all_students = crud.read()
    print("Todos los estudiantes:")
    for student in all_students:
        print(student)

    # Actualiza la edad del estudiante John Doe
    update_query = {"name": "John Doe"}
    update_data = {"age": 21}
    updated_count = crud.update(update_query, update_data)
    print(f"Estudiantes actualizados: {updated_count}")

    # Lee nuevamente todos los estudiantes después de la actualización
    updated_students = crud.read()
    print("Estudiantes después de la actualización:")
    for student in updated_students:
        print(student)

    # Elimina a Jane Smith de la base de datos
    delete_query = {"name": "Jane Smith"}
    deleted_count = crud.delete(delete_query)
    print(f"Estudiantes eliminados: {deleted_count}")

    # Lee nuevamente todos los estudiantes después de la eliminación
    remaining_students = crud.read()
    print("Estudiantes restantes después de la eliminación:")
    for student in remaining_students:
        print(student)
