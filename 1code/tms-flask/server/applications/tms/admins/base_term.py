from ..utils.admin_model_view import ModelView

from ..utils.flask_admin.view.login import LoginMixin
from ..utils.flask_admin.view.query import QueryMixin

class BaseTerm(LoginMixin,QueryMixin,ModelView):

	column_labels = {
		'code':'学期码',
		'year':'学年（度）',
		'term_name':'学期名称',
		'start_date':'学期开始日期',
		'end_date':'学期结束日期',
	}

	column_list = [
		'id',
		'code',
		'year',
		'term_name',
		'start_date',
		'end_date',
	]