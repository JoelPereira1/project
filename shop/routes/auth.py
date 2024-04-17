from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from shop.models.user import User
from shop.extensions import db

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        name = request.form['name']

        user = User(email=email, password=password, name=name)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful. You can now log in.')
        return redirect(url_for('auth.login'))

    return render_template('register.html')