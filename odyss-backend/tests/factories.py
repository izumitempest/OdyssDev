import factory
from factory.faker import Faker
from app.extensions import db
from models.user import User
from models.role import Role
from models.trip import Trip
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

class RoleFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta(factory.alchemy.SQLAlchemyModelFactory.Meta):
        model = Role
        sqlalchemy_session = db.session
    id = Faker("uuid4")
    name = Faker("word")
    name = factory.Faker("word")

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta(factory.alchemy.SQLAlchemyModelFactory.Meta):
        model = User
        sqlalchemy_session = db.session
    id = Faker("uuid4")
    email = Faker("email")
    password_hash = factory.LazyAttribute(lambda x: generate_password_hash("password"))
    role_id = factory.LazyAttribute(lambda x: RoleFactory.create().id)
    role_id = factory.LazyAttribute(lambda x: RoleFactory.create().id)

class TripFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta(factory.alchemy.SQLAlchemyModelFactory.Meta):
        model = Trip
        sqlalchemy_session = db.session
    id = Faker("uuid4")
    name = Faker("sentence", nb_words=4)
    description = Faker("text")
    trip_metadata = {}
    start_date = Faker("date_this_year")
    end_date = factory.LazyAttribute(lambda x: x.start_date + timedelta(days=7))
    creator = factory.SubFactory(UserFactory): x.start_date + timedelta(days=7))
    creator = factory.SubFactory(UserFactory)