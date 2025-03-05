from flask import Flask, jsonify, render_template, request, abort

app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"}
]

# Endpoint 1: Welcome Message
@app.route('/api/welcome', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the Flask API!"})

# Endpoint 2: List of Items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Endpoint 3: Details of a Specific Item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        abort(404, description="Item not found")

# Render HTML Page Using Jinja2
@app.route('/items', methods=['GET'])
def show_items():
    return render_template('items.html', items=items)

# POST Request to Add New Items
@app.route('/api/items', methods=['POST'])
def add_item():
    if not request.json or not 'name' in request.json:
        abort(400, description="Invalid input")
    
    new_item = {
        "id": len(items) + 1,
        "name": request.json['name'],
        "description": request.json.get('description', "")
    }
    items.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)