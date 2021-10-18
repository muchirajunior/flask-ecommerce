# type: ignore
from flask import render_template, redirect, url_for, session
from . import app, db

@app.route('/')
def index():

    return {"message":"success"}
