from ..utils.admin_model_view import ModelView
from libs.flask_pagedown.fields import PageDownField

from libs.flask_admin_tablefield import TableField

from ..utils.flask_admin.view.login import LoginMixin
from ..utils.flask_admin.view.query import QueryMixin

class PlanTeaching(LoginMixin,QueryMixin,ModelView):
	
	edit_template = 'admin/plan_teaching_edit.html'

	column_labels = {
		'code':'培养方案代码',
		'name':'培养方案名称',
		'major':'专业',
		'education_system':'学制',
		'prospective_student':'招生对象',
		'fields':'领域方向',
		'professions':'职业岗位',
		'content':'培养方案内容',
		'plan':'教学计划',
		'credit':'学分',
	}

	column_list = [
		'id',
		'code',
		'name',
		'major',
		'education_system',
	]

	form_overrides = {
        'content': PageDownField,
        'plan':TableField([
        	'课程类型','课程名','学分',
        	'第一学期','第二学期','第三学期','第四学期','第五学期',
        	'第六学期','第七学期','第八学期','第九学期','第十学期',
        ]),
        'credit':TableField([
        	'项',
        	'第一学期','第二学期','第三学期','第四学期','第五学期',
        	'第六学期','第七学期','第八学期','第九学期','第十学期',
        ],is_showing_btn=False),
    }

