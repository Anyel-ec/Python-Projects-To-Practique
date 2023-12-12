# Developer by Anyel EC
# Whatsapp: +593 99 167 5490
# Linkedln: Anyel EC

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
todos = [
    {"id": 1, "task": "Buy milk"},
    {"id": 2, "task": "Exercise"},
    {"id": 3, "task": "Code in Python"},
]

# Route to get all items
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

# Route to get an item by ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((item for item in todos if item["id"] == todo_id), None)
    if todo is not None:
        return jsonify({'todo': todo})
    else:
        return jsonify({'error': 'Item not found'}), 404

# Route to create a new item
@app.route('/todos', methods=['POST'])
def create_todo():
    if not request.json or 'task' not in request.json:
        return jsonify({'error': 'Task is required'}), 400

    new_todo = {
        'id': len(todos) + 1,
        'task': request.json['task']
    }

    todos.append(new_todo)
    return jsonify({'todo': new_todo}), 201

# Route to update an item by ID
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((item for item in todos if item["id"] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Item not found'}), 404

    if 'task' in request.json:
        todo['task'] = request.json['task']

    return jsonify({'todo': todo})

# Route to delete an item by ID
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [item for item in todos if item["id"] != todo_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
