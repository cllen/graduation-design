#coding:utf8
from flask_restx import Model,fields
from ...apis.v1 import api

# 业务代码
from .user import User

task_elective = api.model(
	'task_elective',
	{
		'id':fields.Integer(),
		'student':fields.Nested(User),
		'plan_course_scheduling':fields.String(),
		'is_agent_selected':fields.Boolean(),
		'auditive_status':fields.String(),
		'selected_datetime':fields.String(),
		'audited_datetime':fields.String(),
		'did_I_elect':fields.String(),
	}
)

Entry = api.model(
	'Entry',
	{
		'error_code':fields.Integer(),
		'error_message':fields.String(),
		'error_detail':fields.String(),
		'error_detail2':fields.String(),
		'entry':fields.Nested(task_elective),
	},
)

Entries = api.model(
	'Entries',
	{
		'error_code':fields.Integer(),
		'count':fields.Integer(),
		'entries':fields.List(fields.Nested(task_elective)),
	},
)


# 关于命名：优先写 entry / entries，如果请求之间有差别，再写 get / post / put