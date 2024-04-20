"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
from shop.models.user import User, UserAddress, Role, UserRole
from shop.models.utils import Permission

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password_hashed, authenticated, and active fields are defined correctly
    """

    user = User.get_or_create(
      username='test_user',
      email='test_user@test_user.com',
      password="password",
      is_active=True
    )

    assert user.email == 'test_user@test_user.com'
    assert user.password_hashed != 'FlaskIsAwesome'
    assert user.is_authenticated
    assert user.is_active
    assert not user.can_admin

def test_new_admin_user():
  for permissions, (name, desc) in Permission.PERMISSION_MAP.items():
    Role.create(name=name, permissions=permissions)
    yield f"Role {name} created"

  user = User.create(
    username="admin", email="admin@admin.com", password="admin", is_active=True
  )
  UserRole.create(user_id=user.id, role_id=4)

  assert user.email == 'admin@admin.com'
  assert user.password_hashed == 'admin'
  assert user.is_authenticated
  assert user.is_active
  assert user.can_admin

def test_setting_password():
    """
    GIVEN an existing User
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext
    """
    user = User.get_or_create(
      username='test_user',
      email='test_user@test_user.com',
      password="password",
      is_active=True
    )
    user.set_password('MyNewPassword')
    assert user.password_hashed != 'MyNewPassword'
    assert user.is_password_correct('MyNewPassword')
    assert not user.is_password_correct('MyNewPassword2')
    assert not user.is_password_correct('FlaskIsAwesome')

def test_user_id():
    """
    GIVEN an existing User
    WHEN the ID of the user is defined to a value
    THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
    """
    user = User.get_or_create(
      username='test_user',
      email='test_user@test_user.com',
      password="password",
      is_active=True
    )
    user.id = 17
    assert isinstance(user.get_id(), str)
    assert not isinstance(user.get_id(), int)
    assert user.get_id() == '17'

def test_new_address():
  """
  GIVEN a User model
  WHEN a new User is created
  THEN try to create an address for him
  """
  user = User.get_or_create(
    username='test_user',
    email='test_user@test_user.com',
    password="password",
    is_active=True
  )

  address = UserAddress.create(
    contact_name='User1 address',
    province='Lisbon',
    city='Lisbon1',
    district='Lisbon2',
    address='LisbonStreet',
    contact_phone='210000000',
    user_id=user.id
  )

  assert address.contact_name == 'User1 address'
  assert address.province == 'Lisbon'
  assert address.city == 'Lisbon1'
  assert address.district == 'Lisbon2'
  assert address.user_id == user.id

def test_new_role():
  """
  GIVEN a User model
  WHEN a new Role is created
  THEN check values
  """
  role = Role.create(name='new_role', permissions='user')
  assert role.name == 'new_role'
  assert role.permissions == 'user'

def test_new_user_role():
  """
  GIVEN a User model
  WHEN a new User is created
  THEN try to create an address for him
  """
  role = Role.create(name='new_role', permissions='user')
  user = User.get_or_create(
    username='test_user',
    email='test_user@test_user.com',
    password="password",
    is_active=True
  )

  user_role = UserRole.create(user_id=user.id, role_id=role.id)
  assert user_role.user_id == role.id
  assert user_role.role_id == user.id

from shop.models.product import Product

def test_new_book():
    """
    GIVEN a Book model
    WHEN a new Book is created
    THEN check the title, author, and rating fields are defined correctly
    """
    book = Book('Malibu Rising', 'Taylor Jenkins Reid', '5', 1)
    assert book.title == 'Malibu Rising'
    assert book.author == 'Taylor Jenkins Reid'
    assert book.rating == 5
    assert book.__repr__() == '<Book: Malibu Rising>'

def test_update_book():
    """
    GIVEN a Book model
    WHEN a new Book is updated
    THEN check the title, author, and rating fields are updated correctly
    """
    book = Book('Malibu Rising', 'Taylor Jenkins Reid', '5', 1)

    book.update(new_title='Carrie Soto is Back')
    assert book.title == 'Carrie Soto is Back'
    assert book.author == 'Taylor Jenkins Reid'
    assert book.rating == 5

    book.update(new_rating='4')
    assert book.title == 'Carrie Soto is Back'
    assert book.author == 'Taylor Jenkins Reid'
    assert book.rating == 4

    book.update(new_author='Taylor J. Reid')
    assert book.title == 'Carrie Soto is Back'
    assert book.author == 'Taylor J. Reid'
    assert book.rating == 4

    book.update(new_title='Book Lovers', new_author='Emily Henry', new_rating='5')
    assert book.title == 'Book Lovers'
    assert book.author == 'Emily Henry'
    assert book.rating == 5
