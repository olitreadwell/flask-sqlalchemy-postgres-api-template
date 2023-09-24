from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# i had to move this to its own file
# because of circular imports with the models
