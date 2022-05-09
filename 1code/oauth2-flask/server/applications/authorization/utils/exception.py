from functools import wraps

from flask import request, session, current_app, render_template

import traceback

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# from exceptions import error_messages

# from exceptions import HTMLException,JSONException

def catch_exception(func):

	@wraps(func)
	def wrapper2(*args,**kwargs):

		try:
			return func(*args,**kwargs)
		except Exception as e:
			logger.error(e)
			raise e

	return wrapper2
