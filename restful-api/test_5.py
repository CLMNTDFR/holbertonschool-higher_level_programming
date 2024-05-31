import unittest
import json
from task_05_basic_security import app, users

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test unauthorized access to basic-protected route
    def test_unauthorized_basic_protected(self):
        response = self.app.get('/basic-protected')
        self.assertEqual(response.status_code, 401)

    # Test valid basic authentication to basic-protected route
    def test_valid_basic_auth(self):
        response = self.app.get('/basic-protected', headers={"Authorization": "Basic dXNlcjE6cGFzc3dvcmQ="})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Basic Auth: Access Granted", response.data)

    # Test invalid basic authentication to basic-protected route
    def test_invalid_basic_auth(self):
        response = self.app.get('/basic-protected', headers={"Authorization": "Basic dXNlcjE6cGFzc3dvcmR="})
        self.assertEqual(response.status_code, 401)

    # Test login route
    def test_login(self):
        response = self.app.post('/login', json={"username": "user1", "password": "password"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("access_token", data)

    # Test unauthorized access to jwt-protected route
    def test_unauthorized_jwt_protected(self):
        response = self.app.get('/jwt-protected')
        self.assertEqual(response.status_code, 401)

    # Test valid jwt authentication to jwt-protected route
    def test_valid_jwt_auth(self):
        # Get token
        login_response = self.app.post('/login', json={"username": "user1", "password": "password"})
        login_data = json.loads(login_response.data)
        token = login_data["access_token"]

        # Access jwt-protected route with token
        response = self.app.get('/jwt-protected', headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"JWT Auth: Access Granted", response.data)

    # Test unauthorized access to admin-only route
    def test_unauthorized_admin_only(self):
        response = self.app.get('/admin-only')
        self.assertEqual(response.status_code, 401)

    # Test access to admin-only route with user token
    def test_user_access_admin_only(self):
        # Get user token
        login_response = self.app.post('/login', json={"username": "user1", "password": "password"})
        login_data = json.loads(login_response.data)
        token = login_data["access_token"]

        # Access admin-only route with user token
        response = self.app.get('/admin-only', headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 403)

    # Test access to admin-only route with admin token
    def test_admin_access_admin_only(self):
        # Get admin token
        login_response = self.app.post('/login', json={"username": "admin1", "password": "adminpass"})
        login_data = json.loads(login_response.data)
        token = login_data["access_token"]

        # Access admin-only route with admin token
        response = self.app.get('/admin-only', headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Admin Access: Granted", response.data)

if __name__ == '__main__':
    unittest.main()
