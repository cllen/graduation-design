from ...login import current_user
from ...constants import UserType
from flask import redirect,current_app,session

from werkzeug.exceptions import HTTPException
import traceback
from flask import Response,request

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from ...constants import AdminAccessErrorReason

class LoginMixin:

	def is_accessible(self):
		if current_user == None:
			request.access_error_reason = AdminAccessErrorReason.not_logined
			return False
		elif current_user.type not in [UserType.teacher,]:
			logger.warning('>>> is_accessible:该学生正在尝试登录管理后台！')
			logger.warning(current_user)
			request.access_error_reason = AdminAccessErrorReason.not_teacher
			# return False
		else:
			return True

	def inaccessible_callback(self, name, **kwargs):
		# session['state'] = request.referrer
		logger.debug('>>> inaccessible_callback')
		logger.debug(request.access_error_reason)
		if request.access_error_reason == AdminAccessErrorReason.not_logined:
			return redirect(current_app.urls['login_url'])
		elif request.access_error_reason == AdminAccessErrorReason.not_teacher:
			return redirect(current_app.urls['logout_url'])


	def render(self, *args, **kwargs):
		self.current_user = current_user
		self.current_app = current_app
		return super().render(*args, current_view=self, **kwargs)
