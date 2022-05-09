from ..utils.admin_model_view import ModelView

from ..utils.constants import Term

from ..utils.flask_admin.view.login import LoginMixin
from ..utils.flask_admin.view.query import QueryMixin

class GradeClass(LoginMixin,QueryMixin,ModelView):


	column_labels = {
		'campus_code':'校区代码',
		'specialty':'专业',
		'grade':'年级',
		'code':'行政班代码',
		'name':'行政班名称',
		'headteacher':'班主任',
		'classroom_numbering':'教室编号',
		'male_number':'男生人数',
		'female_number':'女生人数',
		'total_number':'总人数',
		'class_monitor':'班长',
		'found_date':'建班年月',
		'plan_teaching':'培养方案',
		'current_term':'当前学期',
		'class_member_ids':'班级成员',
	}

	column_list = [
		'id',
		'code',
		'name',
		'classroom_numbering',
		'headteacher_id',
		'class_monitor_id',
		'total_number',
	]


	form_choices = {
		'current_term': [
			(Term.one, Term.one),
			(Term.two, Term.two),
			(Term.three, Term.three),
			(Term.four, Term.four),
			(Term.five, Term.five),
			(Term.six, Term.six),
			(Term.seven, Term.seven),
			(Term.eight, Term.eight),
			(Term.nine, Term.nine),
			(Term.ten, Term.ten),
		]
	}

	column_choices = {
		'current_term': [
			(Term.one, Term.one),
			(Term.two, Term.two),
			(Term.three, Term.three),
			(Term.four, Term.four),
			(Term.five, Term.five),
			(Term.six, Term.six),
			(Term.seven, Term.seven),
			(Term.eight, Term.eight),
			(Term.nine, Term.nine),
			(Term.ten, Term.ten),
		]
	}
