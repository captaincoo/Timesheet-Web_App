from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/Login')
def login():
    return '<p>Test</p>'

@auth.route('/Logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/SignUp')
def signup():
    return '<p>SignUP</p>'