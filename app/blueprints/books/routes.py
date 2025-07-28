from app.blueprints.books.schemas import book_schema,books_schema #login_schema
from app.models import Book,db
from flask import request,jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from . import books_bp

#====================Routes================
#===========#CREATE A book ROUTE===================
@books_bp.route("/books", methods=['POST']) #This a listener: As soon as it hears, this request, it fires the following function
def create_book():
  try:
    book_data = book_schema.load(request.json)

  except ValidationError as e:
    return jsonify(e.messages),400
  
  query = select(Book).where(Book.title==book_data['title'])

  existing_book=db.session.execute(query).scalars().all()
  if existing_book:
    return jsonify({"Error":"Title already associated with account"}),400

  new_book = Book(**book_data)
  db.session.add(new_book)
  db.session.commit()
  return book_schema.jsonify(new_book),201

#=======GET ALL bookS===============================
# @books_bp.route("/books", methods=['GET'])
# def get_books():
#   query = select(Book)
#   books = db.session.execute(query).scalars().all()
#   return jsonify(books_schema.dump(books)),200

#=====get all books with pagination

@books_bp.route("/books",methods=["GET"])
def get_books():
  try:
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    query = select(Book)
    books = db.paginate(query, page = page, per_page = per_page)
    return books_schema.jsonify(books),200
  except:
    query = select(Book)
    books = db.session.execute(query).scalars().all()
    return books_schema.jsonify(books),200
  




#==============RETRIEVE SPECIFIC book====================

@books_bp.route("/books/<int:book_id>", methods=['GET'])

def get_book(book_id):
  book = db.session.get(Book,book_id)

  if book:
    return book_schema.jsonify(book),200
  return jsonify({"Error": "book not found"})


#================UPDATE A book========================

@books_bp.route("/books/<int:book_id>", methods=['PUT'])
# @token_required
def update_book(book_id):
  book = db.session.get(Book,book_id)

  if not book:
    return jsonify({"Error":"book not found"})
  
  try:
    book_data = book_schema.load(request.json)

  except ValidationError as e:
    return jsonify(e.messages),400
  
  for key,value in book_data.items():
    setattr(book,key,value)

  db.session.commit()
  return book_schema.jsonify(book),200

#=============DELETE A book==========================
@books_bp.route("/books/<int:book_id>", methods=['DELETE'])
# @token_required

def delete_book(book_id):
  book = db.session.get(Book,book_id)

  if not book:
    return jsonify({"Error":"book not found"})
  
  db.session.delete(book)
  db.session.commit()

  return jsonify({"Message":f"book_id:{book_id}, successfully deleted"})

# ====Printing a popular book =======

@books_bp.route("/books/popular",methods =["GET"])
def popular_books():
  query = select(Book)
  books=db.session.execute(query).scalars().all()
  print(books)
  
  books.sort(key=lambda book:len(book.loans),reverse=True)

  return books_schema.jsonify(books)

@books_bp.route("/books/search",methods=["GET"])
def search_book():
  title = request.args.get("title")

  query = select(Book).where(Book.title.like(f"%{title}%"))

  book = db.session.execute(query).scalars().all()

  return books_schema.jsonify(book),200

#Postman search key:http://127.0.0.1:5000/books/search?title=all


