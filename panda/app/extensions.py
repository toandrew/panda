# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()
cors_app = CORS()
debug_toolbar = DebugToolbarExtension()
