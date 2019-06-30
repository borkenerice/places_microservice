import os
import config
from api import db, create_app
from api.models import Place

# Data to initialize database with
PLACES = [
    {
        "name": "Westeros",
    },
    {
        "name": "Kingslanding"
    },
    {
        "name": "Winterfell"
    },
]


def create_database(database_name):
    # Delete database file if it exists currently
    if os.path.exists(os.path.join(config.BASE_DIR, database_name)):
        os.remove(os.path.join(config.BASE_DIR, database_name))

    if os.name == 'nt':
        sqlite_url = "sqlite:///" + os.path.join(config.BASE_DIR, database_name)
    else:
        sqlite_url = "sqlite:////" + os.path.join(config.BASE_DIR, database_name)

    # Create the database
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_url
    with app.app_context():
        db.create_all()
        # iterate over the PEOPLE structure and populate the database
        for place in PLACES:
            p = Place(name=place.get("name"))
            db.session.add(p)
        db.session.commit()


