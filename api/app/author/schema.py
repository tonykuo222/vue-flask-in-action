from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from app.author.models import Author
from app.books.schema import BookSchema
from app import db

class AuthorSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Author
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    created = fields.String(dump_only=True)
    books = fields.Nested(BookSchema, many=True, only=['title','year','id'])
