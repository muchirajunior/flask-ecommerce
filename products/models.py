from main import db

class Product(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    price=db.Column(db.Float, nullable=False)
    cartegory=db.Column(db.String, nullable=False)
    description=db.Column(db.String, default='')
    image=db.Column(db.String, default='')

    def __init__(self,name,price,cartegory,description,image):
        self.name=name
        self.price=price
        self.description=description
        self.cartegory=cartegory
        self.image=image

class Cartegory(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)

    def __init__(self,name):
        self.name=name



class OrderProduct(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    productid=db.Column(db.Integer)
    orderid=db.Column(db.Integer)

        