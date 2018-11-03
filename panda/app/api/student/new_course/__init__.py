# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

from . import new_course

student_new_course_bp = Blueprint('student_new_course', __name__, url_prefix="/app/new_course")
student_new_course_api = Api(student_new_course_bp)

student_new_course_api.add_resource(new_course.HomePageList, "/home_page_list")
student_new_course_api.add_resource(new_course.List, "/list")
student_new_course_api.add_resource(new_course.NewTeacherList, "/new_teacher_list")
student_new_course_api.add_resource(new_course.TeacherWriteLog, "/teacher_write_log")
student_new_course_api.add_resource(new_course.TeacherList, "/teacher_list")
student_new_course_api.add_resource(new_course.TeacherComments, "/teacher_comments")
student_new_course_api.add_resource(new_course.TeacherDetail, "/teacher_detail")
student_new_course_api.add_resource(new_course.TeacherTimeDetail, "/teacher_time_detail")
student_new_course_api.add_resource(new_course.BookSchedule, "/book_schedule")
student_new_course_api.add_resource(new_course.Detail, "/detail")
student_new_course_api.add_resource(new_course.SetUserNote, "/set_user_note")
student_new_course_api.add_resource(new_course.CancelSchedule, "/cancel_schedule")
student_new_course_api.add_resource(new_course.CancelScheduleAlertInfo, "/cancel_schedule_alert_info")
student_new_course_api.add_resource(new_course.CourseList, "/course_list")
student_new_course_api.add_resource(new_course.TeacherScheduleCalendar, "/teacher_schedule_calendar")
student_new_course_api.add_resource(new_course.TeacherSchedules, "/teacher_schedules")
student_new_course_api.add_resource(new_course.NewTeacherDetail, "/new_teacher_detail")
student_new_course_api.add_resource(new_course.GetTimeBoundary, "/get_time_boundary")
