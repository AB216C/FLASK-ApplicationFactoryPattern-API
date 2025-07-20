from app.extentions import ma
from app.models import Member

# CREATING SCHEMAS
#Member Schema

class MemberSchema(ma.SQLAlchemyAutoSchema): 
  class Meta:
    model = Member
  
member_schema = MemberSchema() #Allow serialization for a single user
members_schema = MemberSchema(many=True) #Allow serialization for many users