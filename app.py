from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column
from datetime import date
from typing import List
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError
from sqlalchemy import select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Mahirane231995@localhost/Bank'

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class = Base)
ma = Marshmallow()

db.init_app(app)
ma.init_app(app)

class Member(Base):
  __tablename__ = 'members'

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(db.String(255), nullable=False)
  email: Mapped[str] = mapped_column(db.String(360), nullable=False, unique=True)
  DOB: Mapped[date]
  password: Mapped[str] = mapped_column(db.String(255), nullable=False)

  loans: Mapped[List['Loan']] = db.relationship(back_populates='member') 


loan_book = db.Table(
    'loan_book',
    Base.metadata,
    db.Column('loan_id', db.ForeignKey('loans.id')),
    db.Column('book_id', db.ForeignKey('books.id'))
)

class Loan(Base):
  __tablename__ = 'loans'

  id: Mapped[int] = mapped_column(primary_key=True)
  loan_date: Mapped[date] = mapped_column(db.Date)
  member_id: Mapped[int] = mapped_column(db.ForeignKey('members.id'))

  member: Mapped['Member'] = db.relationship(back_populates='loans')
  books: Mapped[List['Book']] = db.relationship(secondary=loan_book, back_populates='loans')

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(db.String(255), nullable=False)
    genre: Mapped[str] = mapped_column(db.String(255), nullable=False)
    desc: Mapped[str] = mapped_column(db.String(255), nullable=False)
    title: Mapped[str] = mapped_column(db.String(255), nullable=False)

    loans: Mapped[List['Loan']] = db.relationship(secondary=loan_book, back_populates='books')

    # CREATING SCHEMAS

#Member Schema

class MemberSchema(ma.SQLAlchemyAutoSchema): 
  class Meta:
    model = Member
  
member_schema = MemberSchema() #Allow serialization for a single user
members_schema = MemberSchema(many=True) #Allow serialization for many users

#====================Routes================
# from flask import request
#==from marshmallow import ValidationError

@app.route("/members", methods=['POST']) #This a listener: As soon as it hears, this request, it fires the following function
def create_member():
  try:
    member_data = member_schema.load(request.json)

  except ValidationError as e:
    return jsonify(e.messages),400
  
  query = select(Member).where(Member.email==member_data['email'])

  existing_member=db.session.execute(query).scalars().all()
  if existing_member:
    return jsonify({"Error":"Email already associated with account"}),400

  new_member = Member(**member_data)
  db.session.add(new_member)
  db.session.commit()
  return member_schema.jsonify(new_member),201

#GET SELECTING ALL MEMBERS
@app.route("/members", methods=['GET'])
def get_members():
  query = select(Member)
  members = db.session.execute(query).scalars().all()
  return jsonify(members_schema.dump(members)),200

#RETRIEVE SPECIFIC MEMBER

@app.route("/members/<int:member_id>", methods=['GET'])

def get_member(member_id):
  member = db.session.get(Member,member_id)

  if member:
    return member_schema.jsonify(member),200
  return jsonify({"Error": "Member not found"})


#UPDATE A MEMBER

@app.route("/members/<int:member_id>", methods=['PUT'])

def update_member(member_id):
  member = db.session.get(Member,member_id)

  if not member:
    return jsonify({"Error":"Member not found"})
  
  try:
    member_data = member_schema.load(request.json)

  except ValidationError as e:
    return jsonify(e.messages),400
  
  for key,value in member_data.items():
    setattr(member,key,value)

  db.session.commit()
  return member_schema.jsonify(member),200

#DELETE A MEMBER
@app.route("/members/<int:member_id>", methods=['DELETE'])

def delete_member(member_id):
  member = db.session.get(Member,member_id)

  if not member:
    return jsonify({"Error":"Member not found"})
  
  db.session.delete(member)
  db.session.commit()

  return jsonify({"Message":f"Member_id:{member_id}, successfully deleted"})


with app.app_context():
  db.create_all()

app.run(debug=True)













