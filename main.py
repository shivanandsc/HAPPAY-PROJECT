from flask import Flask, jsonify, render_template, request
from replit import web,db
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

global Api_key
Api_key='bdy6etf4yegf3cf3' 
##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Author(db.Model):
    Author_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(250), unique=True, nullable=False)
    Phone_Number = db.Column(db.String(500), nullable=True)
    Birth_Date = db.Column(db.String(500), nullable=True)
    Death_Date = db.Column(db.String(250), nullable=True)
  
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return 'hi'

@app.route("/home")
def new():
    return 'home'








web.run(app)


















