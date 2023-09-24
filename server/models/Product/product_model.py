from extensions import db

# this is an absolute import from the root of the project
# server is the root of the project
# extensions is a file in the root of the project


class Product(db.Model):
    """Product model."""

    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Product {self.name}>"
