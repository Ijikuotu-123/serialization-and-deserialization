from marshmallow import Schema, fields


class UserSchema(Schema):
    class Meta():
        load_only = ('password',) # dumping(GET) won't display password (password) must be a tuple
        dump_only = ('id',)# this means will be displayed by GET and for POST isn't needed since the system will do that 
    id = fields.Int()  # id is autoincremental and it will be handle by sqlalchemy
    username = fields.Str(reqired = True)
    password = fields.Str(required = True)
# this is used for both post and get( loading and dumping) which means during a GET request the password
#  will be displayed. to hide the password, introduce the class Meta

# we are now using flask_marshmallow instead of the ordinary marshmallow
# flask_marshmallow helps us to link our schema and the sqlalchemy models and helps to remove repetition



from ma import ma
from marshmallow import pre_dump
from model.user import UserModel # since we are linking the two


class UserSchema(ma.ModelSchema):  # we are now inheritng from ma.ModelSchema and no schema
    class Meta():
        model = UserModel   # this becomes our schema.inheriting the UserModel(i.e the fields defined as the table)
        load_only = ('password',) # dumping(GET) won't display password (password) must be a tuple
        dump_only = ('id','confirmation') # this means will be displayed for GET and for POST isn't needed since the system will do that 
    
    @ pre_dump
    def _pre_dump(self, user: UserModel):
        user.confirmation =[user.most_recent_confirmation]
        return user