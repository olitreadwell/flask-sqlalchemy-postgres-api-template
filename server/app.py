#!/usr/bin/env python3

import os

from flask import Flask, current_app, g, make_response, request

app = Flask(__name__)


# happens before every request
@app.before_request
def before_request():
    # g is a global object for the context of the request
    # sets the current working directory path to the global object
    g.path = os.path.abspath(os.getcwd())


@app.route("/")
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


@app.route("/<string:username>")
def user(username):
    return f"<h1>Welcome to my Flask app, {username}!</h1>"


@app.route("/print/<parameter>")
def print_parameter(parameter):
    print(parameter)
    return parameter


@app.route("/count/<parameter>")
def count_parameter(parameter):
    rendered_string = ""

    for i in range(int(parameter)):
        rendered_string += str(i) + "\n"

    return rendered_string


@app.route("/math/<num1>/<operation>/<num2>")
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


if __name__ == "__main__":
    app.run(port=5555, debug=True)
