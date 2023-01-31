from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models.user import User
from .models.properties import Property
from .models.transactions import Transactions
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


clientview = Blueprint('clientview', __name__)

@clientview.route('/', methods=['GET', 'POST'])
@login_required
def clientIndex():
    properties = Property.query.all()
    print(properties)
    return render_template("clientActiveAuctions.html", properties=properties)





@clientview.route('/bought_properties',methods=['GET'])
@login_required
def boughtProperties():
    properties = Property.query.filter_by(broughtBy=current_user.id).all()    
    return render_template('clientBoughtProperties.html', properties=properties)


# @clientview.route('/buy_property',methods=['POST'])
# @login_required
# def buyProperty():
#     if(request.method == 'POST'):
#         clientid = request.form['clientid']
#         propertyid = request.form['propertyid']
#         price = request.form['price']

#         new_transaction = Transaction(clientid=clientid, propertyid=propertyid,price=price)

#         db.session.add(new_transaction)
#         db.session.commit()  