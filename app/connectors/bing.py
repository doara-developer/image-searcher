
import requests

from models.search_result import SearchResult


class BingConnector():
    """Bing connector class"""

    API_URL = 'https://api.cognitive.microsoft.com/bing/v7.0/images'

    def __init__(self, api_key):
        """
        init method
        Attributes:
            api_key(str): API Key
        """
        self.api_key = api_key

    def search(self, keyword):
        """search
        Args:
            keyword(str): search keyword
        """
        url = self.API_URL + '/search'
        headers = {
            'Ocp-Apim-Subscription-Key': self.api_key
        }
        query = {
            'q': keyword,
        }
        res = requests.get(url, headers=headers, params=query)
        res_json = res.json()
        return [
            SearchResult(
                id=item['imageId'],
                name=item['name'],
                src=item['contentUrl'],
                published_date=item['datePublished'],
                thumbnail=item['thumbnailUrl']
            )
            for item in res_json['value']
        ]
