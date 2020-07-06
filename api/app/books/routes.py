from flask import request
from app import db
from app.books import books_bp
from app.books.models import Book
from app.books.schema import BookSchema
from app.utils.responses import response_with
from app.utils import responses as resp
from flask_jwt_extended import jwt_required

@books_bp.route('/',methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        book_schema = BookSchema()
        book = book_schema.load(data)
        result = book_schema.dump(book.create())
        return response_with(resp.SUCCESS_201,value={"book":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

@books_bp.route('/',methods=['GET'])
@jwt_required
def get_book_list():
    fetched = Book.query.all()
    book_schema = BookSchema(many=True,only=['author_id','title','year'])
    books = book_schema.dump(fetched)
    return response_with(resp.SUCCESS_200,value={"books":books})

@books_bp.route('/<int:id>',methods=['GET'])
def get_book_detail(id):
    fetched = Book.query.get_or_404(id)
    book_schema = BookSchema()
    books = book_schema.dump(fetched)
    return response_with(resp.SUCCESS_200,value={"books":books})

@books_bp.route('/<int:id>', methods=['PUT'])
def update_book_detail(id):
    data = request.get_json()
    get_book = Book.query.get_or_404()
    get_book.title = data['title']
    get_book.year = data['year']
    db.session.add(get_book)
    db.session.commit()

    book_schema = BookSchema()
    book = book_schema.dump(get_book)
    return response_with(resp.SUCCESS_200,value={"book":book})


@books_bp.route('/<int:id>', methods=['PATCH'])
def modify_book_detail(id):
    data = request.get_or_404()
    get_book = Book.query.get_or_404(id)

    if data.get('title'):
        get_book.title = data['title']
    if data.get('year'):
        get_book_year = data['year']

    db.session.add(get_book)
    db.session.commit()
    book = book_schema.dump(get_book)
    return response_with(resp.SUCCESS_200,value={"book":book})


@books_bp.route('/<int:id>',methods=['DELETE'])
def delete_books(id):
    get_book = Book.query.get_or_404(id)
    db.session.delete(get_book)
    db.session.commit()
    return response_with(resp.SUCCESS_204)
