from flask import make_response, abort
from config import db
from models import Place, PlaceSchema


def get_all_places():
    places = Place.query.order_by(Place.name).all()
    place_schema = PlaceSchema(many=True)
    data = place_schema.dump(places).data
    return data


def get_place(place_id):
    place = Place.query.filter(Place.place_id == place_id).one_or_none()
    if place is not None:
        place_schema = PlaceSchema()
        data = place_schema.dump(place).data
        return data
    else:
        abort(404, f'Place not found with the id: {place_id}')
