#!/usr/bin/env python3

from app import app, db
from faker import Faker
from models import Product, User

fake = Faker()

with app.app_context():
    # delete all rows in the tables
    Product.query.delete()
    User.query.delete()

    # create users
    users = []
    for _ in range(50):
        simple_profile = fake.simple_profile()
        username = simple_profile["username"]
        user = User(username=username)
        users.append(user)

    db.session.add_all(users)

    # create products
    products = []
    for _ in range(100):
        product_name = fake.color_name() + " " + fake.word(part_of_speech="noun")
        product = Product(name=product_name)
        products.append(product)

    db.session.add_all(products)

    db.session.commit()
