from flask import (
    Blueprint,
    request,
    jsonify,
)
from views.search import SearchView

search = Blueprint('search', __name__)


@search.route('/', methods=['GET'])
def search_keyword():
    keyword = request.args.get('keyword')
    view = SearchView()
    res = view.search(keyword)
    return jsonify(res)
