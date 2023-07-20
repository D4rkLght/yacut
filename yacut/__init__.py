from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
LENGHT_SHORT_LINK = 6
ONLY_DIGITS_AND_LETTERS = r'^[a-zA-Z\d]{0,9}$'

from . import api_views, error_handlers, views