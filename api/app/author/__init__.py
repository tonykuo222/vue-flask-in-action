from flask import Blueprint
author_bp = Blueprint('author_bp',__name__)
from app.author import routes
