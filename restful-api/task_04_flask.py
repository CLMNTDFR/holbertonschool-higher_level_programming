#!/usr/bin/env python3
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def 


if __name__ == "__main__":
    app.run()
