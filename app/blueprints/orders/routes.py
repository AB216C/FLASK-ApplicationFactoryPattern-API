from app.blueprints.orders.schemas import order_schema,orders_schema,create_order_schema,receipt_schema
from app.models import Order,OrderItems, db
from flask import request,jsonify
from marshmallow import ValidationError
from sqlalchemy import select
from . import orders_bp



#====================Routes=================

#==========#CREATE A ORDER ROUTE===============

@orders_bp.route("/orders",methods=["POST"])
def create_order():
  try:
    order_data = create_order_schema.load(request.json)
    print(order_data)
  except ValidationError as e:
    return jsonify(e.messages),400
  
  new_order = Order(member_id=order_data['member_id'], order_date=order_data['order_date'])
  db.session.add(new_order)
  db.session.commit()

  for item in order_data['item_quant']:
    order_item = OrderItems(order_id = new_order.id, item_id = item['item_id'], quantity=item['item_quant'])
    db.session.add(order_item)
  
  db.session.commit()

  total = 0

  for order_item in new_order.order_items:
    price = order_item.quantity * order_item.item.price
    total +=price

    receipt = {
      "total": total,
      "order": new_order
    }
    
  return receipt_schema.jsonify(receipt),201



# @orders_bp.route("/orders", methods=['POST']) #This a listener: As soon as it hears, this request, it fires the following function
# def create_order():
#   try:
#     order_data = order_schema.load(request.json)

#   except ValidationError as e:
#     return jsonify(e.messages),400
  
#   query = select(Order).where(Order.order_date==order_data['order_date'])

#   existing_order=db.session.execute(query).scalars().all()
#   if existing_order:
#     return jsonify({"Error":"Order date already associated with account"}),400

#   new_order = Order(**order_data)
#   db.session.add(new_order)
#   db.session.commit()
#   return order_schema.jsonify(new_order),201

# #GET SELECTING ALL orderS -Limiter and Cache was added to this route
# @orders_bp.route("/orders", methods=['GET'])

# def get_orders():
#   query = select(Order)
#   orders = db.session.execute(query).scalars().all()
#   return jsonify(orders_schema.dump(orders)),200

# #RETRIEVE SPECIFIC order

# @orders_bp.route("/orders/<int:order_id>", methods=['GET'])

# def get_order(order_id):
#   order = db.session.get(Order,order_id)

#   if order:
#     return order_schema.jsonify(order),200
#   return jsonify({"Error": "order not found"})

# #UPDATE A order

# @orders_bp.route("/orders/<int:order_id>", methods=['PUT'])

# def update_order(order_id):
#   order = db.session.get(Order,order_id)

#   if not order:
#     return jsonify({"Error":"order not found"})
  
#   try:
#     order_data = order_schema.load(request.json)

#   except ValidationError as e:
#     return jsonify(e.messages),400
  
#   for key,value in order_data.orders():
#     setattr(order,key,value)

#   db.session.commit()
#   return order_schema.jsonify(order),200

# #DELETE A order
# @orders_bp.route("/orders/<int:order_id>", methods=['DELETE'])

# def delete_order(order_id):
#   order = db.session.get(Order,order_id)

#   if not order:
#     return jsonify({"Error":"order not found"})
  
#   db.session.delete(order)
#   db.session.commit()

#   return jsonify({"Message":f"order_id:{order_id}, successfully deleted"})
