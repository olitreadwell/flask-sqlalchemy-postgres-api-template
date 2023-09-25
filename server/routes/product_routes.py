from flask import Blueprint, make_response
from models import Product

product_routes = Blueprint("product_routes", __name__)


@product_routes.route("/products")
def get_all_products():
    products = Product.query.all()

    response_body = "<h1>Products</h1>"

    for product in products:
        response_body += f"""
                            <p>
                            <span>id: {product.id}</span>
                            <span>name: {product.name}</span>
                            </p>
                            """

    response = make_response(response_body, 200)

    return response


@product_routes.route("/products/<int:id>")
def get_product_by_id(id):
    product = Product.query.filter(Product.id == id).first()

    if not product:
        response = make_response("<h1>404 product not found</h1>", 404)
    else:
        response_body = f"""<h1>Product</h1>
                            <p>id: {product.id}</p>
                            <p>name: {product.name}</p>
                            """

        response = make_response(response_body, 200)

    return response
