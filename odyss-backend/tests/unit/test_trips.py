import unittest
from app import create_app
from app.extensions import db
from tests.factories import UserFactory, TripFactory

class TripsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("development")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            self.user = UserFactory.create()
            login_response = self.client.post("/api/v1/auth/login", json={"email": self.user.email, "password": "password"})
            self.token = login_response.get_json()["access_token"]
    
    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
    
    def test_create_trip(self):
        response = self.client.post(
            "/api/v1/trips",
            json={"name": "Test Trip", "start_date": "2025-06-15", "end_date": "2025-06-20", "metadata": {}},
            headers={"Authorization": f"Bearer {self.token}"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("Test Trip", response.get_json()["trip"]["name"])
    
    def test_get_trips(self):
        TripFactory.create_batch(3)
        response = self.client.get("/api/v1/trips?page=1&per_page=2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()["trips"]), 2)

if __name__ == "__main__":
    unittest.main()