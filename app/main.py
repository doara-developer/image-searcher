from flask import Flask

from routes.search import search

version = '/v1.0'
app = Flask(__name__)

app.register_blueprint(search, url_prefix=version + '/search')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, threaded=True)
