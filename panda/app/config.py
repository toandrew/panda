# -*- coding: utf-8 -*-


import os
import yaml


class Config(object):
    DEBUG = True

    def __init__(self):
        app_dir = os.path.dirname(__file__)
        config_file = self.__class__.__name__ + ".yml"
        config_file_with_full_path = os.path.join(app_dir, config_file)
        if os.path.isfile(config_file_with_full_path):
            obj_yaml = yaml.load(open(config_file_with_full_path))
            for k, v in obj_yaml.items():
                setattr(self, k, v)

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB_IDX = 0
    SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    UPLOAD_FOLDER = "/tmp"
    QINIU_ACCESS_KEY = 'C1_of-9bVOWfAHq07NI0uEhSmvk_9barxVWvxJYi'
    QINIU_SECRET_KEY = '5b13oJOzCOaIyduNEBjmZm1lfWspck2QDhVF4X2J'

    RAVEN = "https://9dcea27d7ee546ee9fc76b412e7594f5@sentry.io/1312654"

    LOG_CONFIG = {
        "version": 1,
        'disable_existing_loggers': False,
        "formatters": {
            'verbose': {
                'format':
                    '%(asctime)s %(levelname)s { module name : %(module)s Line no : %(lineno)d} %(message)s'
            },
            'simple': {
                'format': '%(asctime)s %(levelname)s %(message)s'
            }
        },
        "handlers": {
            'errorHandler': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': 'error.log',
                'maxBytes': 1024 * 1024 * 5,
                'backupCount': 5,
                'level': 'ERROR',
                'formatter': 'verbose',
                'encoding': 'utf8'
            },
            'console': {
                'class': 'logging.StreamHandler'
            }
        },
        "loggers": {
            "": {
                'handlers': ['errorHandler'],
                'level': "DEBUG",
            },
            "kafka": {
                "handlers": ["console"],
                "level": "INFO"
            },
            "app": {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            }
        }
    }


class DevConfig(Config):
    DEBUG = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:a1b2c3@A@localhost/xplatform"

    QINIU_BUCKET = "study-fun-dev"
    QINIU_BASE_URL = "http://store-dev.study-fun.com"

    #   微信公众号
    WX_APP_ID = "wxc21dea3e7234dc93"
    WX_APP_SECRET = "ff898d549f06b3602324f3c6e1973bed"
    WX_TOKEN = "bd5786123d2079f4ac74046c73b707a0"
    ENCODING_AES_KEY = "aDknCYNoR45eThxGh8Dr8UjHNszSrLywJsib3cnEgts"

    #   微信公众平台
    OPEN_WX_APPID = "wx5a163580673692df"
    OPEN_WX_SECRET = "43bd181eb3293448e3cf3ee989097c86"

    API_BASE_URL = "http://api-dev.study-fun.com/api/1.0"
    SHARE_SERVER_BASE_URL = "http://share-dev.study-fun.com"

    RAVEN = "https://9dcea27d7ee546ee9fc76b412e7594f5@sentry.io/1312654"


class ProdConfig(Config):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://xplatform_prod:Xplatform_Prod@rm-bp14iu40glat494rj.mysql.rds.aliyuncs.com/xplatform_prod"

    QINIU_BUCKET = "study-fun-prod"
    QINIU_BASE_URL = "http://store.study-fun.com"

    #   微信公众号
    WX_APP_ID = "wx06c5be2d107df576"
    WX_APP_SECRET = "432f7658412ff84ff2d3a8efe2a6e27d"
    WX_TOKEN = "5786123d2079f4ac74046c73b707a0bd"
    ENCODING_AES_KEY = "sSoFY9jb914ZCoDbLtD3sZ0foGG6QplODL3w7dZNQFv"

    #   微信公众平台
    OPEN_WX_APPID = "wx6888ab95098e6cac"
    OPEN_WX_SECRET = "93aff6b0b545da7e3727f0d67731e3c2"

    API_BASE_URL = "http://api.study-fun.com/api/1.0"
    SHARE_SERVER_BASE_URL = "http://share.study-fun.com"

    RAVEN = "https://9dcea27d7ee546ee9fc76b412e7594f5@sentry.io/1312654"


def get_config():
    env = os.getenv("FLASK_ENV", "dev")
    env_map = {
        "dev": DevConfig(),
        "prod": ProdConfig()
    }

    return env_map[env]
