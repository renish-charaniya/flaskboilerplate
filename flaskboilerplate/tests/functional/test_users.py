def test_login_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


def test_valid_login(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post(
        "/login", data=dict(email="krack@g.c", password="renish"), follow_redirects=True
    )
    print(response.data)
    assert response.status_code == 200
    assert b"welcome" in response.data
    assert b"Login" not in response.data
    # assert b'Register' not in response.data
