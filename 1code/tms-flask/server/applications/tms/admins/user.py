from ..utils.admin_model_view import ModelView

from ..utils.flask_admin.view.login import LoginMixin
from ..utils.flask_admin.view.query import QueryMixin

class User(LoginMixin,QueryMixin,ModelView):
	
	column_labels = {
		'oauth2_user_id':'统一登录id',
		'account':'账号',
		'username':'用户名',
		'type':'用户类型',
		'_class':'班级',
	}

	column_list = [
		'id',
		'oauth2_user_id',
		'grade_name',
		'account',
		'username',
		'type',
		'_class',
	]