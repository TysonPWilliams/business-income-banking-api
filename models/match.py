from init import db, ma
from flask_marshmallow import Schema
from datetime import datetime

class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)

    invoice_id = db.Column(db.Integer, db.ForeignKey("invoices.id", ondelete='cascade'), nullable=False)
    transaction_id = db.Column(db.Integer, db.ForeignKey("transaction.id", ondelete='cascade'), nullable=False)
    matched_at = db.Column(db.DateTime, default=datetime.timezone.utcnow)

    invoice = db.relationship('Invoice', back_populates='matches')
    transaction = db.relationship('Relationship', back_populates='matches')

class MatchSchema(ma.Schema):
    class Meta:
        fields = ('id', 'invoice_id', 'transaction_id', )

one_match = MatchSchema()
many_matches = MatchSchema(many=True)