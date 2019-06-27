import os
from config import db
from models import Place

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

# Delete database file if it exists currently
if os.path.exists("places.db"):
    os.remove("places.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for place in PLACES:
    p = Place(name=place.get("name"))
    db.session.add(p)

db.session.commit()
