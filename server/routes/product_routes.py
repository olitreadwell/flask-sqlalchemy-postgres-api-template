from flask import Blueprint, jsonify, make_response
from models import Product
from sqlalchemy.sql.expression import func

product_routes = Blueprint("product_routes", __name__)

api_v1 = "/api/v1"


@product_routes.route(api_v1 + "/products/", strict_slashes=False)
def get_all_products():
    products = []

    all_products = Product.query.all()
    all_products = sorted(all_products, key=lambda product: product.id)

    for product in all_products:
        product_dict = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity": product.quantity,
            "category": product.category,
            "image_url": product.image_url,
        }
        products.append(product_dict)

    response = make_response(
        jsonify(products), 200, {"Content-Type": "application/json"}
    )

    return response


@product_routes.route(api_v1 + "/products/<int:id>/", strict_slashes=False)
def get_product_by_id(id):
    product = Product.query.filter(Product.id == id).first()

    if not product:
        response = make_response(
            jsonify({"error": f"Product with id {id} not found"}),
            404,
            {"Content-Type": "application/json"},
        )
    else:
        product = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity": product.quantity,
            "category": product.category,
            "image_url": product.image_url,
        }

        response = make_response(
            jsonify(product), 200, {"Content-Type": "application/json"}
        )

    return response


@product_routes.route(api_v1 + "/products/random/", strict_slashes=False)
def get_random_product():
    product = Product.query.order_by(func.random()).first()

    if not product:
        response_body = {"error": "No products found"}
    else:
        response_body = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity": product.quantity,
            "category": product.category,
            "image_url": product.image_url,
        }

    response = make_response(
        jsonify(response_body), 200, {"Content-Type": "application/json"}
    )

    return response


@product_routes.route(
    api_v1 + "/products/random/<int:num_of_products>/", strict_slashes=False
)
def get_random_products(num_of_products):
    returned_products = []

    random_products = Product.query.order_by(func.random()).limit(num_of_products)
    random_products = sorted(random_products, key=lambda product: product.id)

    for product in random_products:
        product_dict = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity": product.quantity,
            "category": product.category,
            "image_url": product.image_url,
        }
        returned_products.append(product_dict)

    response = make_response(
        jsonify(returned_products), 200, {"Content-Type": "application/json"}
    )

    return response
