# -*- coding: utf-8 -*-

from .auth import student_auth_bp
from .bill import student_bill_bp
from .config import student_config_bp
from .idfa import student_idfa_bp
from .im import student_im_bp
from .new_course import student_new_course_bp
from .schedule import student_schedule_bp
from .tuia import student_tuia_bp
from .tune import student_tune_bp
from .user import student_user_bp


def register_blueprints(app):
    app.register_blueprint(student_auth_bp)
    app.register_blueprint(student_bill_bp)
    app.register_blueprint(student_config_bp)
    app.register_blueprint(student_idfa_bp)
    app.register_blueprint(student_im_bp)
    app.register_blueprint(student_new_course_bp)
    app.register_blueprint(student_schedule_bp)
    app.register_blueprint(student_tuia_bp)
    app.register_blueprint(student_tune_bp)
    app.register_blueprint(student_user_bp)
    pass
