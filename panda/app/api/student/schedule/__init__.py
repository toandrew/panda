# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

from . import schedule

student_schedule_bp = Blueprint('student_schedule', __name__, url_prefix="/app/schedule")
student_schedule_api = Api(student_schedule_bp)

student_schedule_api.add_resource(schedule.NewList, "/new_list")
student_schedule_api.add_resource(schedule.List, "/list")
student_schedule_api.add_resource(schedule.Detail, "/detail")
student_schedule_api.add_resource(schedule.NewTeacherRate, "/new_teacher_rate")
student_schedule_api.add_resource(schedule.TeacherComment, "/teacher_comment")
student_schedule_api.add_resource(schedule.ScheduleNum, "/schedule_num")
student_schedule_api.add_resource(schedule.Status, "/status")
student_schedule_api.add_resource(schedule.OldEnterClassroom, "/enterclassroom")
student_schedule_api.add_resource(schedule.ScheduleCommentReport, "/schedule_comment_report")
student_schedule_api.add_resource(schedule.EnterClassroom, "/enterClassroom")
student_schedule_api.add_resource(schedule.SaveFgComment, "/save_fg_comment")
student_schedule_api.add_resource(schedule.ShowScheduleComment, "/show_schedule_comment")
student_schedule_api.add_resource(schedule.ShareScheduleReport, "/share_schedule_report")
student_schedule_api.add_resource(schedule.Likes, "/likes")
