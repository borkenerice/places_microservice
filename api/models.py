from api import db, ma


class Place(db.Model):
    __tablename__ = "place"
    place_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)


class PlaceSchema(ma.ModelSchema):
    class Meta:
        model = Place

