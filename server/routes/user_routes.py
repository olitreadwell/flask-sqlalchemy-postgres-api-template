from flask import Blueprint, jsonify, make_response
from models import User
from sqlalchemy.sql.expression import func

user_routes = Blueprint("user_routes", __name__)


api_v1 = "/api/v1"


@user_routes.route(api_v1 + "/users/", strict_slashes=False)
def get_all_users():
    users = []

    all_users = User.query.all()
    all_users = sorted(all_users, key=lambda user: user.id)

    for user in all_users:
        user_dict = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        users.append(user_dict)

    response = make_response(jsonify(users), 200, {"Content-Type": "application/json"})

    return response


@user_routes.route(api_v1 + "/users/<int:id>/", strict_slashes=False)
def get_user_by_id(id):
    user = User.query.filter(User.id == id).first()

    if not user:
        response = make_response(
            jsonify({"error": f"User with id {id} not found"}),
            404,
            {"Content-Type": "application/json"},
        )
    else:
        user = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }

        response = make_response(
            jsonify(user), 200, {"Content-Type": "application/json"}
        )

    return response


@user_routes.route(api_v1 + "/users/random/", strict_slashes=False)
def get_random_user():
    user = User.query.order_by(func.random()).first()

    if not user:
        response_body = {"error": "No users found"}
    else:
        response_body = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }

    response = make_response(
        jsonify(response_body), 200, {"Content-Type": "application/json"}
    )

    return response


@user_routes.route(api_v1 + "/users/random/<int:num_of_users>/", strict_slashes=False)
def get_random_users(num_of_users):
    returned_users = []

    random_users = User.query.order_by(func.random()).limit(num_of_users)
    random_users = sorted(random_users, key=lambda user: user.id)

    for user in random_users:
        user_dict = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        returned_users.append(user_dict)

    response = make_response(
        jsonify(returned_users), 200, {"Content-Type": "application/json"}
    )

    return response
