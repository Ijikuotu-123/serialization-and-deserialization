from ma import ma
from model.item import ItemModel # since we are linking the model and the schema together using flask_marsh
from model.store import StoreModel # this is reqiured because their is a relationship between item and store


class itemSchema(ma.ModelSchema):  # we are now inheritng from ma.ModelSchema and no schema
    class Meta():
        model = ItemModel   # inheriting the ItemModel(i.e the fields defined in the table)
        load_only = ('store',) # dumping(GET) won't display store (store,) must be a tuple
        dump_only = ('id',)# this means: will be displayed for GET and for POST isn't needed 
        include_fk = True  # we dont ingnore anything that is used to link table  
