from EstateBazar import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class AdminUser(db.Model, UserMixin):
    __tablename__ = 'adminuser'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150))
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    properties = db.relationship('Property',backref='adminuser')
