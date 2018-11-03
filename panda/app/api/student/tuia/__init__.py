# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

from . import tuia

student_tuia_bp = Blueprint('student_tuia', __name__, url_prefix="/app/tuia")
student_tuia_api = Api(student_tuia_bp)

student_tuia_api.add_resource(tuia.Tuia, "/")
