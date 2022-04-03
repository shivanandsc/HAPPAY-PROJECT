from flask import Flask, jsonify, render_template, request
from replit import web,db
from flask_sqlalchemy import SQLAlchemy
import random
import datetime
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)


##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Author TABLE Configuration
class Author(db.Model):
    Author_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(250), unique=True, nullable=False)
    Phone_Number = db.Column(db.String(500),unique=False, nullable=True)
    Birth_Date = db.Column(db.String(500),unique=False, nullable=True)
    Death_Date = db.Column(db.String(250), unique=False,nullable=True)
  



##Book TABLE Configuration
class Book(db.Model):
    Book_Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(250), unique=True, nullable=False)
    Author_id = db.Column(db.String(500), nullable=False)
    Publisher = db.Column(db.String(500), nullable=False)
    category_Id = db.Column(db.String(250), nullable=False)
    Price=db.Column(db.String(500), nullable=False)
    Sold_Count=db.Column(db.String(500), nullable=False)

db.create_all()

@app.route("/")
def home():
    return 'Welcome to HAPPAY project'

@app.route("/addAnAuthor", methods=["POST","GET"])
def addAnAuthor(): 
      try:
        Birth_Date=request.args.get("birth_date")
        Death_date=request.args.get("death_date")     
        if Birth_Date!='null':      
          b_day, b_month, b_year = Birth_Date.split('-')
          if Death_date!='null':
            d_day, d_month, d_year = Death_date.split('-')
            try:
              datetime.datetime(int(d_year),int(d_month),int(d_day)) 
            except:
              return jsonify(response={"unsuccessfull": "Invalid death date "})
          try:
            datetime.datetime(int(b_year),int(b_month),int(b_day))       
          except:
              return jsonify(response={"unsuccessfull": "Invalid birth date "})  
        try:  
          new_author = Author(
              Name=request.args.get("name"),
              Phone_Number=request.args.get("phone_number"),
              Birth_Date=Birth_Date,
              Death_Date=Death_date,
              )
          db.session.add(new_author)
          db.session.commit()
          return jsonify(response={"success": "Successfully added the new author."})
        except:
          return jsonify(response={"unsuccessfull": "Author details are present "})

      except:
        return jsonify(response={"unsuccessfull": "invalid API URL"})


@app.route("/addBookToCatalog", methods=["POST","GET"])
def addBookToCatalog():
    title = request.args.get("title")
    print(title)
    books = db.session.query(Book).all()
    try:
      print('enter')
      new_book = Book(
        Title = title,
        Author_id = request.args.get("author"),
        Publisher = request.args.get("publisher"),
        category_Id = request.args.get("category"),
        Price=request.args.get("price"),
        Sold_Count=request.args.get("sold_count")
                  )      
      db.session.add(new_book)
      db.session.commit()
      return jsonify(response={"success": "Successfully added the new book."})
      
    except:
        return jsonify(response={"unsuccessfull": "invalid API URL"})



@app.route("/getListOfCategories", methods=["POST","GET"])
def getListOfCategories():
  all_categories=[]
  books = db.session.query(Book).all()
  for book in books:
    if book.category_Id != 'null':
      all_categories.append(book.category_Id)
  all_categories=list(dict.fromkeys(all_categories))
  return jsonify(response={"success": all_categories})


@app.route("/searchBookByAuthorName", methods=["POST","GET"])
def searchBookByAuthorName():
  author_books=[]
  Author_name= request.args.get("name")
  Book_details = db.session.query(Book).all()
  for book in Book_details:
    if Author_name==book.Author_id:
      author_books.append(book.Title)
  print(author_books)
  if len(author_books)!=0:
    return jsonify(response={"success": author_books})
  else :
    return jsonify(response={"success": "No book present"})


@app.route("/searchBook", methods=["POST","GET"])
def searchBook():
  searched_books=[]
  book_name= request.args.get("name")
  Book_details = db.session.query(Book).all()
  for book in Book_details:
    if book_name in book.Title:
      searched_books.append(book.Title)
  if len(searched_books)!=0:
    return jsonify(response={"success": searched_books})
  else:
    return jsonify(response={"success": "No book present"})
    
  
@app.route("/getMostSoldBookInCategory", methods=["POST","GET"])
def getMostSoldBookInCategory():
  sold_count=0
  mostsold_book=0
  category= request.args.get("category")
  Book_details = db.session.query(Book).all()
  for book in Book_details:
    if book.category_Id==category and int(book.Sold_Count)>int(sold_count):     
      sold_count=book.Sold_Count
      mostsold_book=book
  if len(Book_details)!=0:
    return jsonify(response={"success": (mostsold_book.Title+"  "+mostsold_book.Sold_Count)})
  else:   
    return jsonify(response={"unsuccess":'add books'})


@app.route("/getAllAuthorName", methods=["POST","GET"])
def getAllAuthorName():
  Author_details = db.session.query(Author).all()
  all_authors=[]
  for author in Author_details:
    all_authors.append(author.Name)
  return jsonify(response={"success":all_authors })











  
web.run(app)


















