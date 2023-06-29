from ma import ma 
from models.confirmation import ConfirmationModel


class ConfirmationSchema(ma.ModelSchema):
    class meta():
        model = ConfirmationModel
        load_only = ("user",)
        dump_only = ("id","expired at", "confirmed")
        include_fk = True









from marshmallow import schema, fileds
class LoginSchema(schema):
    user_name = fileds.str()
    password = fileds.str()




# EXAMPLE  
class BookSchema():
    title = field.str()
    author = fields.str()

incoming_data ={
    'title': 'clean code',
    'author':'john maxwell',
    'description':'fiction'
}
book_schema = BookSchema()
book = book_schema.load(incoming_data)
# during load if u pass a anthing(e.g description) that is not represented in schema into the schema.
# it will throw an error. since i don't want description to be in the book, then do this:

# Method 1
# add description to the table
class BookSchema():
    title = field.str(required=True)
    author = fields.str(required=True)
    description = fileds.str()
# with this i can either pass description or  not


# method 2
# import INCLUDE AND EXCLUDE from marshamllow and do this :
book_schema = BookSchema(unknown =INCLUDE)
# this will include description
book_schema = BookSchema(unknown =EXCLUDE)
# this will exclude decription






