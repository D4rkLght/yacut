import re
from http import HTTPStatus

from flask import jsonify, request

from . import ONLY_DIGITS_AND_LETTERS, app, db
from .error_handlers import InvalidAPIUsageError
from .models import URLMap
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsageError('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsageError('"url" является обязательным полем!')
    if 'custom_id' not in data or not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
    if URLMap.query.filter_by(short=data['custom_id']).first():
        custom_id = data['custom_id']
        raise InvalidAPIUsageError(f'Имя "{custom_id}" уже занято.')
    if not re.match(ONLY_DIGITS_AND_LETTERS, data.get('custom_id')):
        raise InvalidAPIUsageError('Указано недопустимое имя для короткой ссылки',
                                   HTTPStatus.BAD_REQUEST)
    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify(urlmap.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_link(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if not urlmap:
        raise InvalidAPIUsageError('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': urlmap.original}), HTTPStatus.OK
