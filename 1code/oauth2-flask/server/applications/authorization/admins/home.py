from flask_admin import AdminIndexView,expose

from ..utils.flask_admin.query import QueryMixin
from ..utils.flask_admin.login import LoginMixin


class Home(LoginMixin,QueryMixin,AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/home.html')
