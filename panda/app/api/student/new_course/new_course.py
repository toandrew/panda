# -*- coding: utf-8 -*-

from flask import request, current_app

from core.api import ApiBase


class HomePageList(ApiBase):
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


class List(ApiBase):
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


class NewTeacherList(ApiBase):
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


class TeacherWriteLog(ApiBase):
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


class TeacherList(ApiBase):
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


class TeacherComments(ApiBase):
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


class TeacherDetail(ApiBase):
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


class TeacherTimeDetail(ApiBase):
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


class BookSchedule(ApiBase):
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


class Detail(ApiBase):
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


class SetUserNote(ApiBase):
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


class CancelSchedule(ApiBase):
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


class CancelScheduleAlertInfo(ApiBase):
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


class CourseList(ApiBase):
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


class TeacherScheduleCalendar(ApiBase):
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


class TeacherSchedules(ApiBase):
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


class NewTeacherDetail(ApiBase):
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


class GetTimeBoundary(ApiBase):
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
