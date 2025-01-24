from flask import Flask, render_template, request, redirect, url_for
import pymysql
from utils.calculator import calculate_carbon_footprint

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database configuration
db = pymysql.connect(
    host='localhost',
    user='root',
    password='1980',
    database='carbon_tracker'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    electricity = float(request.form['electricity'])
    gas = float(request.form['gas'])
    water = float(request.form['water'])

    carbon_footprint = calculate_carbon_footprint(electricity, gas, water)

    # Save to database
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO consumption (electricity, gas, water, carbon_footprint) VALUES (%s, %s, %s, %s)",
        (electricity, gas, water, carbon_footprint)
    )
    db.commit()

    return render_template('dashboard.html', carbon_footprint=carbon_footprint)

@app.route('/dashboard')
def dashboard():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM consumption")
    data = cursor.fetchall()
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
