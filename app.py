from flask import Flask, g, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from views.auth import auth_bp
from views.books import book
from views.create_user import create_user
from database import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

db.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(book, url_prefix='/book')
app.register_blueprint(create_user, url_prefix='/create_user')

@app.before_request
def before_request():
    g.name="vikash"
    g.age=23


@app.route('/')
def test():
    return "Hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

