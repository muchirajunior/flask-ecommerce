# type: ignore
from flask import render_template, redirect, url_for, session
from main import app, db
from admin.routes import admin


app.register_blueprint(admin)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/about')
def about():
    
    return render_template('about.html')

@app.route('/page')
def method_name():
   
   return render_template('layout.html')


