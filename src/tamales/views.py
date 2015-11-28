from flask import jsonify, request, redirect, abort
import redis
from baseconv import BaseConverter

from tamales import app, __version__


redis_store = redis.StrictRedis(host=app.config['REDIS_HOST'],
                                port=app.config['REDIS_PORT'],
                                db=app.config['REDIS_DB'])

base62random = BaseConverter(app.config['ALPHABET'])


def get_url(code):
    url = redis_store.get(code)
    if url:
        return url.decode('utf-8')


def get_code(url):
    # Store counter value using the zero element of the alphabet
    counter = app.config['ALPHABET'][0]

    with redis_store.pipeline() as pipe:
        for _ in range(app.config['REDIS_COUNTER_ERRORS']):
            try:
                pipe.watch(counter)
                value = pipe.get(counter) or 0
                next_value = int(value) + 1
                code = base62random.encode(next_value)
                pipe.multi()
                pipe.set(counter, next_value)
                pipe.set(code, url)
                pipe.execute()
                break
            except redis.WatchError:
                continue
    return code


@app.route("/api/v1/")
def index():
    data = {
        'name': 'tamales',
        'version': __version__,
        'url': 'http://t.antojitos.io/',
    }
    return jsonify(**data)


@app.route("/api/v1/urls", methods=['POST'])
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


@app.route("/api/v1/urls/<code>", methods=['GET'])
def metadata(code):
    long_url = get_url(code)
    if not long_url:
        abort(404)
    short_url = '{0}{1}'.format(request.host_url, code)
    data = {
        'long_url': long_url,
        'short_url': short_url,
    }
    return jsonify(**data)


@app.route("/<code>")
def go_to(code):
    url = get_url(code)
    if not url:
        abort(404)
    return redirect(url)
