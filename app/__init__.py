from flask import Flask
from datetime import timedelta

from . import config
# from extensions import db
# from models import User, Champion
from .blueprints.base import base_bp

def create_app(config_class=config.DevelopmentConfig):
    """
    Flask Application Factory.
    Creates and configures the Flask application instance

    Args:
        config_class: The configuration class (from config.py) to use (Default: DevelopmentConfig).

    Returns:
        A configured Flask application instance.
    """
    app = Flask(__name__)

    # Load configuration from config class
    app.config.from_object(config_class)

    # Register base blueprint
    app.register_blueprint(base_bp)

    # Session lifetime of 1 week (7 days)
    app.permanent_session_lifetime = timedelta(days=7)

    # Uncomment once I have everything regarded database figured out, i.e. tables, columns, format, etc.
    # # Initialize db
    # db.init_app(app)

    # # Create database
    # with app.app_context():
    #     db.create_all()
    
    return app


