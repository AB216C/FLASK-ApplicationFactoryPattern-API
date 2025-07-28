from app.blueprints.members.schemas import member_schema,members_schema #login_schema
from app.models import Member,db
from flask import request,jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from . import members_bp
# from app.extentions import limiter,cache
# from app.utils.util import encode_token,token_required

#====================Routes================
# from flask import request
#==from marshmallow import ValidationError
#At this time, @members_bp.route will be transformed into @members_bp.route

#This code generate token after logging in using email and password
# @members_bp.route("/member/login", methods=['POST'])
# def login():
#     try:
#         credentials = login_schema.load(request.json)
#         email = credentials['email']
#         password = credentials['password']
#     except ValidationError as e:
#         return jsonify(e.messages), 400

#     query = select(Member).where(Member.email == email)
#     member = db.session.execute(query).scalars().first()  # fixed typo

#     if member and member.password == password:
#         token = encode_token(member.id)
#         response = {
#             "status": "success",
#             "message": "Login successful",
#             "token": token
#         }
#         return jsonify(response), 200
#     else:
#         return jsonify({"Error": "Invalid email or password"})
  
  #CREATE A MEMBER ROUTE

@members_bp.route("/members", methods=['POST']) #This a listener: As soon as it hears, this request, it fires the following function
def create_member():
  try:
    member_data = member_schema.load(request.json)

  except ValidationError as e:
    return jsonify(e.messages),400
  
  query = select(Member).where(Member.email==member_data['email'])

  existing_member=db.session.execute(query).scalars().all()
  if existing_member:
    return jsonify({"Error":"Email already associated with account"}),400

  new_member = Member(name=member_data["name"], email=member_data["email"], DOB=member_data["DOB"],password=member_data["password"])
  db.session.add(new_member)
  db.session.commit()
  return member_schema.jsonify(new_member),201

#GET SELECTING ALL MEMBERS -Limiter and Cache was added to this route
@members_bp.route("/members", methods=['GET'])
#@limiter.limit("5 per 30 seconds") #Limit the number of requests to 5 per 30 seconds
#@cache.cached(timeout=45) #Cache the response for 30 seconds
def get_members():
  query = select(Member)
  members = db.session.execute(query).scalars().all()
  return jsonify(members_schema.dump(members)),200

#RETRIEVE SPECIFIC MEMBER

@members_bp.route("/members/<int:member_id>", methods=['GET'])

def get_member(member_id):
  member = db.session.get(Member,member_id)

  if member:
    return member_schema.jsonify(member),200
  return jsonify({"Error": "Member not found"})


#UPDATE A MEMBER

@members_bp.route("/members/<int:member_id>", methods=['PUT'])
# @token_required
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
@members_bp.route("/members/<int:member_id>", methods=['DELETE'])
# @token_required

def delete_member(member_id):
  member = db.session.get(Member,member_id)

  if not member:
    return jsonify({"Error":"Member not found"})
  
  db.session.delete(member)
  db.session.commit()

  return jsonify({"Message":f"Member_id:{member_id}, successfully deleted"})

# members/<int:member_id was deleted from the route because token _required decorate will take care of that
# @token_required decorator will ensure that the member_id is passed to the function
# and the member_id is used to retrieve the member from the database
# if the member is not found, it will return the error message
#if the error is found, it will delete the member and return the success message
# This is a practice to ensure the only ahtenticated users can delete a member