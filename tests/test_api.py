import pytest
from api import create_app, db
from api.models import Place


@pytest.fixture(scope='module')
def test_client():
    app = create_app()

    testing_client = app.test_client()

    context = app.app_context()
    context.push()

    yield testing_client

    context.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert user data
    place = Place(name='Westeros Test')
    place2 = Place(name='Kingslanding Test')
    db.session.add(place)
    db.session.add(place2)

    # Commit the changes for the users
    db.session.commit()

    yield db

    db.drop_all()


def test_read_places_response(test_client, init_database):
    response = test_client.get('/api/place')
    assert response.status_code == 200


def test_read_place_response(test_client, init_database):
    response = test_client.get('/api/place/1')
    assert response.status_code == 200


def test_read_place_do_not_exists(test_client, init_database):
    response = test_client.get('/api/place/3')
    assert response.status_code == 404


def test_create_place(test_client, init_database):
    place = {
        'name': 'Place Create Test'
    }
    response = test_client.post('/api/place', json=place)
    assert response.status_code == 201


def test_create_place_same_name_error(test_client, init_database):
    place = {
        'name': 'Place Create Test'
    }
    response = test_client.post('/api/place', json=place)
    assert response.status_code == 400


def test_update_place(test_client, init_database):
    place = {
        'name': 'Place Update Test',
        'place_id': '1'
    }
    response = test_client.post('/api/place', json=place)
    assert response.status_code == 201


def test_update_place_same_name_error(test_client, init_database):
    place = {
        'name': 'Place Update Test',
        'place_id': '1'
    }
    response = test_client.post('/api/place', json=place)
    assert response.status_code == 400


def test_delete_place(test_client, init_database):
    response = test_client.delete('/api/place/1')
    assert response.status_code == 200


def test_delete_place_does_not_exists_error(test_client, init_database):
    response = test_client.delete('/api/place/80')
    assert response.status_code == 404




