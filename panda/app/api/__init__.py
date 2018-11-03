# -*- coding: utf-8 -*-

from . import student
from . import teacher
from . import web
from . import wechat


def register_blueprints(app):
    student.register_blueprints(app)
    teacher.register_blueprints(app)
    web.register_blueprints(app)
    wechat.register_blueprints(app)
    pass
