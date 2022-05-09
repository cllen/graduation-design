from flask import request, current_app
from flask_admin import expose, BaseView

from ..utils.flask_admin.query import QueryMixin
from ..utils.flask_admin.login import LoginMixin

from flask import request,Response,redirect

class Configuration(LoginMixin,QueryMixin,BaseView):

	html_name = 'admin/configuration.html'

	@expose('/',methods=['get'])
	def get(self):
		data = current_app.settings
		return self.render(self.html_name,data=data)

	@expose('/',methods=['post'])
	def post(self):
		data = request.form.to_dict()
		data = current_app.settings.update(**data)
		return self.render(self.html_name,data=data)
