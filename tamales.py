from flask import Flask
from flask import jsonify, request, redirect
import redis
from baseconv import BaseConverter


app = Flask(__name__)

redis_store = redis.StrictRedis(host='redis.lxc', port=6379, db=0)
base62random = BaseConverter('h6sCQgcPqJNrSzlWn5TfeBK8HxiY1Z7'
                             'kIap3yXODMbvVt0m2udjRU4GEFoL9Aw')


def generate_code():
    counter = redis_store.incr('counter')
    return base62random.encode(counter)


def get_url(code):
    url = redis_store.get(code)
    return url.decode('utf-8')


def get_code(url):
    # FIXME: this function must be atomic
    # See http://redis.io/topics/transactions
    code = generate_code()
    redis_store.set(code, url)
    return code


@app.route("/")
def index():
    data = {
        'name': 'tamales',
        'version': '0.1',
        'url': 'https://github.com/Antojitos/tamales/',
    }
    return jsonify(**data)


@app.route("/", methods=['POST'])
def shorten():
    request_json = request.get_json()
    long_url = request_json['url']
    code = get_code(long_url)
    short_url = '{0}{1}'.format(request.host_url, code)
    data = {
        'long_url': long_url,
        'short_url': short_url,
    }
    return jsonify(**data)


@app.route("/<code>/metadata")
def metadata(code):
    long_url = get_url(code)
    short_url = '{0}{1}'.format(request.host_url, code)
    data = {
        'long_url': long_url,
        'short_url': short_url,
    }
    return jsonify(**data)


@app.route("/<code>")
def go_to(code):
    url = get_url(code)
    return redirect(url)


if __name__ == "__main__":
    app.run(debug=True)
