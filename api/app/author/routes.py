from flask import request
from app import db
from app.author import author_bp
from app.author.models import Author
from app.author.schema import AuthorSchema
from app.utils.responses import response_with
from app.utils import responses as resp


@author_bp.route('/',methods=['POST'])
def create_author():
    try:
        data = request.get_json()
        print(data)
        author_schema = AuthorSchema()
        author = author_schema.load(data)
        result = author_schema.dump(author.create())
        return response_with(resp.SUCCESS_201,value={"author":result})
    except Exception as e:
        #print(e)
        return response_with(resp.INVALID_INPUT_422)

@author_bp.route('/',methods=['GET'])
def get_author_list():
    fetched = Author.query.all()
    author_schema = AuthorSchema(many=True,only=['first_name','last_name','id'])
    authors = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200,value={"authors":authors})

@author_bp.route('/<int:author_id>',methods=['GET'])
def get_author_detail(author_id):
    fetched = Author.query.get_or_404(author_id)
    author_schema = AuthorSchema()
    author = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200,value={"author":author})

@author_bp.route('/<int:id>',methods=['PUT'])
def update_author_detail(id):
    data = request.get_json()
    get_author = Author.query.get_or_404(id)
    get_author.first_name = data['first_name']
    get_author.last_name = data['last_name']
    db.session.add(get_author)
    db.session.commit()
    author_schema = AuthorSchema()
    author = author_schema.dump(get_author)
    return response_with(resp.SUCCESS_200,value={"author":author})

@author_bp.route('/<int:id>',methods=['PATCH'])
def modify_author_detail(id):
    data = request.get_json()
    get_author = Author.query.get(id)
    if data.get('first_name'):
        get_author.first_name = data['first_name']
    if data.get('last_name'):
        get_author.last_name = data['last_name']

    db.session.add(get_author)
    db.session.commit()
    author_schema = AuthorSchema()
    author = author_schema.dump(get_author)
    return response_with(resp.SUCCESS_200,value={"author":author})

@author_bp.route('/<int:id>',methods=['DELETE'])
def delete_author(id):
    get_author = Author.query.get_or_404(id)
    db.session.delete(get_author)
    db.session.commit()
    return response_with(resp.SUCCESS_200)
