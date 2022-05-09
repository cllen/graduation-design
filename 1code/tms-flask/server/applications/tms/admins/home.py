from flask_admin import AdminIndexView,expose

from ..utils.flask_admin.view.query import QueryMixin
from ..utils.flask_admin.view.login import LoginMixin

from flask import current_app
from ..utils.login import current_user

class Home(QueryMixin,AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/home.html')

    def render(self, *args, **kwargs):
        self.current_user = current_user
        self.current_app = current_app
        return super().render(*args, current_view=self, **kwargs)

