from functools import wraps

from flask import request, session, current_app

from flask import has_request_context, _request_ctx_stack
from werkzeug.local import LocalProxy

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import traceback

from .constants import UserType

from werkzeug.exceptions import HTTPException
from flask import Response

from exceptions import JSONException,HTMLException,error_messages

current_user = LocalProxy(lambda: _get_user())

def login_required(required_user_types=[]):

	def wrapper1(func):

		@wraps(func)
		def wrapper2(*args,**kwargs):
			from ..models import User as UserModel

			# cookie / session 方式进行认证
			if not session.get('user'):
				raise JSONException(1002)

			if required_user_types and session['user'].get('type') not in required_user_types:
				# logger.debug('>>> login_required user type')
				# logger.debug(request.endpoint)
				if request.endpoint.startswith('apis'):
					raise JSONException(1003,error_message=error_messages[1003]['error_message'].format(required_user_types))
				else:
					raise HTMLException(1003,error_message=error_messages[1003]['error_message'].format(required_user_types))

			# args[0].user = current_app.miniorm(UserModel).get(id=session['user']['id'])[0]

			# args[0].user = UserModel.query.filter_by(id=session['user']['id']).first()

			# 通过认证
			return func(*args,**kwargs)

		return wrapper2

	return wrapper1


def _get_user():

	# logger.error('>>> _get_user')
	# logger.error(session)

	# 请求上下文有用户对象
	if has_request_context() and hasattr(_request_ctx_stack.top, 'user') and _request_ctx_stack.top.user != None:
		return getattr(_request_ctx_stack.top, 'user')

	# 第一次登录就会没有，所以查询。
	if session.get('user'):
		# logger.error('if session.get(user)')
		from ..models import User as UserModel
		try:
			user = current_app.miniorm(UserModel).get(id=session['user']['id'])[0]
			# 保存到请求上下文。
			setattr(_request_ctx_stack.top, 'user', user)
			return user
		except Exception as e:
			logger.error('>>> _get_user.查询数据库失败！')
			logger.error(traceback.format_exc())
			# raise CMSException(
			# 	error_code=1005,
			# 	error_message=error_messages[1005],
			# 	error_detail=traceback.format_exc(),
			# )
			# raise HTTPException(
			# 	description={
			# 		'error_code':1005,
			# 		'error_message':error_messages[1005],
			# 		'error_detail':traceback.format_exc(),
			# 	},
			# 	response=Response(
			# 		status=500,
			# 		# headers=header,
			# 	)
			# )


			# raise JSONException(1005)
			# return None
			del session['user']
			return None
	else:
		logger.debug('>>> _get_user.逻辑正常，用户未登录！')
		# raise HTTPException(
		# 	description={
		# 		'error_code':1006,
		# 		'error_message':error_messages[1006],
		# 		'error_detail':traceback.format_exc(),
		# 	},
		# 	response=Response(
		# 		status=500,
		# 		# headers=header,
		# 	)
		# )
		return None


def current_user_logout():
	# 请求上下文有用户对象
	if has_request_context() and hasattr(_request_ctx_stack.top, 'user') and _request_ctx_stack.top.user != None:
		_request_ctx_stack.top.user = None
	if session.get('user'):
		del session['user']
	return True