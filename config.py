import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL is not set")
    
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Suppress SQLAlchemy warning

    @staticmethod
    def init_app(app):
        Config.init_app(app)

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

environment = os.environ.get("FLASK_ENV") or "development"
if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()