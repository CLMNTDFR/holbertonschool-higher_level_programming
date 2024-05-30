#!/usr/bin/env python3
from flask import Flask
from flask import jsonify
from flask import request

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
    username = user_data['username']
    users[username] = {
        "name": user_data["name"],
        "age": user_data["age"],
        "city": user_data["city"]
    }
    return jsonify({"message": "User added", "user": users[username]})


if __name__ == "__main__":
    app.run()
