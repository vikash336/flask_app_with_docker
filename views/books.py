from flask import Blueprint , g

book = Blueprint('book', __name__)


@book.route('/login')
def login():
    return "Book page"

@book.route('/register')
def register():
    return "Book register"

@book.route('/')
def index():
    user_data = f"{g.age } {g.name}"
    return f'User Data: {user_data}'

