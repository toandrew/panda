# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

from . import idfa

student_idfa_bp = Blueprint('student_idfa', __name__, url_prefix="/app/idfa")
student_idfa_api = Api(student_idfa_bp)

student_idfa_api.add_resource(idfa.StudentIdfaList, "/list")
student_idfa_api.add_resource(idfa.StudentIdfaAdd, "/add")
