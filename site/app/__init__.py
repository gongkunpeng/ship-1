# coding: utf-8

from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from config import config


app = Flask(__name__)
app.config.from_object(config['default'])
pages = FlatPages(app)
freezer = Freezer(app)


from . import views, forms
