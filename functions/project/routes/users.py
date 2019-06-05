from flask import Blueprint, jsonify

user_bp = Blueprint('users', __name__)


@user_bp.route('/')
def users():
    return jsonify(list(range(100)))
