import pytest
from src.app import create_app, db
from src.config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database for testing

@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    app.config.from_object(TestConfig)

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            yield testing_client  # this is where the testing happens!
            db.drop_all()

@pytest.fixture(scope='module')
def init_database():
    db.create_all()
    yield db  # this is where the testing happens!
    db.drop_all()
