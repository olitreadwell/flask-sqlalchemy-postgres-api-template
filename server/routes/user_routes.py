from flask import Blueprint, make_response
from models import User
from sqlalchemy.sql.expression import func

user_routes = Blueprint("user_routes", __name__)


def user_string(user):
    user_string = f"""
                        <tr>
                            <td>{user.id}</td>
                            <td>{user.username}</td>
                            <td>{user.email}</td>
                            <td>{user.first_name}</td>
                            <td>{user.last_name}</td>
                        </tr>
                    """
    return user_string


@user_routes.route("/users/", strict_slashes=False)
def get_all_users():
    users = User.query.all()

    response_body = """<h1>Users</h1>
                    <table>
                        <tr>
                            <th>id</th>
                            <th>username</th>
                            <th>email</th>
                            <th>first_name</th>
                            <th>last_name</th>
                        </tr>
                    """

    for user in users:
        response_body += user_string(user)

    response_body += "</table>"

    response = make_response(response_body, 200)

    return response


@user_routes.route("/users/<int:id>")
def get_user_by_id(id):
    user = User.query.filter(User.id == id).first()

    if not user:
        response = make_response("<h1>404 user not found</h1>", 404)
    else:
        response_body = f"""<h1>User</h1>
                            <table>
                                <tr>
                                    <th>id</th>
                                    <th>username</th>
                                    <th>email</th>
                                    <th>first_name</th>
                                    <th>last_name</th>
                                </tr>
                                {user_string(user)}
                            </table>
                            """

        response = make_response(response_body, 200)

    return response


@user_routes.route("/users/random/", strict_slashes=False)
def get_random_user():
    user = User.query.order_by(func.random()).first()

    response_body = f"""<h1>Random User</h1>
                        <table>
                            <tr>
                                <th>id</th>
                                <th>username</th>
                                <th>email</th>
                                <th>first_name</th>
                                <th>last_name</th>
                            </tr>
                            {user_string(user)}
                        </table>
                        """

    response = make_response(response_body, 200)

    return response


@user_routes.route("/users/random/<int:num_of_users>/", strict_slashes=False)
def get_random_users(num_of_users):
    users = User.query.order_by(func.random()).limit(num_of_users)

    # sort users by id
    users = sorted(users, key=lambda user: user.id)

    response_body = """<h1>Random Users</h1>
                        <table>
                            <tr>
                                <th>id</th>
                                <th>username</th>
                                <th>email</th>
                                <th>first_name</th>
                                <th>last_name</th>
                            </tr>
                        """

    for user in users:
        response_body += user_string(user)

    response_body += "</table>"

    response = make_response(response_body, 200)

    return response
