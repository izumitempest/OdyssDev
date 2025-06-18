import pytest
from ...app import create_app
from app.extensions import db
from tests.factories import UserFactory, TripFactory
from flask_jwt_extended import create_access_token

class TripsTestCase:
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            self.user = UserFactory.create()
            db.session.commit()
            self.token = create_access_token(identity=str(self.user.id))

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_trip(self):
        data = {
            "name": "Test Trip",
            "start_date": "2025-06-15",
            "end_date": "2025-06-20",
            "trip_metadata": {}
        }
        response = self.client.post(
            "/api/v1/trips",
            json=data,
            headers={"Authorization": f"Bearer {self.token}"}
        )
        assert response.status_code == 201
        json_data = response.get_json()
        assert json_data["message"] == "Trip created"
        assert json_data["trip"]["name"] == "Test Trip"

    def test_get_trips(self):
        TripFactory.create(creator=self.user)
        db.session.commit()
        response = self.client.get(
            "/api/v1/trips",
            headers={"Authorization": f"Bearer {self.token}"}
        )
        assert response.status_code == 200
        json_data = response.get_json()
        assert len(json_data["trips"]) == 1