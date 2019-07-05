import os
import sys

if os.path.abspath(os.curdir) not in sys.path:
    print('...missing directory in PYTHONPATH... added!')
    sys.path.append(os.path.abspath(os.curdir))

import config
from api import db, create_app
from api.models import Character


# Data to initialize database with
CHARACTERS = [
    {
        "name": "Jon",
        "place_id": "1",
        "king": False,
        "alive": False
    },
    {
        "name": "Sansa",
        "place_id": "1",
        "king": True,
        "alive": True
    },
    {
        "name": "Doggie",
        "place_id": "2",
        "king": False,
        "alive": False
    },
]


def create_database():
    # Create the database
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        # iterate over the PEOPLE structure and populate the database
        for character in CHARACTERS:
            p = Character(name=character.get("name"), place_id=character.get("place_id"), king=character.get("king"),
                          alive=character.get("alive"))
            db.session.add(p)
        db.session.commit()


if __name__ == '__main__':
    create_database()
