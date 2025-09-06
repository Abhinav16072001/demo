from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:F6NBm46v3bzJ5Av1@test.agfnj5q.mongodb.net/?retryWrites=true&w=majority&appName=Test")
db = client["mydatabase"]
collection = db["submissions"]

@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "No JSON received"}), 400

        doc = {
            "name": data.get("name"),
            "email": data.get("email"),
            "message": data.get("message")
        }
        collection.insert_one(doc)

        return jsonify({"status": "success", "message": "Data saved successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.get_json(force=True)

    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    if not item_name:
        return jsonify({"error": "Item Name is required"}), 400

    todo_id = todos.insert_one({
        "itemName": item_name,
        "itemDescription": item_description,
    }).inserted_id

    return jsonify({
        "message": "To-Do item saved successfully",
        "id": str(todo_id),
        "itemName": item_name,
        "itemDescription": item_description
    }), 201


if __name__ == "__main__":
    app.run(port=5000, debug=True)
