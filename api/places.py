from flask import abort
from sqlalchemy.exc import IntegrityError

from api import db
from api.models import Place, PlaceSchema


def find_all_places():
    places = Place.query.order_by(Place.name).all()
    place_schema = PlaceSchema(many=True)
    data = place_schema.dump(places).data
    return data


def find_place_by_id(place_id):
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
        return data, 201
    except IntegrityError as i:
        db.session.rollback()
        abort(400, f'Place: {place_id} could not be updated: {i.orig}')


def create_place(place_data):
    try:
        schema = PlaceSchema()
        new_place = schema.load(place_data, session=db.session).data
        db.session.add(new_place)
        db.session.commit()
        data = schema.dump(new_place).data
        return data, 201
    except IntegrityError as i:
        db.session.rollback()
        abort(400, f'Place could not be created: {i.orig}')


def delete_place(place_id):
    place = Place.query.get_or_404(place_id, description=f'Place not found with the id: {place_id}')
    db.session.delete(place)
    db.session.commit()
    return

