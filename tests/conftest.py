import pytest
from webtest import TestApp
from symptoms.app import create_app


@pytest.yield_fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app()
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def testapp(app):
    """A Webtest app."""
    return TestApp(app)
