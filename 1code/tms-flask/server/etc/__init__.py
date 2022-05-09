import os
import abc
import socket
basedir = os.path.abspath(os.getcwd())

config_path = os.path.join(
	os.path.dirname(				# 1code
		os.path.dirname(			# tms-flask
			os.path.dirname( 		# server
				os.path.dirname( 	# etc
					__file__
				)
			)
		)
	),
	'config.conf'
)

from configparser import ConfigParser

parser = ConfigParser()
with open(config_path,encoding='utf-8') as stream:
	parser.read_string("[top]\n" + stream.read())  # This line does the trick.

# db
db_host = parser.get('top', 'db_host')
db_port = parser.get('top', 'db_port')
db_username = parser.get('top', 'db_username')
db_password = parser.get('top', 'db_password')

# service
oauth2_domain = parser.get('top', 'oauth2_domain')
tms_domain = parser.get('top', 'tms_domain')

# 这几个用上
gunicorn_oauth2_ip = parser.get('top', 'gunicorn_oauth2_ip')
gunicorn_tms_ip = parser.get('top', 'gunicorn_tms_ip')
gunicorn_oauth2_port = parser.get('top', 'gunicorn_oauth2_port')
gunicorn_tms_port = parser.get('top', 'gunicorn_tms_port')

# tms
tms_name = parser.get('top', 'tms_name')
client_id = parser.get('top', 'client_id')
client_secret = parser.get('top', 'client_secret')
tms_teacher_account = parser.get('top', 'tms_teacher_account')
tms_teacher_password = parser.get('top', 'tms_teacher_password')
tms_teacher_name = parser.get('top', 'tms_teacher_name')
tms_student_account = parser.get('top', 'tms_student_account')
tms_student_password = parser.get('top', 'tms_student_password')
tms_student_name = parser.get('top', 'tms_student_name')





class SystemConfig:

	"""
		这里的配置是给开发者修改的。

		存放了如文件路径等参数。
	"""

	# flask-admin-image,video,file
	UPLOADS_PATH = os.path.join(
		os.path.abspath(os.getcwd()), 
		"static",
		"uploads"
	)

	def get_FILE_UPLOAD_URL(self):
		return "".join([
			self.DOMAIN,
			"/",
			self.PROJECT_NAME,
			"/",
			"static",
			"/"
			"uploads",
			"/"
		])

	def get_FILE_DOWNLOAD_URL(self):
		return self.get_FILE_UPLOAD_URL()

class BaseConfig(SystemConfig):

	"""
		这里的配置是给运维修改的。

		存放了：数据库、管理后台账号密码等参数。
	"""

	PROJECT_NAME = 'tms' # authorization and resource

	PROJECT_CHINESE_NAME = tms_name

	# applications
	SECRET_KEY = 'RSAFHJDASKFGHJLASKJ'
	
	# sqlalchemy
	SQLALCHEMY_TRACK_MODIFICATIONS = True

	# # admin
	# FLASK_ADMIN_USERNAME = 'admin'
	# FLASK_ADMIN_PASSWORD = 'admin'

	DOMAIN = tms_domain

	BUNDLE_ERRORS = True




class TestingConfig(BaseConfig):

	# sqlalchemy
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tms-testing.sqlite')

	testing_client_id = client_id
	testing_client_secret = client_secret
	testing_client_name = 'test-client'
	testing_client_scope = 1

	testing_student_account = tms_student_account
	testing_student_password = tms_student_password
	testing_student_name = tms_student_name
	testing_student_type = "学生"

class DevelopmentConfig(BaseConfig):

	# sqlalchemy
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tms-dev.sqlite')

class ProductionConfig(BaseConfig):

	SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://{user}:{password}@{server}/{database}'.format(
		user=db_username, 
		password=db_password, 
		server='{}:{}'.format(db_host,db_port),
		database='cms')

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	# 'heroku': HerokuConfig,
	# 'docker': DockerConfig,
	# 'unix': UnixConfig,

	'default': DevelopmentConfig
}
