from app.extentions import ma
from app.models import Item

# CREATING SCHEMAS
#item Schema

class ItemSchema(ma.SQLAlchemyAutoSchema): 
  class Meta:
    model = Item
  
item_schema = ItemSchema() #Allow serialization for a single user
items_schema = ItemSchema(many=True) #Allow serialization for many users
