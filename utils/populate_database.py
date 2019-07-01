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


def create_database():
    # Delete database file if it exists currently
    if os.path.exists(os.path.join(config.BASE_DIR, 'places.db')):
        os.remove(os.path.join(config.BASE_DIR, 'places.db'))
    # Create the database
    app = create_app()
    with app.app_context():
        db.create_all()
        # iterate over the PEOPLE structure and populate the database
        for place in PLACES:
            p = Place(name=place.get("name"))
            db.session.add(p)
        db.session.commit()


if __name__ == '__main__':
    create_database()
