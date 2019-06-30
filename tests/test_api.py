import pytest
from api import create_app
from utils import populate_database


@pytest.fixture(scope='session')
def test_client():
    populate_database.create_database('test.db')

    app = create_app()

    client = app.test_client()

    with app.app_context():
        yield client


def test_read_places_response(test_client):
    response = test_client.get('/api/place')
    assert response.status_code == 200


def test_read_place_response(test_client):
    response = test_client.get('/api/place/1')
    assert response.status_code == 200


def test_read_place_do_not_exists(test_client):
    response = test_client.get('/api/place/4')
    assert response.status_code == 404


def test_create_place(test_client):
    place = {
        'name': 'Place Create Test'
    }
    response = test_client.post('/api/place', json=place)
    assert response.status_code == 200


def test_create_place_same_name_error(test_client):
    place = {
        'name': 'Place Create Test'
    }
    response = test_client.post('/api/place', json=place)
    assert response.status_code == 400


def test_update_place(test_client):
    place = {
        'name': 'Place Update Test',
    }
    response = test_client.put('/api/place/1', json=place)
    assert response.status_code == 201


def test_update_place_same_name_error(test_client):
    place = {
        'name': 'Place Update Test',
    }
    response = test_client.put('/api/place/1', json=place)
    assert response.status_code == 400


def test_delete_place(test_client):
    response = test_client.delete('/api/place/1')
    assert response.status_code == 200


def test_delete_place_does_not_exists_error(test_client):
    response = test_client.delete('/api/place/80')
    assert response.status_code == 404




