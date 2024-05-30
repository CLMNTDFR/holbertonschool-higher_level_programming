import unittest
import json
from http.server import HTTPServer
import threading
import requests

from task_03_http_server import SimpleHTTPRequestHandler

class TestHTTPServer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.server_address = ('', 8000)
        cls.httpd = HTTPServer(cls.server_address, SimpleHTTPRequestHandler)
        cls.server_thread = threading.Thread(target=cls.httpd.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()
        cls.server_thread.join()

    def test_root(self):
        response = requests.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, this is a simple API!")

    def test_data_endpoint(self):
        response = requests.get('http://localhost:8000/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        expected_data = {"name": "John", "age": 30, "city": "New York"}
        self.assertEqual(response.json(), expected_data)

    def test_status_endpoint(self):
        response = requests.get('http://localhost:8000/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    def test_info_endpoint(self):
        response = requests.get('http://localhost:8000/info')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        expected_info = {
            "version": "1.0",
            "description": "A simple API built with http.server",
        }
        self.assertEqual(response.json(), expected_info)

    def test_invalid_endpoint(self):
        response = requests.get('http://localhost:8000/jdhdgfdhjej')
        self.assertEqual(response.status_code, 404)
        self.assertIn("Endpoint not found", response.text)
    
    def test_double_invalid_endpoint(self):
        response = requests.get('http://localhost:8000/status/12345')
        self.assertEqual(response.status_code, 404)
        self.assertIn("Endpoint not found", response.text)

if __name__ == '__main__':
    unittest.main()
