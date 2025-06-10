# -*- coding: utf-8 -*-
# Odyss Backend - Flask Application Initialization
from flask import Flask
from app.config import config
from app.extensions import init_extensions
from core.database import init_db
from api.v1.routes import api_v1_bp

def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    init_extensions(app)
    init_db(app)
    app.register_blueprint(api_v1_bp, url_prefix="/api/v1")
    return app