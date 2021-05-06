import pytest
from flaskboilerplate import create_app
from flaskboilerplate.models import User
from flaskboilerplate import Config


@pytest.fixture(scope="module")
def new_user():
    user = User("renish", "krack@g.c", "renish")
    return user


@pytest.fixture(scope="module")
def test_client():
    # flask_app = create_app('flask_test.cfg')
    flask_app = create_app(Config)
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!
