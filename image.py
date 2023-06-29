from marshmallow import Schema,fields
from werkzeug.datastructures import FileStorage

''' We won't be saving our images to the database, so we don't need a model but we will check if what is
coming in is an image of the accepted type and then deserialize (load) it '''

class FileStorageField(fields.Field):
    default_error_messages = {
        "invalid": "Not a valid image."
    }
    def _deserialize(self,value,attr,data) -> FileStorage:
        if value is None:
            return None
        if not isinstance (value, FileStorage):
            raise self.fail("invalid")      # raise ValidationError. fail is a method in the field super class                       
        return value


class ImageSchema(Schema):
    image = FileStorageField(required=True)

''' FilestoragField does not exist so we have to create it as shown above'''

