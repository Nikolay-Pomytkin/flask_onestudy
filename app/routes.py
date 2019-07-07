from app import app
from flask import render_template, redirect

@app.route('/index')
@app.route('/')
def index():
    user = {'username': 'Nikolay'}
    return render_template('index.html', title="One-Study", user=user)

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title="Login")