from init import db, ma
from sqlalchemy import Date
from marshmallow import Schema
from datetime import datetime

class Invoice(db.Model):
    __tablename__ = 'invoices'

    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Float, nullable=False)
    date = db.Column(Date)
    created_at = db.Column(db.DateTime, default=datetime.timezone.utcnow)

    matches = db.relationship('Match', backref='invoice', lazy=True)

class InvoiceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'amount', 'date', 'created_at')

one_invoice = InvoiceSchema()
many_invoices = InvoiceSchema(many=True)
invoice_without_id = InvoiceSchema(exclude=['id'])