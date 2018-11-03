# -*- coding: utf-8 -*-

from flask import request, current_app

from core.api import ApiBase


class LikeList(ApiBase):
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


class Like(ApiBase):
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


class UnLike(ApiBase):
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


class PushWeiXin(ApiBase):
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


class Device(ApiBase):
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


class ScheduleCancel(ApiBase):
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


class UserInfo(ApiBase):
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


class GetUserId(ApiBase):
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


class InviteRecord(ApiBase):
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


class Opinion(ApiBase):
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
