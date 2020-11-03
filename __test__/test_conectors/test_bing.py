
from unittest.mock import (
    patch,
    MagicMock,
)

from connectors.bing import BingConnector


class TestBingConnector(object):
    """Test for BingConnector model."""
    assert_endpoint = 'https://api.bing.microsoft.com/v7.0/images'
    dummy_api_key = 'dummy_api_key'
    dummy_keyword = 'dummy_keyword'
    dummy_image_id_1 = 'dummy_image_id_1'
    dummy_image_id_2 = 'dummy_image_id_2'
    dummy_name_1 = 'dummy_name_1'
    dummy_name_2 = 'dummy_name_2'
    dummy_content_url_1 = 'dummy_content_url_1'
    dummy_content_url_2 = 'dummy_content_url_2'
    dummy_date_1 = 'dummy_date_1'
    dummy_date_2 = 'dummy_date_2'
    dummy_thumbnail_url_1 = 'dummy_thumbnail_url_1'
    dummy_thumbnail_url_2 = 'dummy_thumbnail_url_2'

    dummy_item_1 = {
        'imageId': dummy_image_id_1,
        'name': dummy_name_1,
        'contentUrl': dummy_content_url_1,
        'datePublished': dummy_date_1,
        'thumbnailUrl': dummy_thumbnail_url_1,
    }
    dummy_item_2 = {
        'imageId': dummy_image_id_2,
        'name': dummy_name_2,
        'contentUrl': dummy_content_url_2,
        'datePublished': dummy_date_2,
        'thumbnailUrl': dummy_thumbnail_url_2,
    }

    def test_init(self):
        """Test init"""
        connector = BingConnector(self.dummy_api_key)
        assert connector.api_key == self.dummy_api_key
        assert connector.API_URL == self.assert_endpoint

    @patch('requests.get')
    def test_search(self, mock):
        """Test search method"""
        mock_res = MagicMock()
        mock_res.json.return_value = {
            'value': [
                self.dummy_item_1,
                self.dummy_item_2,
            ]
        }
        mock.return_value = mock_res
        connector = BingConnector(self.dummy_api_key)
        search_list = connector.search(self.dummy_keyword)
        assert len(search_list) == 2
