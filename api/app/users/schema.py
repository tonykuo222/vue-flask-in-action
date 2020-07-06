from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from app.users.models import User
from app import db

class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = User
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    username = fields.String(required=True)
