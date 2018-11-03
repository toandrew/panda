# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

from . import user

student_user_bp = Blueprint('student_schedule', __name__, url_prefix="/app/user")
student_user_api = Api(student_user_bp)

student_user_api.add_resource(user.LikeList, "/like_list")
student_user_api.add_resource(user.Like, "/like")
student_user_api.add_resource(user.UnLike, "/unlike")
student_user_api.add_resource(user.PushWeiXin, "/pushWeixin")
student_user_api.add_resource(user.Device, "/device")
student_user_api.add_resource(user.ScheduleCancel, "/schedule_cancel")
student_user_api.add_resource(user.UserInfo, "/user_info")
student_user_api.add_resource(user.GetUserId, "/get_user_id")
student_user_api.add_resource(user.InviteRecord, "/inviteRecord")
student_user_api.add_resource(user.Opinion, "/opinion")
