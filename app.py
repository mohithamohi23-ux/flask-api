from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}

@app.route("/")
def home():
    return jsonify({"message": "User Management API is Running"}), 200

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]), 200
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if "id" not in data or "name" not in data or "email" not in data:
        return jsonify({"error": "id, name and email are required"}), 400
    if data["id"] in users:
        return jsonify({"error": "User ID already exists"}), 409

    users[data["id"]] = {
        "name": data["name"],
        "email": data["email"]
    }
    return jsonify({"message": "User created successfully"}), 201

@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    users[user_id].update(data)
    return jsonify({"message": "User updated successfully"}), 200

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
