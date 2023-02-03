from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models.user import User
from .models.properties import Property
from .models.transactions import Transactions
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

#ML
import numpy as np
from keras.models import load_model
model_loaded = load_model('model.h5')

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


@clientview.route('/details', methods=['GET'])
@login_required
def clientDetails():
    propertyId = request.args.get('propertyId')
    propertyObj = Property.query.get(propertyId)

    bedrooms = (propertyObj.bedroom)
    bathrooms = propertyObj.bathroom
    sqrt = propertyObj.sqft
    num = ""
    for c in bedrooms:
        if c.isdigit():
            num = num + c
    num2 = ""
    for c in bathrooms:
        if c.isdigit():
            num2 = num2 + c
    num3 = ""
    for c in sqrt:
        if c.isdigit():
            num3 = num3 + c
    hsqrt = int(num3)/2

    session['userId'] = current_user.id
    session['room'] = propertyId
    session['username'] = current_user.username
    session['propertyId'] = propertyId

    test_data = np.array([2014, 36, int(num), int(num2), hsqrt, int(num3)])
    prediction = str(model_loaded.predict(test_data.reshape(1,6), batch_size=1))

    return render_template('clientDetails.html', property=propertyObj, prediction=prediction, user=current_user) 