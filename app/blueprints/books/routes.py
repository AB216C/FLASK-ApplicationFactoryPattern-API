from app.blueprints.books.schemas import book_schema,books_schema #login_schema
from app.models import Book,db
from flask import request,jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from . import books_bp

#====================Routes================
#CREATE A book ROUTE
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

#GET SELECTING ALL bookS -Limiter and Cache was added to this route
@books_bp.route("/books", methods=['GET'])
def get_books():
  query = select(Book)
  books = db.session.execute(query).scalars().all()
  return jsonify(books_schema.dump(books)),200

#RETRIEVE SPECIFIC book

@books_bp.route("/books/<int:book_id>", methods=['GET'])

def get_book(book_id):
  book = db.session.get(Book,book_id)

  if book:
    return book_schema.jsonify(book),200
  return jsonify({"Error": "book not found"})


#UPDATE A book

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

#DELETE A book
@books_bp.route("/books/<int:book_id>", methods=['DELETE'])
# @token_required

def delete_book(book_id):
  book = db.session.get(Book,book_id)

  if not book:
    return jsonify({"Error":"book not found"})
  
  db.session.delete(book)
  db.session.commit()

  return jsonify({"Message":f"book_id:{book_id}, successfully deleted"})

