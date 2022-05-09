from etc import config
from applications.authorization.models import (
	Client as ClientModel,
	User as UserModel,
	Configuration as ConfigurationModel,
)
from libs.oauth2.utils.constants import Scope
from applications.authorization.utils.constants import UserType




def pre_db(session):

	"""
		插入测试数据
	"""

	# config数据
	configuration = ConfigurationModel(
		redis_db=0,
		redis_host='localhost',
		redis_port=16379,
		redis_password=None,
		token_secret_key='xxx',
		token_salt='xxx',
		token_expiration=60*60*24
	)

	# 第三方数据
	client = ClientModel(
		client_id=config['testing'].testing_client_id,
		client_secret=config['testing'].testing_client_secret,
		client_name=config['testing'].testing_client_name,
		scope=config['testing'].testing_client_scope,
	)

	# 用户数据
	student = UserModel(
		username=config['testing'].testing_student_name,
		password=config['testing'].testing_student_password,
		account=config['testing'].testing_student_account,
		type=config['testing'].testing_student_type,
	)
	teacher = UserModel(
		username=config['testing'].testing_teacher_name,
		password=config['testing'].testing_teacher_password,
		account=config['testing'].testing_teacher_account,
		type=config['testing'].testing_teacher_type,
	)

	session.add(configuration)
	session.add(client)
	session.add(student)
	session.add(teacher)

	session.commit()
