# type: ignore
from flask import render_template, redirect, url_for, session
from main import app, db
from admin import admin
from products.models import Product


app.register_blueprint(admin)

@app.route('/')
def index():
    products=Product.query.all()
    

    return render_template('index.html', products=products)

@app.route('/about')
def about():
    
    return render_template('about.html')



