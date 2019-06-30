import os

import unittest
from config import db, app, connexion_app
from api.models import Place


class PlacesTests(unittest.TestCase):
    basedir = os.path.abspath(os.path.dirname(__file__))
    connexion_app.add_api('api/swagger.yml')
    app.config['TESTING'] = True
    client = app.test_client()
    # database creation and initialization
    if os.path.exists("test.db"):
        os.remove("test.db")
    if os.name == 'nt':
        sqlite_url = "sqlite:///" + os.path.join(basedir, "test.db")
    else:
        sqlite_url = "sqlite:////" + os.path.join(basedir, "test.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
    db.create_all()
    # Data to initialize database
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
    for place in PLACES:
        p = Place(name=place.get("name"))
        db.session.add(p)
    db.session.commit()

    def test_get_place(self):
        response = self.client.get('api/place')
        assert response.status_code == 200

    def test_return_place(self):
        response = self.client.get('api/place/1')
        assert response.status_code == 200




