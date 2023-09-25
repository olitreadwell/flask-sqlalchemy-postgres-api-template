#!/usr/bin/env python3

import random

from app import app, db
from faker import Faker
from models import Product, User, UserProduct

fake = Faker()

with app.app_context():
    # delete all rows in the tables
    UserProduct.query.delete()
    Product.query.delete()
    User.query.delete()

    # create users
    def seed_users():
        print("Seeding users...")
        for _ in range(50):
            simple_profile = fake.simple_profile()
            username = simple_profile["username"]
            email = simple_profile["mail"]
            password = fake.password()
            first_name = simple_profile["name"].split()[0]
            last_name = simple_profile["name"].split()[1]
            user = User(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            db.session.add(user)
        db.session.commit()

    seed_users()

    # create products
    def seed_products():
        print("Seeding products...")
        categories = {
            1: "Electronics",
            2: "Clothing",
            3: "Home",
            4: "Sports",
            5: "Toys",
        }
        for _ in range(100):
            category_id = random.randint(1, 5)
            product = Product(
                name=fake.color_name() + " " + fake.word(part_of_speech="noun"),
                description=fake.sentence(),
                price=(
                    fake.pyfloat(min_value=0, max_value=10000, right_digits=5) * 100
                ),
                quantity=fake.random_int(min=0, max=100),
                category=categories[category_id],
                image_url=fake.image_url(),
            )
            db.session.add(product)
        db.session.commit()

    seed_products()

    # create user products
    def seed_user_products():
        print("Seeding user products...")
        users = User.query.all()
        products = Product.query.all()
        for user in users:
            for _ in range(random.randint(0, 10)):
                product = random.choice(products)
                user_product = UserProduct(
                    user_id=user.id,
                    product_id=product.id,
                    quantity=random.randint(1, 50),
                )
                db.session.add(user_product)
        db.session.commit()

    seed_user_products()
