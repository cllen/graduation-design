from ..utils.admin_model_view import ModelView

from ..utils.constants import EducationSystem

from ..utils.flask_admin.view.login import LoginMixin
from ..utils.flask_admin.view.query import QueryMixin

class BaseMajor(LoginMixin,QueryMixin,ModelView):

	column_labels = {
		'code':'专业代码',
		'name':'专业名称',
		'english_name':'专业英文名称',
		'short_name':'专业简称',
		'education_system':'学制',
		'hours':'总学时',
		'direction':'专业方向名称',
		'found_date':'建立年月',
		'teacher_ids':'专业教师数',
		# 'insitution_numbering':'开设机构号',
		# 'total_credict':'总学分',
	}

	column_list = [
		'id',
		'code',
		'name',
		'short_name',
		'education_system',
		'total_credict',
	]

	form_choices = {
		'education_system': [
			(EducationSystem.three, EducationSystem.three),
			(EducationSystem.five, EducationSystem.five),
		],
	}

	column_choices = {
		'education_system': [
			(EducationSystem.three, EducationSystem.three),
			(EducationSystem.five, EducationSystem.five),
		],
	}