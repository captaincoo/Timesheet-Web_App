from Website import create_app, db
from Website.models import Timesheet
from os import path

# Initialize the Flask app
app = create_app()

# Path to the database file
db_path = 'Website/timesheet.db'

# Check if the database exists
if path.exists(db_path):
    with app.app_context():
        # Execute the query and fetch results
        result = db.session.execute("SELECT * FROM timesheet").fetchall()
        for row in result:
            print(row)
else:
    print(f"Database does not exist at {db_path}. Please ensure the database is created.")
