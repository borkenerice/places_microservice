from config import db, ma


class Place(db.Model):
    __tablename__ = "place"
    place_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Boolean, nullable=False, default=False)


class PlaceSchema(ma.ModelSchema):
    class Meta:
        model = Place

