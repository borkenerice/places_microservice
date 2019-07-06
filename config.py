import os

DEBUG = True
TESTING = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

POSTGRES_USER = 'places_micro'
POSTGRES_PASSWORD = 'places_micro'
POSTGRES_DB = 'places_micro_db'
POSTGRES_SERVICE = 'postgres_places'
POSTGRES_PORT = '5432'
SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVICE}:{POSTGRES_PORT}/{POSTGRES_DB}'

SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

SWAGGER_DIR = os.path.join(BASE_DIR, 'api', 'swagger.yml')
