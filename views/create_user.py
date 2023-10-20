from flask import Blueprint, request , jsonify
from models.models import User
from database import db


create_user=Blueprint('User', __name__)


@create_user.route('/users', methods=['POST'])
def user_creation():
    data = request.get_json()
    print(data)
    new_user = User(**data)
    print(new_user)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"})
