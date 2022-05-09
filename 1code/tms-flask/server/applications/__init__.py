# 第三方库
import os
from flask import Flask, Blueprint 
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin 
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_pagedown import PageDown
from flask_moment import Moment

# 避免循环导入问题，将部分实例化放到业务代码之前
db = SQLAlchemy()

# 自己的库
from libs.web_utils.miniorm.database.FlaskSqlalchemy import MiniOrm
from .tms.utils.settings import Settings

# 业务代码
from .tms import TMS
from etc import config

from .tms.admins import (
	Configuration as ConfigurationAdmin,
	User as UserAdmin,
	Home as HomeAdmin,
)
from .tms.models import (
	Configuration as ConfigurationModel,
	User as UserModel,
)

# 实例化
tms = TMS()

migrate = Migrate()
bootstrap = Bootstrap()
pagedown = PageDown()
moment = Moment()

miniorm = MiniOrm(db)
settings = Settings(
	miniorm=miniorm,
	settings_cls=ConfigurationModel,
)

def create_app(config_name='default',import_name=__name__,is_create_all=False):

	print('>> 当前运行环境：',config_name)

	"""
		app
	"""
	app = Flask(
		import_name,
		static_url_path='/{}/static'.format(config[config_name].PROJECT_NAME),
		static_folder='../static',
		template_folder='../templates'
	)

	"""
		config
	"""
	app.config.from_object(config[config_name])
	app_context = app.app_context()
	app_context.push()

	# 模板路径
	template_path = os.path.abspath(
		os.path.join(
				os.path.dirname(__file__)
			,
			"../",
			'templates',
		)
	)
	bp_template = Blueprint('template',__name__,template_folder=template_path)
	app.register_blueprint(bp_template)

	"""
		init
	"""

	# database
	db.init_app(app)
	app.db = db
	if is_create_all:
		# db.drop_all()
		db.create_all()
		db.session.commit()
	@app.teardown_appcontext
	def shutdown_session(exception=None):
		db.session.remove()
	migrate.init_app(app,db)

	# flask-admin
	admin = Admin(
		app,
		name=app.config['PROJECT_CHINESE_NAME'],
		template_mode='bootstrap4',
		base_template='admin/_base.html',
		url='/{}/admin'.format(app.config['PROJECT_NAME']),
		index_view=HomeAdmin(
			name="首页",
			url='/{}/admin'.format(app.config['PROJECT_NAME'])
		)
	)

	# 其他
	bootstrap.init_app(app)
	pagedown.init_app(app)
	moment.init_app(app)

	
	"""
		applications
	"""
	tms.init_app(app,admin,db)
	
	
	app.miniorm = miniorm
	app.settings = settings

	app_context.pop()

	return app
