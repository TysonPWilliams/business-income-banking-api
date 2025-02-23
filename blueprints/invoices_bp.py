from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from init import db, ma
from models.invoice import Invoice, many_invoices, one_invoice, invoice_without_id

invoices_bp = Blueprint('invoices', __name__)

# Read all - GET /invoices
@invoices_bp.route('/invoices')
def get_invoices():
    stmt = db.Select(Invoice)
    invoices = db.session.scalars(stmt)
    return many_invoices.dump(invoices)

# Read one - GET /invoices/<int:invoice_id>

# Create one - POST /invoices
@invoices_bp.route('/invoices', methods=['POST'])
def create_invoice():
    # Parse the incoming JSON body
    try:
        data = invoice_without_id.load(request.json)

        new_invoice = Invoice(
            amount = data.get('amount'),
            date = data.get('date'),
            created_at = data.get('created_at')
        )

        db.session.add(new_invoice)
        db.session.commit()
        return one_invoice.dump(new_invoice), 201
    
    except IntegrityError as err:
        db.session.rollback()  # Rollback the transaction to prevent corruption
        error_message = str(err.orig)  # Extract the original error message
        return {f"Error": f"{error_message}"}
    
# Delete one - DELETE /invoices/<int:invoice_id>
# Update one - PUT/PATCH /invoices/<int:invoice_id>