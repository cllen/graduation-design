from functools import wraps

from flask import request, session, current_app, render_template

import traceback

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# from exceptions import error_messages

from .constants import UserType

from ..models import User as UserModel

from exceptions import HTMLException,JSONException

from .login import current_user

def catch_exception(func):

	@wraps(func)
	def wrapper2(*args,**kwargs):

		try:
			return func(*args,**kwargs)
		except JSONException as e:
			logger.error(traceback.format_exc())
			raise e

		# HTMLException
		except HTMLException as e:
			logger.error(traceback.format_exc())
			return render_template(
				'home/error.html',
				data={
					'http_code':e.code,
					'error_code':e.error_code,
					'error_message':e.error_message,
					'error_detail':e.error_detail,
					'error_html':e.error_html,
				},
				current_app=current_app,
				current_user=current_user,
			), e.code

		except Exception as e:
			logger.error(traceback.format_exc())
			return render_template(
				'home/error.html',
				data={
					'http_code':500,
					# 'error_code':e.error_code,
					# 'error_message':e.error_message,
					'error_detail':traceback.format_exc(),
					# 'error_html':e.error_html,
				},
				current_app=current_app,
				current_user=current_user,
			), 500

	return wrapper2
