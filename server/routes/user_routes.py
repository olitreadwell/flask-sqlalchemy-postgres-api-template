from flask import Blueprint, make_response
from models import User

user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/users")
def get_all_users():
    users = User.query.all()

    response_body = "<h1>Users</h1>"

    for user in users:
        response_body += f"""
                            <p>
                            <span>id: {user.id}</span>
                            <span>username: {user.username}</span>
                            </p>
                            """

    response = make_response(response_body, 200)

    return response


@user_routes.route("/users/<int:id>")
def get_user_by_id(id):
    user = User.query.filter(User.id == id).first()

    if not user:
        response = make_response("<h1>404 user not found</h1>", 404)
    else:
        response_body = f"""<h1>User</h1>
                            <p>id: {user.id}</p>
                            <p>username: {user.username}</p>
                            """

        response = make_response(response_body, 200)

    return response
