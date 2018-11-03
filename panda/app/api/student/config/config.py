# -*- coding: utf-8 -*-

from flask import request, current_app

from core.api import ApiBase


class StudentConfigIndex(ApiBase):
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


class StudentConfigAbout(ApiBase):
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


class StudentConfigHelp(ApiBase):
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


class StudentConfigAgreement(ApiBase):
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


class StudentConfigPrivate(ApiBase):
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


class StudentConfigUploadLog(ApiBase):
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
