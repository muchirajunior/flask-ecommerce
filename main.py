# type: ignore 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app=Flask(__name__)

DB_URI=os.getenv("DB_URI")


app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+str(DB_URI)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']=os.getenv("SECRET_KEY")
app.config['UPLOAD_FOLDER']=os.getenv("UPLOAD_FOLDER")


db=SQLAlchemy(app)
CORS(app)

