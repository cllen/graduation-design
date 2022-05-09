from ..utils.admin_model_view import ModelView

from ..utils.constants import CourseClassification,Nature

from libs.flask_admin_tablefield import TableCheckBoxField

from ..utils.flask_admin.view.login import LoginMixin
from ..utils.flask_admin.view.query import QueryMixin

class PlanCourseScheduling(LoginMixin,QueryMixin,ModelView):

	column_labels = {
		'plan_course':'课程',
		'base_term':'学期',
		'teaching_datetimes':'教学时间',
		'teaching_place':'教学地点',
		'teaching_resource':'教学资源',
		'campus':'教学班所在校区',
		'start_week':'起始周',
		'end_week':'终止周',
		'hours_of_week':'周学时',
		'expected_members':'计划人数',
		'actual_members':'已选人数',

		'for_base_major_ids':'是否限定专业',
		'for_grade_grade_ids':'是否限定年级',
		'for_grade_class_ids':'是否限定班级',
		'task_elective_ids':'预选学生',
	
		'teacher':'教师',
		'remark':'开课说明（备注）',
	}

	column_list = [
		'id',
		'plan_course',
		'base_term',
		'datetime',
		'teaching_place',
		'expected_members',
		'actual_members',

		'for_grade_class_ids',
		'teacher',
	]

	form_overrides = {
		'teaching_datetimes': TableCheckBoxField({
			"第一节":{"周一":0,"周二":0,"周三":0,"周四":0,"周五":0,},
			"第二节":{"周一":0,"周二":0,"周三":0,"周四":0,"周五":0,},
			"第三节":{"周一":0,"周二":0,"周三":0,"周四":0,"周五":0,},
			"第四节":{"周一":0,"周二":0,"周三":0,"周四":0,"周五":0,},
			"第五节":{"周一":0,"周二":0,"周三":0,"周四":0,"周五":0,},
			"第六节":{"周一":0,"周二":0,"周三":0,"周四":0,"周五":0,},
		}),
	}

