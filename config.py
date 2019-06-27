import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connexion_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connexion_app.app

# Build the Sqlite ULR for SqlAlchemy
sqlite_url = "sqlite:///" + os.path.join(basedir, "places.db")
print(f'sqlite_url: {sqlite_url}')

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the SqlAlchemy db and Marshmallow instances
db = SQLAlchemy(app)
ma = Marshmallow(app)
