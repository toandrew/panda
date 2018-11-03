# -*- coding: utf-8 -*-

from flask import request, current_app

from core.api import ApiBase


class StudentIdfaList(ApiBase):
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


class StudentIdfaAdd(ApiBase):
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
