#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my Flask app!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Welcome to my Flask app, {username}!</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5555)