
from main import app


class TestMain(object):
    """Test for main model."""

    def test_init(self):
        """Test init"""
        app.config['TESTING'] = True
        app.test_client()
