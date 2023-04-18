import pyodbc
from flask import Flask, render_template

# Connect to the Azure SQL database
conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'
                      'SERVER=tcp:finalprojectanalysis1.database.windows.net,1433;'
                      'DATABASE=redditanalysis;'
                      'UID=EDMGroup;'
                      'PWD=Projectanalysis3;'
                      'Encrypt=yes;'
                      'TrustServerCertificate=no;'
                      'Connection Timeout=30;')

# Create a cursor object
cursor = conn.cursor()

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page ('/') and a function that retrieves the data from the database and renders a template
@app.route('/')
def display_data():
    # Execute a SQL query
    cursor.execute('SELECT * FROM SentimentAnalysis')
    # Fetch all the rows from the query result
    rows = cursor.fetchall()
    # Render the template with the data
    return render_template('data.html', rows=rows)

# Run the Flask app
if __name__ == '__main__':
    app.run()
