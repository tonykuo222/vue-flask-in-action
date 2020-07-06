from flask import Blueprint

books_bp = Blueprint('books_bp',__name__)

from app.books import routes
