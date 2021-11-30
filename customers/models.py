from main import db

class Customer(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    username=db.Column(db.String,unique=True)
    password=db.Column(db.String,nullable=False)
    orders=""

    def __init__(self,name, username,password):
        self.name=name
        self.username=username
        self.password=password

class Order(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.String)
    location=db.Column(db.String)
    total=db.Column(db.Float)
    customer=""
    products=''

    def __init__(self,date,location,total,customer):
        self.date=date
        self.location=location
        self.total=total
        self.customer=customer