from app.extentions import ma
from app.models import Book

# CREATING SCHEMAS
#Book Schema

class BookSchema(ma.SQLAlchemyAutoSchema): 
  class Meta:
    model = Book
  
book_schema = BookSchema() #Allow serialization for a single user
books_schema = BookSchema(many=True) #Allow serialization for many users
