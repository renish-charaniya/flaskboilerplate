from flaskboilerplate.models import User


def test_new_user_with_fixture(new_user):

    user = User("renish", "krack@g.c", "renish")
    assert new_user.username == "renish"
    assert new_user.email == "krack@g.c"
    assert new_user.password != "renish"
    assert user.__repr__() == '<User("renish","krack@g.c")>'

    assert user.is_authenticated
    assert user.is_active
    assert not user.is_anonymous


def test_setting_password(new_user):
    """
    GIVEN an existing User
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext
    """

    new_user.set_password("renish")
    assert new_user.password != "renish"
    assert new_user.is_correct_password("renish")
    assert not new_user.is_correct_password("renishc")
    assert not new_user.is_correct_password("renishc")


def test_user_id(new_user):
    """
    GIVEN an existing User
    WHEN the ID of the user is defined to a value
    THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
    """
    new_user.id = 555
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == "555"
