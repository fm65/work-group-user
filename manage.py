import getpass
import unittest

from flask.cli import FlaskGroup

from src import app, db
from src.accounts.models import User

cli = FlaskGroup(app)


@cli.command("test")
def test():
    """Runs the unit tests without coverage."""
    print("Runs the unit tests without coverage.\n")
    tests = unittest.TestLoader().discover("tests/test_forms")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    tests = unittest.TestLoader().discover("tests/test_models")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    tests = unittest.TestLoader().discover("tests/test_routes")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    
    if result.wasSuccessful():
        return 0
    else:
        return 1

@cli.command("test_forms")
def test():
    """Runs the unit test_forms without coverage."""
    tests = unittest.TestLoader().discover("tests/test_forms")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1

@cli.command("test_models")
def test():
    """Runs the unit test_models without coverage."""
    tests = unittest.TestLoader().discover("tests/test_models")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1

@cli.command("test_routes")
def test():
    """Runs the unit test_routes without coverage."""
    tests = unittest.TestLoader().discover("tests/test_routes")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


@cli.command("create_admin")
def create_admin():
    """Creates the admin user."""
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Enter password again: ")
    if password != confirm_password:
        print("Passwords don't match")
        return 1
    try:
        user = User(username=username, password=password, is_admin=True)
        db.session.add(user)
        db.session.commit()
        print(f"Admin with username {username} created successfully!")
    except Exception:
        print("Couldn't create admin user.")

@cli.command("generate_fake")
def generate_fake():
    """Generate a number of fake users for testing"""
    try:
        user = User.generate_fake()
        print(f"Fake users generated successfully!")
    except Exception:
        print("Couldn't generate fake users.")


if __name__ == "__main__":
    cli()
