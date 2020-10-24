
from unittest.mock import patch

from models.search_result import SearchResult

from views.search import SearchView


class TestSearchView(object):
    """Test for TestSearchView model."""
    dummy_id = 'dummy_id'
    dummy_keyword = 'dummy_keyword'

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

    def test_init(self):
        """Test init"""
        view = SearchView(
            id=self.dummy_id,
        )
        assert view.id == self.dummy_id

    @patch('connectors.bing.BingConnector.search')
    def test_search(self, mock):
        """Test search method"""
        result_1 = SearchResult(
            self.dummy_result_id_1,
            self.dummy_name_1,
            self.dummy_src_1,
            self.dummy_date_1,
            self.dummy_thumbnail_1,
        )
        result_2 = SearchResult(
            self.dummy_result_id_2,
            self.dummy_name_2,
            self.dummy_src_2,
            self.dummy_date_2,
            self.dummy_thumbnail_2,
        )
        mock.return_value = [result_1, result_2]

        view = SearchView(
            id=self.dummy_id,
        )
        result = view.search(self.dummy_keyword)
        assert len(result['data_list']) == 2
