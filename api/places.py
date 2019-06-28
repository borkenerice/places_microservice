from flask import abort
import logging

from config import db
from api.models import Place, PlaceSchema

logger = logging.getLogger(__name__)


def get_all_places():
    places = Place.query.order_by(Place.name).all()
    place_schema = PlaceSchema(many=True)
    data = place_schema.dump(places).data
    return data


def get_place(place_id):
    place = Place.query.get_or_404(place_id, description=f'Place not found with the id: {place_id}')
    place_schema = PlaceSchema()
    data = place_schema.dump(place).data
    return data


def update_place(place_id, place_data):
    place = Place.query.get_or_404(place_id, description=f'Place not found with the id: {place_id}')
    place_schema = PlaceSchema()
    try:
        updated_place = place_schema.load(place_data, session=db.session).data
        updated_place.place_id = place.place_id
        db.session.merge(updated_place)
        db.session.commit()
        data = place_schema.dump(updated_place).data
        return data
    except ValueError as v:
        abort(400, f'Place: {place_id} could not be updated: {v}')


def post_place(place_data):
    try:
        schema = PlaceSchema()
        new_place = schema.load(place_data, session=db.session).data
        db.session.add(new_place)
        db.session.commit()
        data = schema.dump(new_place).data
        return data, 201
    except ValueError as v:
        abort(400, f'Place could not be created: {v}')


def delete_place(place_id):
    place = Place.query.get_or_404(place_id, description=f'Place not found with the id: {place_id}')
    db.session.delete(place)
    db.session.commit()
    return 204

