from extensions import db

# this is an absolute import from the root of the project
# server is the root of the project
# extensions is a file in the root of the project


class Product(db.Model):
    """Product model."""

    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    category = db.Column(db.String(80))
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, name, description, price, quantity, category, image_url):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.category = category
        self.image_url = image_url

    def __repr__(self):
        return (
            f"<Product id={self.id}, name={self.name}, "
            f"description={self.description}, price={self.price}, "
            f"quantity={self.quantity}, category={self.category}, "
            f"image_url={self.image_url}, created_at={self.created_at}, "
            f"updated_at={self.updated_at}>"
        )
