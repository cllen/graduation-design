from ..utils.admin_model_view import ModelView

from ..utils.flask_admin.view.login import LoginMixin
from ..utils.flask_admin.view.query import QueryMixin

from ..utils.constants import ElectiveStatus

class TaskElective(LoginMixin,QueryMixin,ModelView):

	column_labels = {
		'student':'学生',
		'plan_course_scheduling':'课程',
		'is_agent_selected':'是否代选',
		'auditive_status':'选课审核状态',

		'selected_datetime':'选课时间',
		'audited_datetime':'审核时间',
		'auditor':'审核人',
	}

	column_list = [
		'id',
		'student',
		'plan_course_scheduling',
		'auditive_status',
		'auditor',
	]


	form_choices = {
		'auditive_status': [
			(ElectiveStatus.selected, ElectiveStatus.selected),
			(ElectiveStatus.approved, ElectiveStatus.approved),
			(ElectiveStatus.rejected, ElectiveStatus.rejected),
		],
	}

	column_choices = {
		'auditive_status': [
			(ElectiveStatus.selected, ElectiveStatus.selected),
			(ElectiveStatus.approved, ElectiveStatus.approved),
			(ElectiveStatus.rejected, ElectiveStatus.rejected),
		],
	}