# type: ignore 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app=Flask(__name__)

DB_URI=os.getenv("DB_URI")

app.config['SQLALCHEMY_DATABASE_URI']=DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
CORS(app)

