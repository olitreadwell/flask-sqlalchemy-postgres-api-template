from extensions import db

# this is an absolute import from the root of the project
# server is the root of the project
# extensions is a file in the root of the project


class User(db.Model):
    """User model."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f"<User {self.username}>"
