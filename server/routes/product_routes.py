from flask import Blueprint, make_response
from models import Product

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


@product_routes.route("/products")
def get_all_products():
    products = Product.query.all()

    response_body = """<h1>Products</h1>
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


@product_routes.route("/products/<int:id>")
def get_product_by_id(id):
    product = Product.query.filter(Product.id == id).first()

    if not product:
        response = make_response("<h1>404 product not found</h1>", 404)
    else:
        response_body = """<h1>Products</h1>
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

        response_body += product_string(product)

        response_body += "</table>"

        response = make_response(response_body, 200)

    return response
