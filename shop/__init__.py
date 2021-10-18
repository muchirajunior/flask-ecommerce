# type: ignore 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)

DB_URI=os.getenv("DB_URI")

app.config['SQLALCHEMY_DATABASE_URI']=DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

print(DB_URI)

db=SQLAlchemy(app)


from .routes import app