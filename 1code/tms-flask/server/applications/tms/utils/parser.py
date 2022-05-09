import traceback
from functools import wraps

from exceptions import JSONException

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def parse_with(Schema):

	def wrapper1(func):

		@wraps(func)
		def wrapper2(*args,**kwargs):

			try:
				json = Schema.parse_args()
			except Exception as e:
				logger.debug('>> parse_with')
				logger.debug(e)
				logger.debug(traceback.format_exc())
				raise JSONException(1004)

			args[0].json = json

			return func(*args, **kwargs)
		return wrapper2
	return wrapper1
