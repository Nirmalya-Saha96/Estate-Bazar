from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models.user import User
from .models.adminuser import AdminUser
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

adminview = Blueprint('adminview', __name__)

@adminview.route('/', methods=['GET', 'POST'])
@login_required
def index():
    print(current_user)
    return render_template("adminActiveListing.html", user=current_user)