from flask import Blueprint, url_for, render_template

bp = Blueprint('main', __name__)

@bp.route('/home')
def home():
    return render_template('main/home.html')

@bp.route('/latest')
def latest():
    return render_template('main/home.html', active='latest')

@bp.route('/chats')
def chats():
    return render_template('main/home.html', active='chats')

@bp.route('/forums')
def forums():
    return render_template('main/home.html', active='forums')
    