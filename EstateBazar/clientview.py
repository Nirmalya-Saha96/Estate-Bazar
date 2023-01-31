from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


clientview = Blueprint('clientview', __name__)

@clientview.route('/', methods=['GET', 'POST'])
@login_required
def clientIndex(request):
    