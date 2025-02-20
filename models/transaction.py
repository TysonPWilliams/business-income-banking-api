from flask_marshmallow import Schema
from init import db, ma
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Numeric(10, 2), nullable=False)
    date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.timezone.utcnow)

    matches = db.relationship('Match', backref='transaction', lazy=True)

class TransactionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'amount', 'date', 'created_at')

one_transaction = TransactionSchema()
many_transactions = TransactionSchema(many=True)