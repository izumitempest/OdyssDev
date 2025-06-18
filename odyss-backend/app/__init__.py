from flask import Flask
from app.extensions import db
from core.database import init_db
from .config import config
from api.v1.routes import auth_bp
from api.v1.routes import trips_bp
# Import models to ensure tables are registered
from models.user import User
from models.role import Role
from models.trip import Trip

def create_app(config_name=None):
    if config_name is None:
        config_name = "development"
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    
    # Initialize database tables
    with app.app_context():
        init_db(app)
    
    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    app.register_blueprint(trips_bp, url_prefix="/api/v1/trips")
    
    return app