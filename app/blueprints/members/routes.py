from app.blueprints.members.schemas import member_schema,members_schema
from app.models import Member,db
from flask import request,jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from . import members_bp


#====================Routes================
# from flask import request
#==from marshmallow import ValidationError
#At this time, @members_bp.route will be transformed into @members_bp.route

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

  new_member = Member(**member_data)
  db.session.add(new_member)
  db.session.commit()
  return member_schema.jsonify(new_member),201

#GET SELECTING ALL MEMBERS
@members_bp.route("/members", methods=['GET'])
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

def delete_member(member_id):
  member = db.session.get(Member,member_id)

  if not member:
    return jsonify({"Error":"Member not found"})
  
  db.session.delete(member)
  db.session.commit()

  return jsonify({"Message":f"Member_id:{member_id}, successfully deleted"})
