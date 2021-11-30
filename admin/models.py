from main import db

class Admins(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(300))
    username=db.Column(db.String(50),unique=True)
    password=db.Column(db.String)

    def __init__(self,name,username,password):
        self.name=name
        self.username=username
        self.password=password