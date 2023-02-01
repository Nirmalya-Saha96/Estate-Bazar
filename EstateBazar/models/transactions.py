from EstateBazar import db

class Transactions(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    clientId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    propertyId = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)
    price = db.Column(db.Integer)
    paymentMode = db.Column(db.String(150),default='Cash')
