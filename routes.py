# type: ignore
from flask import render_template, redirect, url_for, session
from main import app, db
from admin import admin
from products.models import Product
import os


app.register_blueprint(admin)

@app.route('/')
def index():
    products=Product.query.all()
    

    return render_template('index.html', products=products)

@app.route('/about')
def about():
    
    return render_template('about.html')

@app.route('/files')
def make_tree():
    path="/"
    tree = dict(name=os.path.basename(path), children=[])
    print(tree)
    try: lst = os.listdir(path)
    except Exception as e:
        print(e)
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree



