from app import app
from flask import render_template, redirect

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title="One-Study", name="Nikolay")

@app.route('/login')
def login():
    return render_template('login.html', title="Login")