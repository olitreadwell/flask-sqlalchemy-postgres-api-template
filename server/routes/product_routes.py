from flask import Blueprint, jsonify, make_response
from models import Product
from sqlalchemy.sql.expression import func

product_routes = Blueprint("product_routes", __name__)


def product_string(product):
    product_string = f"""
                        <tr>
                            <td>{product.id}</td>
                            <td>{product.name}</td>
                            <td>{product.description}</td>
                            <td>{product.price}</td>
                            <td>{product.quantity}</td>
                            <td>{product.category}</td>
                            <td><a href="{product.image_url}" target="_blank">product image</a></td>
                        </tr>
                    """
    return product_string


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
    products = Product.query.order_by(func.random()).limit(num_of_products)

    # sort products by id
    products = sorted(products, key=lambda product: product.id)

    response_body = """<h1>Random Products</h1>
                        <table>
                            <tr>
                                <th>id</th>
                                <th>name</th>
                                <th>description</th>
                                <th>price</th>
                                <th>quantity</th>
                                <th>category</th>
                                <th>image_url</th>
                            </tr>
                        """

    for product in products:
        response_body += product_string(product)

    response_body += "</table>"

    response = make_response(response_body, 200)

    return response
