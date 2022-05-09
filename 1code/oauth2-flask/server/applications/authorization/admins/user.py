from flask_admin.contrib import sqla

from ..utils.flask_admin.query import QueryMixin
from ..utils.flask_admin.login import LoginMixin

from applications.authorization.utils.constants import UserType

class User(LoginMixin,QueryMixin,sqla.ModelView):

	column_labels = {
		'username':'用户名',
		'account':'账号',
		'password':'密码',
		'type':'类型',
	}

	column_list = [
		'id',
		'username',
		# 'password',
		'account',
		'type',
	]

	form_choices = {
		'type': [
			(UserType.student, UserType.student),
			(UserType.teacher, UserType.teacher),
			(UserType.admin, UserType.admin),
		],
	}

	column_choices = {
		'type': [
			(UserType.student, UserType.student),
			(UserType.teacher, UserType.teacher),
			(UserType.admin, UserType.admin),
		],
	}