import factory
from models.user import User
from models.trip import Trip
from app.extensions import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session
    email = factory.Faker("email")
    password_hash = factory.LazyAttribute(lambda x: generate_password_hash("password"))

class TripFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Trip
        sqlalchemy_session = db.session
    name = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("text")
    metadata = factory.Dict({})
    start_date = factory.LazyFunction(lambda: datetime.now().date())
    end_date = factory.LazyFunction(lambda: (datetime.now() + timedelta(days=7)).date())
    creator = factory.SubFactory(UserFactory)