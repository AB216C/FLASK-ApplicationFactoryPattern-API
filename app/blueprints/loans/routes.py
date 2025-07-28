
from app.blueprints.loans.schemas import loan_schema,loans_schema, return_loan_schema, edit_loan_schema
from app.models import Loan,Book, db
from flask import request,jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from . import loans_bp

  
#==================CREATE A loan ROUTE=====================

@loans_bp.route("/loans", methods=['POST']) #This a listener: As soon as it hears, this request, it fires the following function
def create_loan():
  try:
    loan_data = loan_schema.load(request.json)

  except ValidationError as e:
    return jsonify(e.messages),400

  new_loan = Loan(loan_date = loan_data["loan_date"], member_id = loan_data["member_id"])

  for book_id in loan_data.get("book_ids"):
    query = select(Book).where(Book.id==book_id)
    book = db.session.execute(query).scalar()
    if book:
      new_loan.books.append(book)
    else:
      return jsonify({"Messages":"Invalid book Id"}),400

  db.session.add(new_loan)
  db.session.commit()
  return loan_schema.jsonify(new_loan),201

#==============GET SELECTING ALL loanS -Limiter and Cache was added to this route======
@loans_bp.route("/loans", methods=['GET'])
def get_loans():
  query = select(Loan)
  loans = db.session.execute(query).scalars().all()
  return jsonify(loans_schema.dump(loans)),200

#===================RETRIEVE SPECIFIC loan=====================

@loans_bp.route("/loans/<int:loan_id>", methods=['GET'])

def get_loan(loan_id):
  loan = db.session.get(Loan,loan_id)

  if loan:
    return loan_schema.jsonify(loan),200
  return jsonify({"Error": "loan not found"})


#==========================DELETE A loan========================
@loans_bp.route("/loans/<int:loan_id>", methods=['DELETE'])
def delete_loan(loan_id):
  loan = db.session.get(Loan,loan_id)

  if not loan:
    return jsonify({"Error":"loan not found"})
  
  db.session.delete(loan)
  db.session.commit()

  return jsonify({"Message":f"loan_id:{loan_id}, successfully deleted"}),200


#===========Edit a loan ===============================

@loans_bp.route("/loans/<int:loan_id>",methods=["PUT"])
def edit_loan(loan_id):
  try:
    loan_edits = edit_loan_schema.load(request.json)
  except ValidationError as e:
    return jsonify(e.messages),400
  
  query = select(Loan).where(Loan.id ==loan_id)
  loan =db.session.execute(query).scalar()

  for book_id in loan_edits["add_book_ids"]:
    query = select(Book).where(Book.id==book_id)
    book = db.session.execute(query).scalar()

    if book and book not in loan.books:
      loan.books.append(book)
  
  for book_id in loan_edits["remove_book_ids"]:
    query = select(Book).where(Book.id==book_id)
    book = db.session.execute(query).scalar()

    if book and book in loan.books:
      loan.books.remove(book)
  db.session.commit()
  return return_loan_schema.jsonify(loan),200