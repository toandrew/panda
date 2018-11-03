# -*- coding: utf-8 -*-

from flask import request, current_app

from core.api import ApiBase


class StudentSignIn(ApiBase):
    """
    """

    def post(self):
        stats = request.get_json(force=True)

        # TODO
        ret = None
        if not ret:
            return self.write_json(code=2, msg="operation failed")
        else:
            return self.write_json()


class StudentNewSignIn(ApiBase):
    """
    """

    def post(self):
        stats = request.get_json(force=True)

        # TODO
        ret = None
        if not ret:
            return self.write_json(code=2, msg="operation failed")
        else:
            return self.write_json()


class StudentSignUp(ApiBase):
    """
    """

    def post(self):
        stats = request.get_json(force=True)

        # TODO
        ret = None
        if not ret:
            return self.write_json(code=2, msg="operation failed")
        else:
            return self.write_json()


class StudentSignOut(ApiBase):
    """
    """

    def post(self):
        stats = request.get_json(force=True)

        # TODO
        ret = None
        if not ret:
            return self.write_json(code=2, msg="operation failed")
        else:
            return self.write_json()


class StudentSendValidateCode(ApiBase):
    """
    """

    def post(self):
        stats = request.get_json(force=True)

        # TODO
        ret = None
        if not ret:
            return self.write_json(code=2, msg="operation failed")
        else:
            return self.write_json()


class StudentImToken(ApiBase):
    """
    """

    def post(self):
        stats = request.get_json(force=True)

        # TODO
        ret = None
        if not ret:
            return self.write_json(code=2, msg="operation failed")
        else:
            return self.write_json()


class StudentUserInfo(ApiBase):
    """
    """

    def post(self):
        stats = request.get_json(force=True)

        # TODO
        ret = None
        if not ret:
            return self.write_json(code=2, msg="operation failed")
        else:
            return self.write_json()
