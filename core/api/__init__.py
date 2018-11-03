# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource


# todo add validate and error handler

class ApiBase(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def write_json(self, data=None, error=None, code=0, msg='ok'):
        resp = {
            "data": data,
            "errors": error,
            "meta": {
                "code": code,
                "msg": msg
            }
        }
        return resp, 200
