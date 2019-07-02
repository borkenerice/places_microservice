import pytest
from api import create_app, db
from api.models import Place


@pytest.fixture(scope='module')
def client():
    """
    fixture that initializes the flask app to be used in the tests
    :return: flask app
    """
    app = create_app()
    client = app.test_client()
    with app.app_context():
        yield client


@pytest.fixture(scope='module')
def init_database():
    """
    fixture that initializes the db to be used in the tests
    :return: db
    """
    db.create_all()
    place = Place(name='Westeros Test')
    place2 = Place(name='Kingslanding Test')
    db.session.add(place)
    db.session.add(place2)
    db.session.commit()
    yield db
    db.drop_all()


def test_read_places_response_status(client, init_database):
    """
    Check correct response code for a get request to the place endpoint
    :param client: fixture
    :param init_database: fixture
    :return:
    """
    response = client.get('/api/place')
    assert response.status_code == 200


def test_read_place_response(client, init_database):
    """
    Check correct response code for a get request for a unique place
    :param client: fixture
    :param init_database: fixture
    :return:
    """
    response = client.get('/api/place/1')
    assert response.status_code == 200


def test_read_place_do_not_exists(client, init_database):
    """
    Check correct response code for a get request for a unique place if it does not exists
    :param client: fixture
    :param init_database: fixture
    :return:
    """
    response = client.get('/api/place/4')
    assert response.status_code == 404


def test_create_place(client, init_database):
    """
    Check correct response code for a post request to create a place
    :param client: fixture
    :param init_database: fixture
    :return:
    """
    place = {
        'name': 'Place Create Test'
    }
    response = client.post('/api/place', json=place)
    assert response.status_code == 201


def test_create_place_same_name_error(client, init_database):
    """
    Check correct response code for a post request to create a place if it has the same name as one that already exists
    :param client: fixture
    :param init_database: fixture
    :return:
    """
    place = {
        'name': 'Place Create Test'
    }
    response = client.post('/api/place', json=place)
    assert response.status_code == 400


def test_update_place(client, init_database):
    """
    Check correct response code for a put request to update a place
    :param client: fixture
    :param init_database: fixture
    :return:
    """
    place = {
        'name': 'Place Update Test',
    }
    response = client.put('/api/place/1', json=place)
    assert response.status_code == 201


def test_update_place_same_name_error(client, init_database):
    """
    Check correct response code for a put request to update a place if it has the same name as one that already exists
    :param client: fixture
    :param init_database: fixture
    :return:
    """
    place = {
        'name': 'Place Update Test',
    }
    response = client.put('/api/place/2', json=place)
    assert response.status_code == 400


def test_delete_place(client, init_database):
    """
    Check correct response code for a delete request to delete a place
    :param client: fixture
    :param init_database: fixture
    :return:
    """
    response = client.delete('/api/place/1')
    assert response.status_code == 200


def test_delete_place_does_not_exists_error(client, init_database):
    """
    Check correct response code for a delete request to delete a place that do not exists
    :param client: fixture
    :param init_database: fixture
    :return:
    """
    response = client.delete('/api/place/80')
    assert response.status_code == 404




