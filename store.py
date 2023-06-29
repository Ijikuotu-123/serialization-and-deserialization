from ma import ma
from model.store import StoreModel # since we are linking the model and the schema together using flask_marsh
from model.item import ItemModel # this is reqiured because their is a relationship between item and store 
from schemas.item import itemSchema 


class StoreSchema(ma.ModelSchema):  # we are now inheritng from ma.ModelSchema and no schema
    items = ma.Nested(ItemSchema, many= True )
    class Meta():
        model = StoreModel   # inheriting the StoreModel(i.e the fields defined as the table)
        dump_only = ('id',)# this means will be displayed for GET and for POST isn't needed 
         
