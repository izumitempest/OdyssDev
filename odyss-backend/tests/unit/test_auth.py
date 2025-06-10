import unittest
from app import create_app
from app.extensions import db

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("development")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
    
    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
    
    def test_register(self):
        response = self.client.post("/api/v1/auth/register", json={"email": "test@example.com", "password": "password"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("User created", response.get_json()["message"])
    
    def test_login(self):
        self.client.post("/api/v1/auth/register", json={"email": "test@example.com", "password": "password"})
        response = self.client.post("/api/v1/auth/login", json={"email": "test@example.com", "password": "password"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.get_json())

if __name__ == "__main__":
    unittest.main()