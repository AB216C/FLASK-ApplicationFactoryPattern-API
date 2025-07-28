from app.blueprints.items.schemas import item_schema,items_schema 
from app.models import Item,db
from flask import request,jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from . import items_bp

@items_bp.route("/items", methods=['POST']) #This a listener: As soon as it hears, this request, it fires the following function
def create_item():
  try:
    item_data = item_schema.load(request.json)

  except ValidationError as e:
    return jsonify(e.messages),400
  
  query = select(Item).where(Item.item_name==item_data['item_name'])

  existing_item=db.session.execute(query).scalars().all()
  if existing_item:
    return jsonify({"Error":"Email already associated with account"}),400

  new_item = Item(**item_data)
  db.session.add(new_item)
  db.session.commit()
  return item_schema.jsonify(new_item),201

#GET SELECTING ALL itemS -Limiter and Cache was added to this route
@items_bp.route("/items", methods=['GET'])

def get_items():
  query = select(Item)
  items = db.session.execute(query).scalars().all()
  return jsonify(items_schema.dump(items)),200

#RETRIEVE SPECIFIC item

@items_bp.route("/items/<int:item_id>", methods=['GET'])

def get_item(item_id):
  item = db.session.get(Item,item_id)

  if item:
    return item_schema.jsonify(item),200
  return jsonify({"Error": "item not found"})

#UPDATE A item

@items_bp.route("/items/<int:item_id>", methods=['PUT'])

def update_item(item_id):
  item = db.session.get(Item,item_id)

  if not item:
    return jsonify({"Error":"item not found"})
  
  try:
    item_data = item_schema.load(request.json)

  except ValidationError as e:
    return jsonify(e.messages),400
  
  for key,value in item_data.items():
    setattr(item,key,value)

  db.session.commit()
  return item_schema.jsonify(item),200

#DELETE A item
@items_bp.route("/items/<int:item_id>", methods=['DELETE'])

def delete_item(item_id):
  item = db.session.get(Item,item_id)

  if not item:
    return jsonify({"Error":"item not found"})
  
  db.session.delete(item)
  db.session.commit()

  return jsonify({"Message":f"item_id:{item_id}, successfully deleted"})
