from flask import Flask, jsonify, render_template, request
from replit import web,db
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)


##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Author TABLE Configuration
class Author(db.Model):
    Author_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(250), unique=True, nullable=False)
    Phone_Number = db.Column(db.String(500), nullable=True)
    Birth_Date = db.Column(db.String(500), nullable=True)
    Death_Date = db.Column(db.String(250), nullable=True)
  
    def to_dict(self):
        return {column.name: getattr(self, column.Name) for column in self.__table__.columns}


##Book TABLE Configuration
class Book(db.Model):
    Book_Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(250), unique=True, nullable=False)
    Author_id = db.Column(db.String(500), nullable=False)
    Publisher = db.Column(db.String(500), nullable=True)
    categorya_Id = db.Column(db.String(250), nullable=False)
    Price=db.Column(db.String(500), nullable=False)
    Sold_Count=db.Column(db.String(500), nullable=True)
  
    def to_dict(self):
        return {column.name: getattr(self, column.Title) for column in self.__table__.columns}


@app.route("/")
def home():
    return 'hi'









web.run(app)


















