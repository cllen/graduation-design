from .error_message import error_messages
from .base import AppException

class JSONException(AppException):

    co_msg_mapping = error_messages

class HTMLException(AppException):

    co_msg_mapping = error_messages
