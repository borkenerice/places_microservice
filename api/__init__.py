import connexion
import config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    connexion_app = connexion.App(__name__, specification_dir=config.BASE_DIR)
    app = connexion_app.app
    app.config.from_object(config)
    connexion_app.add_api(config.SWAGGER_DIR)
    initialize_extensions(app)
    return app


def initialize_extensions(app):
    db.init_app(app)
    ma.init_app(app)
