def test_new_user_with_fixture(new_user):

    assert new_user.username=='renish'
    assert new_user.email == 'patkennedy79@gmail.com'
    assert new_user.password != 'FlaskIsAwesome'

def test_setting_password(new_user):
    """
    GIVEN an existing User
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext
    """
    new_user.set_password('MyNewPassword')
    assert new_user.password != 'MyNewPassword'
    assert new_user.is_correct_password('MyNewPassword')
    assert not new_user.is_correct_password('MyNewPassword2')
    assert not new_user.is_correct_password('FlaskIsAwesome')

