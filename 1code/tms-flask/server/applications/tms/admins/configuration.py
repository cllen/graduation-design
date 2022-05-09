from flask import request, current_app
from flask_admin import expose, BaseView
from ..utils.template_mixin import TemplateMixin

from ..utils.flask_admin.view.login import LoginMixin
from ..utils.flask_admin.view.query import QueryMixin

class Configuration(LoginMixin,QueryMixin,BaseView):
	
	html_name = 'admin/configuration.html'

	@expose('/', methods=['get',])
	def get(self):
		data = current_app.settings
		return self.render(self.html_name, data=data)

	@expose('/', methods=['post',])
	def post(self):
		data = request.form.to_dict()
		data = current_app.settings.update(**data)
		return self.render(self.html_name, data=data)
