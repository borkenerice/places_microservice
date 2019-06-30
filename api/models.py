from api import db, ma
from sqlalchemy.orm import validates


class Place(db.Model):
    __tablename__ = "place"
    place_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    @validates('name')
    def validate_name(self, key, name):
        if Place.query.filter(Place.name == name).one_or_none():
            raise ValueError('The name already exists')
        return name


class PlaceSchema(ma.ModelSchema):
    class Meta:
        model = Place

