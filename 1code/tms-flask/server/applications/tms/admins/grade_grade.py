from ..utils.admin_model_view import ModelView

from ..utils.flask_admin.view.login import LoginMixin
from ..utils.flask_admin.view.query import QueryMixin

class GradeGrade(LoginMixin,QueryMixin,ModelView):

	column_labels = {
		'code':'年级代码（根据年份编号）',
		'name':'年级名称',
		'year':'所属年份',
		'state':'年级状态',
	}

	column_list = [
		'id',
		'code',
		'name',
		'year',
		'state',
	]