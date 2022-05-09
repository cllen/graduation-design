from libs.web_utils.authentication.basic_http import Authentication
from libs.web_utils.authentication.exceptions import (
	AuthorizationErrorTypeException,
	AuthorizationErrorUsernameOrPasswordException,
	AuthorizationErrorUnAuthorizationException,
	
)

from flask import request,Response,redirect,current_app
from werkzeug.exceptions import HTTPException

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from flask_admin import expose

"""
	请配合_base.html使用
"""

class LoginMixin:

	authentication = Authentication()

	def is_accessible(self):

		logger.debug('>>>> is_accessible')
		self.authentication.init(
			request.environ,
			current_app.config['FLASK_ADMIN_USERNAME'],
			current_app.config['FLASK_ADMIN_PASSWORD'],
		) 

		try:
			self.authentication.authenticate()
			logger.debug('>>>> is_accessible.succeed')
		except Exception as e:
			logger.debug('>>>> is_accessible.failed')
			self.authentication.reason = e
			status,header = self.authentication.challenge()
			raise HTTPException(response=Response(
				status=status,
				headers=header,
			))
			return False
		else:
			return True

	def inaccessible_callback(self, name, **kwargs):
		status,header = self.authentication.challenge()
		# raise HTTPException(response=Response(
		# 	status=status,
		# 	headers=header,
		# ))
		return Response(
			status=status,
			headers=header,
		)

	def render(self, *args, **kwargs):
		return super().render(*args, current_view=self, **kwargs)
