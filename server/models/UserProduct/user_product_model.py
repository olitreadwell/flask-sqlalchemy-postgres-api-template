from extensions import db

# this is an absolute import from the root of the project
# server is the root of the project
# extensions is a file in the root of the project


class UserProduct(db.Model):
    """UserProduct model."""

    __tablename__ = "user_products"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    # add a relationship to the User model
    user = db.relationship("User", back_populates="user_products")
    # add a relationship to the Product model
    product = db.relationship("Product", back_populates="user_products")

    def __repr__(self):
        return f"<UserProduct id={self.id} user_id={self.user_id} product_id={self.product_id} \
                    quantity={self.quantity} created_at={self.created_at} updated_at={self.updated_at}>"
