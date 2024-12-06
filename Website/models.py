# Database model for Timesheet

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class Timesheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    manager_name = db.Column(db.String(100), nullable=False)
    project = db.Column(db.String(100), nullable=False)
    month = db.Column(db.String(20), nullable=False)
    dates = db.Column(db.String(20), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    hours_worked = db.Column(db.String(500), nullable=False)
    duties_performed = db.Column(db.String(1000), nullable=False)