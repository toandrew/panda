# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

from . import config

student_config_bp = Blueprint('student_config', __name__, url_prefix="/app/config")
student_config_api = Api(student_config_bp)

student_config_api.add_resource(config.StudentConfigIndex, "/index")
student_config_api.add_resource(config.StudentConfigAbout, "/about")
student_config_api.add_resource(config.StudentConfigHelp, "/help")
student_config_api.add_resource(config.StudentConfigAgreement, "/agreement")
student_config_api.add_resource(config.StudentConfigPrivate, "/private")
student_config_api.add_resource(config.StudentConfigUploadLog, "/upload_log")
