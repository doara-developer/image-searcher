
import os

from connectors.bing import BingConnector


class SearchView:
    """View class for search request"""
    def __init__(self, id=''):
        """
        init method
        Attributes:
            id(str): user id
        """
        self.id = id

    def search(self, keyword):
        """
        search keyword
        Args:
            keyword(str): keyword for search
        """
        api_key = os.environ.get('BingAPIKey')
        connector = BingConnector(api_key)
        result_list = connector.search(keyword)
        res = {}
        res['data_list'] = [
            {
                'id': result.id,
                'name': result.name,
                'src': result.src,
                'published_date': result.published_date,
                'thumbnail': result.thumbnail,
            }
            for result in result_list
        ]
        return res
