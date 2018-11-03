# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

from . import tune

student_tune_bp = Blueprint('student_schedule', __name__, url_prefix="/app/tune")
student_tune_api = Api(student_tune_bp)

student_tune_api.add_resource(tune.NewList, "/new_list")
student_tune_api.add_resource(tune.BList, "/blist")
student_tune_api.add_resource(tune.OList, "/olist")
student_tune_api.add_resource(tune.TList, "/tlist")
student_tune_api.add_resource(tune.UtList, "/utList")
student_tune_api.add_resource(tune.UstList, "/ustList")
student_tune_api.add_resource(tune.Select, "/select")
student_tune_api.add_resource(tune.CopyHistory, "/copy_history")
student_tune_api.add_resource(tune.Upload, "/upload")
student_tune_api.add_resource(tune.UtRename, "/utRename")
student_tune_api.add_resource(tune.UstRename, "/ustRename")
student_tune_api.add_resource(tune.UstDelete, "/ustDelete")
student_tune_api.add_resource(tune.UstReplace, "/ustReplace")
student_tune_api.add_resource(tune.SelectGroup, "/select_group")
student_tune_api.add_resource(tune.Report, "/report")
student_tune_api.add_resource(tune.History, "/history")
student_tune_api.add_resource(tune.DetailHistory, "/detail_history")
