import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# Build the Sqlite ULR for SqlAlchemy
if os.name == 'nt':
    sqlite_url = "sqlite:///" + os.path.join(BASE_DIR, "places.db")
else:
    sqlite_url = "sqlite:////" + os.path.join(BASE_DIR, "places.db")

SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = sqlite_url
SQLALCHEMY_TRACK_MODIFICATIONS = False

SWAGGER_DIR = os.path.join(BASE_DIR, 'api', 'swagger.yml')
