from . import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    pass

@app.route('/login')
def login():
    return("Login Page")

@app.route('/dashboard')
def dashboard():
    return("Dashboard")

