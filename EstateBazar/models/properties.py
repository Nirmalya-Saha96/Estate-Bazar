from EstateBazar import db
from sqlalchemy.sql import func

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    soldPrice = db.Column(db.Integer, default = 0)
    bedroom = db.Column(db.Integer)
    bathroom = db.Column(db.Integer)
    sqft = db.Column(db.Integer)
    isSold = db.Column(db.Boolean,default = False)
    isActive = db.Column(db.Boolean,default = False)
    broughtBy = db.Column(db.Integer,db.ForeignKey('users.id'))
    soldBy = db.Column(db.Integer,db.ForeignKey('adminuser.id'))
    address = db.Column(db.String(250))
    imgSrc = db.Column(db.String(250))
    transaction = db.relationship('Transactions', backref='properties')
