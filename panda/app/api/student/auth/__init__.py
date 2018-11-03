# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

from . import auth

student_auth_bp = Blueprint('student_auth', __name__, url_prefix="/app/auth")
student_auth_api = Api(student_auth_bp)

student_auth_api.add_resource(auth.StudentSignIn, "/signin")
student_auth_api.add_resource(auth.StudentNewSignIn, "/new_signin")
student_auth_api.add_resource(auth.StudentSignUp, "/signup")
student_auth_api.add_resource(auth.StudentSignOut, "/signout")
student_auth_api.add_resource(auth.StudentSendValidateCode, "/send_validate_code")
student_auth_api.add_resource(auth.StudentImToken, "/im_token")
student_auth_api.add_resource(auth.StudentUserInfo, "/user_info")
