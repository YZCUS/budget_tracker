from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Transaction
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([transaction.serialize() for transaction in transactions])

@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    description = data['description']
    amount = data['amount']
    # Convert string date to date object
    date_str = data['date']
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    type = data['type']
    transaction = Transaction(description=description, amount=amount, date=date_obj, type=type)
    db.session.add(transaction)
    db.session.commit()
    return jsonify(transaction.serialize()), 201

@app.route('/api/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if transaction:
        db.session.delete(transaction)
        db.session.commit()
        return jsonify({'message': 'Transaction deleted'}), 200
    else:
        return jsonify({'message': 'Transaction not found'}), 404



if __name__ == '__main__':
    app.run(debug=True)