import os
import pathlib

def create_file_tree():
    # Define the corrected file tree with app/ and other folders at root level
    file_tree = {
        "odyss-backend": {
            "app": {
                "__init__.py": "pass",
                "config.py": "pass",
                "extensions.py": "pass"
            },
            "core": {
                "__init__.py": "pass",
                "database.py": "pass",
                "dependencies.py": "pass",
                "exceptions.py": "pass",
                "constants.py": "pass",
                "postgres_utils.py": "pass"
            },
            "models": {
                "__init__.py": "pass",
                "base.py": "pass",
                "user.py": "pass",
                "trip.py": "pass",
                "booking.py": "pass",
                "payment.py": "pass",
                "role.py": "pass",
                "permission.py": "pass"
            },
            "auth": {
                "__init__.py": "pass",
                "models.py": "pass",
                "routes.py": "pass",
                "services.py": "pass",
                "guards.py": "pass",
                "rbac.py": "pass",
                "utils.py": "pass"
            },
            "trips": {
                "__init__.py": "pass",
                "routes.py": "pass",
                "services.py": "pass",
                "repositories.py": "pass",
                "schemas.py": "pass",
                "utils.py": "pass"
            },
            "bookings": {
                "__init__.py": "pass",
                "routes.py": "pass",
                "services.py": "pass",
                "repositories.py": "pass",
                "schemas.py": "pass",
                "utils.py": "pass"
            },
            "payments": {
                "__init__.py": "pass",
                "routes.py": "pass",
                "services.py": "pass",
                "repositories.py": "pass",
                "schemas.py": "pass",
                "processors": {
                    "__init__.py": "pass",
                    "base.py": "pass",
                    "stripe.py": "pass",
                    "paypal.py": "pass"
                },
                "utils.py": "pass"
            },
            "users": {
                "__init__.py": "pass",
                "routes.py": "pass",
                "services.py": "pass",
                "repositories.py": "pass",
                "schemas.py": "pass",
                "utils.py": "pass"
            },
            "admin": {
                "__init__.py": "pass",
                "routes.py": "pass",
                "services.py": "pass",
                "repositories.py": "pass",
                "schemas.py": "pass",
                "dashboard.py": "pass"
            },
            "search": {
                "__init__.py": "pass",
                "routes.py": "pass",
                "services.py": "pass",
                "filters.py": "pass",
                "utils.py": "pass"
            },
            "notifications": {
                "__init__.py": "pass",
                "routes.py": "pass",
                "services.py": "pass",
                "providers": {
                    "__init__.py": "pass",
                    "email.py": "pass",
                    "sms.py": "pass",
                    "push.py": "pass"
                },
                "templates": {
                    "email": {},
                    "sms": {}
                }
            },
            "common": {
                "__init__.py": "pass",
                "decorators.py": "pass",
                "validators.py": "pass",
                "serializers.py": "pass",
                "pagination.py": "pass",
                "errors.py": "pass",
                "helpers.py": "pass"
            },
            "api": {
                "__init__.py": "pass",
                "v1": {
                    "__init__.py": "pass",
                    "routes.py": "pass"
                },
                "middleware.py": "pass"
            },
            "migrations": {
                "alembic.ini": "[alembic]\nscript_location = migrations\n",
                "env.py": "pass",
                "script.py.mako": "# Migration template\n",
                "versions": {}
            },
            "tests": {
                "__init__.py": "pass",
                "conftest.py": "pass",
                "factories.py": "pass",
                "unit": {
                    "test_auth.py": "pass",
                    "test_trips.py": "pass",
                    "test_bookings.py": "pass",
                    "test_payments.py": "pass"
                },
                "integration": {
                    "test_trip_booking_flow.py": "pass",
                    "test_payment_flow.py": "pass"
                },
                "fixtures": {}
            },
            "scripts": {
                "init_db.py": "pass",
                "seed_data.py": "pass",
                "backup_db.py": "pass",
                "restore_db.py": "pass",
                "deploy.py": "pass"
            },
            "logs": {
                "app.log": "",
                "error.log": ""
            },
            "requirements": {
                "base.txt": "flask\nflask-sqlalchemy\nflask-jwt-extended\npsycopg2-binary\npython-dotenv\nmarshmallow\n",
                "development.txt": "",
                "production.txt": "",
                "testing.txt": "pytest\nfactory_boy\n"
            },
            ".env.example": "DATABASE_URL=postgresql://odyss_user:your_secure_password@localhost:5432/odyss_db\n"
                           "FLASK_ENV=development\n"
                           "SECRET_KEY=your_secret_key\n"
                           "JWT_SECRET_KEY=your_jwt_secret_key\n"
                           "SQLALCHEMY_POOL_SIZE=10\n"
                           "SQLALCHEMY_POOL_TIMEOUT=20\n"
                           "SQLALCHEMY_POOL_RECYCLE=3600\n"
                           "SQLALCHEMY_MAX_OVERFLOW=20\n",
            ".gitignore": "__pycache__/\n*.pyc\n.env\nlogs/\n*.log\nmigrations/versions/*\n",
            "README.md": "# Odyss Backend\nA Flask-based backend for the Odyss travel platform.\n",
            "Dockerfile": "# Placeholder Dockerfile\nFROM python:3.9\n",
            "docker-compose.yml": "# Placeholder docker-compose\nversion: '3.8'\nservices:\n  app:\n    build: .\n",
            "wsgi.py": "from app import create_app\napp = create_app()\n",
            "run.py": "from app import create_app\nif __name__ == '__main__':\n    app = create_app()\n    app.run()\n"
        }
    }

    def create_structure(base_path, structure):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                # Create directory
                os.makedirs(path, exist_ok=True)
                print(f"Created directory: {path}")
                # Recursively create substructure
                create_structure(path, content)
            else:
                # Create file with specified content
                pathlib.Path(path).write_text(content)
                print(f"Created file: {path}")

    # Create the file tree
    create_structure(".", file_tree)

if __name__ == "__main__":
    print("Generating Odyss backend file tree...")
    create_file_tree()
    print("File tree generation complete!")
