# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

from . import im

student_im_bp = Blueprint('student_im', __name__, url_prefix="/app/im")
student_im_api = Api(student_im_bp)

student_im_api.add_resource(im.StudentImCallback, "/callback")
student_im_api.add_resource(im.StudentRefreshToken, "/refreshToken")
