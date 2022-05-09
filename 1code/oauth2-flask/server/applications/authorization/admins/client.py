from ..utils.flask_admin.query import QueryMixin
from ..utils.flask_admin.login import LoginMixin

from flask_admin.contrib import sqla

class Client(QueryMixin,LoginMixin,sqla.ModelView):
	pass
