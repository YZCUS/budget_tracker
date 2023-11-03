from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String(20), nullable=False)  # 'income' or 'expense'
    def __repr__(self):
        return f"<Transaction {self.description}>"
    
    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'amount': self.amount,
            'date': self.date.isoformat(),
            'type': self.type
        }