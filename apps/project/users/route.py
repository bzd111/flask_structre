from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def users():
    return jsonify(list(range(10)))
