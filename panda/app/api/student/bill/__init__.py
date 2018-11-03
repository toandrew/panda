# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api

from . import bill

student_bill_bp = Blueprint('student_bill', __name__, url_prefix="/app/bill")
student_bill_api = Api(student_bill_bp)

student_bill_api.add_resource(bill.StudentBillList, "/list")
