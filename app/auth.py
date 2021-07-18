from flask import Blueprint, request, render_template, url_for
import app.db.db_functions as db
from app.utils import safe

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == "POST":
        email = request.form['email']
        pwd = request.form['password']
        cpwd = request.form['confirm_password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        middle_name = request.form['middle_name']
        occupation = request.form['occupation']
        phone = request.form['phone']

        if not email:
            return dict(success=False, message="Email is required")
        if not safe.is_valid_email(email):
            return dict(success=False, message="Invalid Email address")
        if len(pwd) < 6:
            return dict(success=False, message="Password is too short")
        if not first_name:
            return dict(success=False, message="First name is required")
        if not last_name:
            return dict(success=False, message="Last name is required")
        if pwd != cpwd:
            return dict(success=False, message="Password mismatch")
        
        conn = db.get_db()
        cur = conn.cursor()
        if db.get_user_by_email(email, cur) is not None:
            return dict(success=False, message="Email is already registered")
        
        db.register_user(dict(email=email,password=pwd,
                first_name=first_name,last_name=last_name,middle_name=middle_name,
                phone=phone,occupation=occupation),
                cur)
        conn.commit()

        return dict(success=True, redirect=url_for('auth.login'), message="Registered successful")
    else:
        return render_template('auth/register.html')

@bp.route('/login')
def login():
    return "login page"

