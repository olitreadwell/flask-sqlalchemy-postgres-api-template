#!/usr/bin/env python3

import os

# import db from extensions to avoid circular imports
from extensions import db
from flask import Flask, g
from flask_migrate import Migrate

# separate routes into their own files
from routes.main_routes import main_routes
from routes.product_routes import product_routes
from routes.user_routes import user_routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

# register blueprints lets us separate routes into their own files
app.register_blueprint(main_routes)
app.register_blueprint(user_routes)
app.register_blueprint(product_routes)


# happens before every request
@app.before_request
def before_request():
    # g is a global object for the context of the request
    # sets the current working directory path to the global object
    g.path = os.path.abspath(os.getcwd())


if __name__ == "__main__":
    app.run(port=5555, debug=True)
