from pymongo import MongoClient

class MongoDB:
    def __init__(self, host='localhost', port=27017, database='mydb'):
        self.client = MongoClient(host, port)
        self.db = self.client[database]

    def create_document(self, collection_name, data):
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        return result.inserted_id

    def read_document(self, collection_name, query={}):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def update_document(self, collection_name, query, data):
        collection = self.db[collection_name]
        result = collection.update_one(query, {'$set': data})
        return result.modified_count

    def delete_document(self, collection_name, query):
        collection = self.db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count

if __name__ == '__main__':
    # Crear una instancia de MongoDB
    db = MongoDB()

    # Ejemplo de uso:
    
    # Crear un documento
    data_to_insert = {'name': 'Anyel EC', 'age': 30}
    inserted_id = db.create_document('users', data_to_insert)
    print(f'Nuevo documento creado con ID: {inserted_id}')

    # Leer un documento
    user = db.read_document('users', {'name': 'Anyel EC'})
    print('Documento encontrado:')
    print(user)

    # Actualizar un documento
    update_query = {'name': 'Anyel EC'}
    new_data = {'age': 31}
    updated_count = db.update_document('users', update_query, new_data)
    print(f'Número de documentos actualizados: {updated_count}')

    # Leer el documento actualizado
    updated_user = db.read_document('users', {'name': 'Anyel EC'})
    print('Documento actualizado:')
    print(updated_user)

    # Eliminar un documento
    delete_query = {'name': 'Anyel EC'}
    deleted_count = db.delete_document('users', delete_query)
    print(f'Número de documentos eliminados: {deleted_count}')
