import re

from flask import jsonify, request

from . import app, db
from .models import URLMap
from .views import get_unique_short_id
from .error_handlers import InvalidAPIUsage


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    if ('custom_id' not in data or
        data.get('custom_id') == '' or
        data.get('custom_id') is None):
        data['custom_id'] = get_unique_short_id()
    
    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        custom_id = data['custom_id']
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
    
    if not re.match(r'^[a-zA-Z\d]{0,9}$', data.get('custom_id')):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', 400)

    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify(urlmap.to_dict()), 201 


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_link(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': urlmap.original}), 200
