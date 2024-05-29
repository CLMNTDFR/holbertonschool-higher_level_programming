#!/usr/bin/python3
"""
The http.server module in Python’s standard library provides
basic classes for implementing web servers. While it’s not typically
used for production applications, it’s a handy tool for building simple
web servers and understanding the basics of web programming without
relying on third-party libraries.
"""

import http.server
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info_data = {"version": "1.0",
                         "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info_data).encode())
        else:
            self.send_error(404, 'Endpoint not found')


def start_server():
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Serveur démarré sur le port 8000...')
    httpd.serve_forever()


if __name__ == '__main__':
    start_server()
