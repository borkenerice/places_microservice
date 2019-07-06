import os
import sys

if os.path.abspath(os.curdir) not in sys.path:
    print('...missing directory in PYTHONPATH... added!')
    sys.path.append(os.path.abspath(os.curdir))

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
    # Create the database
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        # iterate over the PEOPLE structure and populate the database
        for place in PLACES:
            p = Place(name=place.get("name"))
            db.session.add(p)
        db.session.commit()


if __name__ == '__main__':
    create_database()
