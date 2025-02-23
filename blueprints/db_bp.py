from flask import Blueprint
from init import db
from models.invoice import Invoice
from datetime import datetime

db_bp = Blueprint('db', __name__)

@db_bp.cli.command('init')
def create_tables():
    db.drop_all()
    db.create_all()
    print("Tables Created")

@db_bp.cli.command('seed')
def seed_tables():
    invoices = [
        Invoice(
            amount = 25.99,
            date = "2025-02-23",
            created_at = datetime.utcnow()
        )
    ]

    db.session.add_all(invoices)
    db.session.commit()
    print("Tables seeded")

    