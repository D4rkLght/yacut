from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, ValidationError

from . import MAX_LENGHT_SHORT_URL, MAX_LENGHT_URL
from .models import URLMap


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите оригинальную ссылку',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(max=MAX_LENGHT_URL)]
    )
    custom_id = StringField(
        'Введите короткий вариант ссылки',
        validators=[Length(max=MAX_LENGHT_SHORT_URL), Optional()]
    )
    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        if URLMap.query.filter_by(short=field.data).first():
            raise ValidationError(f'Имя {field.data} уже занято!')
