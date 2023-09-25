from flask import Blueprint, current_app, g, make_response, redirect, request

main_routes = Blueprint("main_routes", __name__)


@main_routes.route("/")
def index():
    host = request.headers.get("Host")
    app_name = current_app.name

    response_body = f"""<h1>Python Operations with Flask Routing and Views</h1>
               <p>Host: {host}</p>
               <p>App Name: {app_name}</p>
               <p>Path: {g.path}</p>"""

    status_code = 200
    response_headers = {"Content-Type": "text/html"}

    response = make_response(response_body, status_code, response_headers)
    return response


@main_routes.route("/<string:username>")
def user(username):
    return f"<h1>Welcome to my Flask app, {username}!</h1>"


@main_routes.route("/print/<parameter>")
def print_parameter(parameter):
    print(parameter)
    return parameter


@main_routes.route("/redirect")
def redirect_to_index():
    """Redirects to "/"."""
    return redirect("/")


@main_routes.route("/error")
def error():
    """Returns a 500 error."""
    return make_response("<h1>error</h1>", 500)


@main_routes.route("/count/<parameter>")
def count_parameter(parameter):
    rendered_string = ""

    for i in range(int(parameter)):
        rendered_string += str(i) + "\n"

    return rendered_string


@main_routes.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return str(int(num1) + int(num2))
    elif operation == "-":
        return str(int(num1) - int(num2))
    elif operation == "*":
        return str(int(num1) * int(num2))
    elif operation == "div":
        return str(int(num1) / int(num2))
    elif operation == "%":
        return str(int(num1) % int(num2))
    else:
        return "Invalid operation"
