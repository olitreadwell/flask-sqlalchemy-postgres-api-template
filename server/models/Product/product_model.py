from extensions import db


class Product(db.Model):
    """Product model."""

    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Product {self.name}>"
