import pytest
from flaskboilerplate import create_app,db
from flaskboilerplate.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User('renish','patkennedy79@gmail.com', 'FlaskIsAwesome')
    return user

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

#
# @pytest.fixture(scope='module')
# def init_database(test_client):
#     # Create the database and the database table
#
#
#     # Insert user data
#     user1 = User(username='renishxta', email='renishpp00@gmail.com',password='FlaskIsAwesome')
#     # user2 = User(username='kennxedy',email='kennxedyfamilyrecipes@gmail.com', password='PaSsWoRd')
#     db.session.add(user1)
#     # db.session.add(user2)
#
#     # Commit the changes for the users
#     db.session.commit()
#
#     yield  # this is where the testing happens!
#
#     db.drop_all()
#
