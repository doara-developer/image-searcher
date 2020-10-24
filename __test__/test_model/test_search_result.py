
from models.search_result import SearchResult


class TestSearchResult(object):
    """Test for TestSearchResult model."""
    dummy_id = 'dummy_id'
    dummy_name = 'dummy_name'
    dummy_src = 'dummy_src'
    dummy_published_date = 'published_date'
    dummy_thumbnail = 'dummy_thumbnail'

    def test_init(self):
        """Test init"""
        model = SearchResult(
            id=self.dummy_id,
            name=self.dummy_name,
            src=self.dummy_src,
            published_date=self.dummy_published_date,
            thumbnail=self.dummy_thumbnail,
        )

        assert model.id == self.dummy_id
        assert model.name == self.dummy_name
        assert model.src == self.dummy_src
        assert model.published_date == self.dummy_published_date
        assert model.thumbnail == self.dummy_thumbnail
