# Author: Anyel EC
import pymongo

class Person:
    def __init__(self, name, age, occupation):
        # Constructor for the Person class
        self.name = name
        self.age = age
        self.occupation = occupation

    def __str__(self):
        # String representation of a Person object
        return f"Name: {self.name}, Age: {self.age}, Occupation: {self.occupation}"

class DatabaseManager:
    def __init__(self):
        # Constructor for the DatabaseManager class
        # Connect to the MongoDB server
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        # Access the "crud_db" database
        self.database = self.client["crud_db"]
        # Access the "personas" collection within the database
        self.collection = self.database["personas"]

    def create_person(self, person):
        # Method to create a new person in the database
        person_dict = {"nombre": person.name, "edad": person.age, "ocupacion": person.occupation}
        # Insert the person's data into the collection
        result = self.collection.insert_one(person_dict)
        print(f"Person created with ID: {result.inserted_id}")

    def read_people(self):
        # Method to read all people from the database
        people = self.collection.find()
        # Display information about each person
        for person in people:
            print(f"ID: {person['_id']}, {person['nombre']}, {person['edad']} years old, Occupation: {person['ocupacion']}")

    def update_person(self, person_id, new_data):
        # Method to update a person's data in the database
        result = self.collection.update_one({"_id": person_id}, {"$set": new_data})
        if result.modified_count > 0:
            print(f"Person updated successfully.")
        else:
            print(f"Person with ID {person_id} not found.")

    def delete_person(self, person_id):
        # Method to delete a person from the database
        result = self.collection.delete_one({"_id": person_id})
        if result.deleted_count > 0:
            print(f"Person deleted successfully.")
        else:
            print(f"Person with ID {person_id} not found.")

# Example of usage
db_manager = DatabaseManager()

# Create persons
person1 = Person("Juan", 25, "Student")
person2 = Person("Ana", 30, "Engineer")
db_manager.create_person(person1)
db_manager.create_person(person2)

# Read persons
print("\nPersons in the database:")
db_manager.read_people()

# Update person
updated_person_data = {"nombre": "Juan Pérez", "edad": 26, "ocupacion": "Developer"}
db_manager.update_person(1, updated_person_data)

# Read persons after the update
print("\nPersons after the update:")
db_manager.read_people()

# Delete person
db_manager.delete_person(2)

# Read persons after the deletion
print("\nPersons after the deletion:")
db_manager.read_people()

