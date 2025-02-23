from flask import Flask
from init import db, ma
import os
from blueprints.db_bp import db_bp
from config import *
from blueprints.invoices_bp import invoices_bp


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(db_bp)
    app.register_blueprint(invoices_bp)

    return app