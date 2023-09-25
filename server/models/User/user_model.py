from datetime import datetime

from extensions import db


class User(db.Model):
    """User model."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    user_products = db.relationship("UserProduct", back_populates="user")

    def __repr__(self):
        return f"<User id={self.id} username={self.username} email={self.email} \
                    password={self.password} first_name={self.first_name} last_name={self.last_name} \
                    user_products={self.user_products} created_at={self.created_at} \
                    updated_at={self.updated_at}>"
