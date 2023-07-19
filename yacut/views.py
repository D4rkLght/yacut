import string

from random import sample
from flask import flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id():
    letters_and_digits = string.ascii_letters + string.digits
    short_link = ''.join(sample(letters_and_digits, 6))
    if URLMap.query.filter_by(short=short_link).first():
        return get_unique_short_id()
    return short_link


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if URLMap.query.filter_by(short=custom_id).first():
            flash('Такое сокращение уже используется!')
            return render_template('index.html', form=form)
        if not custom_id:
            custom_id = get_unique_short_id()
        urlmap = URLMap(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(urlmap)
        db.session.commit()
        return render_template('index.html', **{'form': form, 'short_url': custom_id})
    return render_template('index.html', form=form)


@app.route('/<string:short_url>')
def original_redirect_view(short_url):
    url = URLMap.query.filter_by(short=short_url).first_or_404()
    return redirect(url.original)