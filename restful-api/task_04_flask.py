#!/usr/bin/env python3
"""
This script sets up a simple API using Flask.
It includes endpoints to:
- Return a welcome message at the root URL.
- Provide a list of all usernames.
- Check the API status.
- Return API information.
- Get user data for a specific username.
- Add a new user via a POST request.
"""

#   Importing Flask and necessary functions
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    return jsonify(users.get(username))


@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    username = user_data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = {
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]})


if __name__ == "__main__":
    app.run()
