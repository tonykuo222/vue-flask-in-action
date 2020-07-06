from app.books.models import Book
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from app import db

class BookSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Book
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    year = fields.Integer(required=True)
    author_id = fields.Integer()
