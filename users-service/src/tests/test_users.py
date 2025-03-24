import json

def test_register_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' route is POSTed to (with valid data)
    THEN a '201' status code is returned
    """
    data = {
        'email': 'test@example.com',
        'password': 'password123'
    }
    response = test_client.post('/users/register', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201

def test_login_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' route is POSTed to (with valid data)
    THEN a '200' status code is returned
    """
    # First register the user
    data = {
        'email': 'test@example.com',
        'password': 'password123'
    }
    test_client.post('/users/register', data=json.dumps(data), content_type='application/json')

    # Then login
    response = test_client.post('/users/login', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200

def test_login_invalid_credentials(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' route is POSTed to (with invalid credentials)
    THEN a '401' status code is returned
    """
    data = {
        'email': 'test@example.com',
        'password': 'wrongpassword'
    }
    response = test_client.post('/users/login', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 401
