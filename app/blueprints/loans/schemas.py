from app.extentions import ma
from app.models import Loan
from marshmallow import fields
# CREATING SCHEMAS
#Loa Schema

class LoanSchema(ma.SQLAlchemyAutoSchema): 
  books = fields.Nested("BookSchema",many=True)
  member = fields.Nested("MemberSchema")
  book_ids = fields.List(fields.Integer(),load_only=True)
  class Meta:
    model = Loan
    include_fk = True
    fields = ("loan_date", "member_id", "id", "books", "member", "book_ids")
class EditLoanSchema(ma.Schema):
  add_book_ids = fields.List(fields.Integer(), required=True)
  remove_book_ids = fields.List(fields.Integer(),required=True)
  class Meta:
    fields = ("add_book_ids", "remove_book_ids")

loan_schema = LoanSchema() #Allow serialization for a single user
loans_schema = LoanSchema(many=True) #Allow serialization for many users
return_loan_schema = LoanSchema(exclude=["member_id"])
edit_loan_schema = EditLoanSchema() #Schema for editing loans