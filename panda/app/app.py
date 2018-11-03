# -*- coding: utf-8 -*-

import logging
import logging.config

import sentry_sdk
from flask import Flask
from redis import StrictRedis
from sentry_sdk.integrations.flask import FlaskIntegration

import api

from panda.app.config import get_config

from config import Config
from extensions import (cors_app, db, debug_toolbar)


def create_app(config=get_config()):
    # config logger
    logging.config.dictConfig(Config.LOG_CONFIG)

    app = Flask(__name__)
    app.config.from_object(config)

    configure_sentry(app)
    configure_redis(app)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    api.register_blueprints(app)


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    cors_app.init_app(app)
    marsh_app.init_app(app)
    debug_toolbar.init_app(app)


def configure_redis(app):
    r = StrictRedis(
        host=app.config['REDIS_HOST'],
        port=app.config['REDIS_PORT'],
        db=app.config['REDIS_DB_IDX']
    )

    try:
        r.get("foo")
    except:
        import sys
        print
        "can not connect to redis server..."
        sys.exit(-1)
    app.config['REDIS'] = r


def configure_sentry(app):
    if Config.DEBUG:
        sentry_sdk.init(
            dsn=Config.RAVEN,
            integrations=[FlaskIntegration()]
        )
