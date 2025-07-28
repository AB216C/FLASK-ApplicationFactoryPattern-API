from app.extentions import ma
from app.models import Order, OrderItems
from marshmallow import fields

# CREATING SCHEMAS
#Order Schema

class ReceiptSchema(ma.Schema):
  '''
  total: 45.45
  order: {
  order_id: 1,
  member_id: 1,
  order_Date: "2025-07-28",
  order_items: [
  {item:[item_name: "PSL", price:34.56, quantity:2]},
  {item:[item_name: "PSL", price:34.56, quantity:2]}
  ]
  }
  
  '''
  total = fields.Float(required=True)
  order = fields.Nested("OrderSchema")

class OrderSchema(ma.SQLAlchemyAutoSchema): 
  class Meta:
    model = Order
    include_relationships = True
  order_items = fields.Nested("OrderItemSchema", exclude=['id'], many=True)

class OrderItemSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = OrderItems
  item = fields.Nested("ItemSchema", exclude =["id"])


class CreateOrderSchema(ma.Schema):
  '''
  {
  member_id:1,
  item_quantity:[item_id:1, quantity:2]
  }
  '''
  member_id = fields.Integer(required=True)
  order_date = fields.Date(required=True)
  item_quant = fields.Nested("ItemQuantSchema", many=True)

class ItemQuantSchema(ma.Schema):
  item_id = fields.Integer(required=True)
  item_quant = fields.Integer(required=True) 

order_schema = OrderSchema() #Allow serialization for a single user
orders_schema = OrderSchema(many=True) #Allow serialization for many users
create_order_schema = CreateOrderSchema() #Schema for creating orders
receipt_schema = ReceiptSchema() #schema for receipt generation



