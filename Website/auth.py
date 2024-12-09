from flask import Blueprint, render_template, request, redirect, url_for
from .models import Timesheet
from . import db
auth = Blueprint('auth', __name__)

@auth.route('/spurcroftinc/timesheet', methods = ['GET', 'POST'])
def home():
    data = request.form
    print(data)

    if request.method == 'POST':
        name = request.form.get('name')
        title = request.form.get('title')
        email = request.form.get('email')
        phone = request.form.get('phone')
        manager_name = request.form.get('manager_name')
        project = request.form.get('project')
        month = request.form.get('month')
        dates = request.form.get('dates')
        year = request.form.get('year')
        duties_performed = request.form.getlist('duties_performed[]')  # Get all duties
        hours_worked = request.form.getlist('hours_worked[]')          # Get all hours worked
        
        # Flatten and handle empty hours_worked
        flattened_hours = [float(h or 0) for h in hours_worked]  # Replace None/empty with 0
        flattened_duties = [d or '' for d in duties_performed]   # Replace None/empty with ''

        print(flattened_hours)
        print(flattened_duties)

        # Aggregate or process as needed (example: sum total hours)
        total_hours = sum(flattened_hours)

        # Save to the database
        new_user = Timesheet(
            name=name,
            title=title,
            email=email,
            phone=phone,
            manager_name=manager_name,
            project=project,
            month=month,
            dates=dates,
            year=year,
            hours_worked=", ".join(flattened_hours),  # Save aggregated value
            duties_performed=", ".join(flattened_duties)  # Join all duties if required
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('views.home'))
    return render_template("home.html")


@auth.route('/Login')
def login():
    return '<p>Test</p>'

@auth.route('/Logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/SignUp')
def signup():
    return '<p>SignUP</p>'