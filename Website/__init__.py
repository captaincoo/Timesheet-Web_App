# from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from Website.models import db, Timesheet

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timesheet.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # db.init_app(app)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = "timesheet.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'awdsfdvcefdvcvx12343'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Timesheet
    create_database(app)
    return app


def create_database(app):
      if not path.exists('Website/'+DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
