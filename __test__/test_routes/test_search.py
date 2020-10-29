from unittest.mock import patch
import json

from main import app


class TestSearchRoutes(object):
    """Test for search routes."""

    dummy_result_id_1 = 'dummy_result_id_1'
    dummy_result_id_2 = 'dummy_result_id_2'
    dummy_name_1 = 'dummy_name_1'
    dummy_name_2 = 'dummy_name_2'
    dummy_src_1 = 'dummy_src_1'
    dummy_src_2 = 'dummy_src_2'
    dummy_date_1 = 'dummy_date_1'
    dummy_date_2 = 'dummy_date_2'
    dummy_thumbnail_1 = 'dummy_thumbnail_1'
    dummy_thumbnail_2 = 'dummy_thumbnail_2'

    dummy_result_1 = {
        'id': dummy_result_id_1,
        'name': dummy_name_1,
        'src': dummy_src_1,
        'published_date': dummy_date_1,
        'thumbnail': dummy_thumbnail_1,
    }
    dummy_result_2 = {
        'id': dummy_result_id_2,
        'name': dummy_name_2,
        'src': dummy_src_2,
        'published_date': dummy_date_2,
        'thumbnail': dummy_thumbnail_2,
    }

    @patch('views.search.SearchView.search')
    def test_search_keyword(self, mock):
        """Test search keyword"""
        ret = {}
        ret['data_list'] = [
            self.dummy_result_1,
            self.dummy_result_2,
        ]
        mock.return_value = ret
        app.config['TESTING'] = True
        client = app.test_client()
        res = client.get('/v1.0/search/?keyword=dummy_key')
        resJson = json.loads(res.data)
        assert len(resJson['data_list']) == 2
