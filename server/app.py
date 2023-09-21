#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Welcome to my Flask app, {username}!</h1>'


@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter


@app.route('/count/<parameter>')
def count_parameter(parameter):
    rendered_string = ''
    
    for i in range(int(parameter)):
        rendered_string += str(i) + '\n'
        
    return rendered_string


@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(int(num1) + int(num2))
    elif operation == '-':
        return str(int(num1) - int(num2))
    elif operation == '*':
        return str(int(num1) * int(num2))
    elif operation == 'div':
        return str(int(num1) / int(num2))
    elif operation == '%':
        return str(int(num1) % int(num2))
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run(port=5555, debug=True)


if __name__ == '__main__':
    app.run(debug=True, port=5555)