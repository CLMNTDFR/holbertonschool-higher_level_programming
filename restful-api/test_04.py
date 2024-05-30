import unittest
import json
from task_04_flask import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b'Welcome to the Flask API!')

    def test_get_data(self):
        response = self.app.get('/data')
        data = json.loads(response.data)
        self.assertEqual(data, ['jane', 'john', 'alice'])  # Update to include 'alice'

    def test_status(self):
        response = self.app.get('/status')
        self.assertEqual(response.data, b'OK')

    def test_get_info(self):
        response = self.app.get('/info')
        data = json.loads(response.data)
        self.assertEqual(data, {"version": "1.0", "description": "A simple API built with Flask"})

    def test_get_user_jane(self):
        response = self.app.get('/users/jane')
        data = json.loads(response.data)
        self.assertEqual(data, {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"})

    def test_get_user_john(self):
        response = self.app.get('/users/john')
        data = json.loads(response.data)
        self.assertEqual(data, {"username": "john", "name": "John", "age": 30, "city": "New York"})

    def test_add_user(self):
        new_user = {"username": "alice", "name": "Alice", "age": 25, "city": "San Francisco"}
        response = self.app.post('/add_user', json=new_user)
        data = json.loads(response.data)
        self.assertEqual(data, {"message": "User added", "user": new_user})

    def test_undefined_endpoint(self):
        response = self.app.get('/undefined')
        data = json.loads(response.data)
        self.assertEqual(data, {"error": "Endpoint not found"})


if __name__ == '__main__':
    unittest.main()
