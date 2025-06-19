from flask import Flask
from flask_jwt_extended import JWTManager
from app.extensions import db
from core.database import init_db
from .config import config
from api.v1.routes import api_v1_bp
from models.user import User
from models.role import Role
from models.trip import Trip

def create_app(config_name=None):
    if config_name is None:
        config_name = "production"
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    jwt = JWTManager(app)
    
    # Initialize database tables
    with app.app_context():
        init_db(app)
    
    # Register blueprints
    app.register_blueprint(api_v1_bp, url_prefix="/api/v1")
    
    # Health check endpoint
    @app.route('/api/v1/auth/ping')
    def ping():
        return {"status": "ok"}, 200
    
    return app