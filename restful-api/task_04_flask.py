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

#   Creating the Flask application instance
app = Flask(__name__)

#   In-memory data store for users
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}

#   Route for the root URL, returning a welcome message


@app.route('/')
def home():
    #   Return a welcome message
    return "Welcome to the Flask API!"

#   Route to get all usernames


@app.route('/data')
def get_data():
    #   Return a list of all usernames
    return jsonify(list(users.keys()))

#   Route to check the API status


@app.route('/status')
def status():
    #   Return OK status
    return "OK"

#   Route to get API information


@app.route('/info')
def get_info():
    #   Return API version and description
    return jsonify({
        "version": "1.0",
        "description": "A simple API built with Flask"
    })

#   Route to get user data for a specific username


@app.route('/users/<username>')
def get_user(username):
    #   Find user data for the given username
    user = users.get(username)
    #   If user exists, return the user data
    if user:
        return jsonify(user)
    #   If user does not exist, return an error message & 404 status code
    else:
        return jsonify({"error": "User not found"}), 404

#   Route to add a new user, accepts POST requests only


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


#   Start the Flask development server
if __name__ == "__main__":
    #   Run the application
    app.run()
