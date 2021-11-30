# type: ignore
from flask import Blueprint,render_template,request,redirect
from products import *
from customers import *
from .models import Admins,db

admin=Blueprint('admin',__name__,url_prefix='/admin', static_folder='./static', template_folder='admin/templates' )

@admin.route('/', methods=['GET','POST'])
def adminLogin():
    
    return render_template('admin_login.html', page="admin login")


@admin.route('/addproduct', methods=['GET','POST'])
def addproduct():
    if request.method=="POST":
        name=request.form['name']
        price=request.form['price']
        description=request.form['description']
        image=request.files['image']
        imagename=uploadFile(image)  
        newProduct=Product(name,price,'sales',description, imagename)

        db.session.add(newProduct)
        db.session.commit() 

        return redirect('/admin/addproduct')
    
    return render_template('addproduct.html', page="add product")