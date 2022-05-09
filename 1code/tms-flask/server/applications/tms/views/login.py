from ._imports_ import *

# 第三方
logger = logging.getLogger(__name__)

# 自己的库
from libs.oauth2.client.constants import Scope

from libs.oauth2.utils.constants import GrantType

from libs.oauth2.client.urls import Urls

# 业务代码
from ..schemas.parsers.login import (
	CodeCallback as CodeCallbackSchema,
	GetToken as GetTokenSchema,
	GetUserinfo as GetUserinfoSchema,
)
from ..models import (
	User as UserModel,
)


from ..utils.login import current_user,current_user_logout

from ..utils.exception import catch_exception

@bp.route('/',methods=('GET',))
@bp.route('/home',methods=('GET',))
@bp.route('/home/',methods=('GET',))
def home():
	return render_template(
		'home/home.html', 
		current_app=current_app,
		current_user=current_user,	
	)

@bp.route('/login',methods=('GET',))
def login():

	# 生成一个获取用户信息权限的code的url
	redirect_uri = Urls.authorization_code(
		authorization_code_api=current_app.settings.authorization_code_api,
		client_id=current_app.settings.client_id,
		code_callback_api=current_app.settings.client_code2token_api,
		scope=Scope.snsapi_base,
	)

	# 将 referrer 拼接到 redirect_uri
	# logger.debug('>>> login')
	session['referrer'] = request.referrer
	return redirect(redirect_uri)

@bp.route('/logout',methods=('GET',))
def logout():
	session['user'] = {}
	current_user_logout()
	return redirect(current_app.urls['home_url'])

@bp.route('/code_callback', methods=['GET',])
@catch_exception
def code_callback():
	
	# 校验参数
	try:
		params = CodeCallbackSchema().load(request.values)
	except Exception as e: 
		raise HTMLException(1101)


	# 获取token
	url = Urls.get_token(
		token_api=current_app.settings.code2token_api,
		client_id=current_app.settings.client_id,
		client_secret=current_app.settings.client_secret,
		grant_type=GrantType.authorization_code,
		code=params['code']
	)
	resp = requests.get(url)
	
	# logger.debug('>>>> get,token:')
	# logger.debug(url)
	# logger.debug(resp.text)
	# logger.debug(resp.json())


	# 校验统一登录系统返回的参数，是否为json类型
	try:
		assert resp.status_code == 200
		# assert resp.headers['Content-Type'] == 'application/json'
	except Exception as e:
		raise HTMLException(1103,error_html=resp.text)

	# 反序列化返回的json数据
	try:
		params = GetTokenSchema().loads(resp.text)
	except Exception as e:
		raise HTMLException(1104,error_html=resp.text)

	# 获取用户信息
	url = Urls.get_userinfo(
		userinfo_api=current_app.settings.token2userinfo_api,
		client_id=current_app.settings.client_id,
		client_secret=current_app.settings.client_secret,
		user_access_token=params['access_token']
	)
	logger.debug(url)
	resp = requests.get(url)
	
	# 校验统一登录系统返回的参数，是否为json类型
	try:
		assert resp.status_code == 200
		#assert resp.headers['Content-Type'] == 'application/json'
	except Exception as e:
		logger.error(resp.text)
		raise HTMLException(1105,error_html=resp.text)


	# 反序列化返回的json数据
	try:
		# logger.debug('>>>> get,userinfo:')
		# logger.debug(resp.json())
		params = GetUserinfoSchema().loads(resp.text)
	except Exception as e:
		logger.error(resp.json())
		raise HTMLException(1107,error_html=resp.text)

	# 校验返回的参数
	try:
		assert params['error_code'] == 0
	except Exception as e: 
		raise HTMLException(1108)

	# logger.debug('>>>> get,userinfo:')
	# logger.debug(url)
	# logger.debug(params)

	"""
		业务代码部分
	"""
	# 进行用户登录或注册
	userinfo = params['entry']
	# 查询或存储用户
	user = None
	try:
		user = current_app.settings.miniorm(UserModel).get(oauth2_user_id=userinfo['id'])[0]
	except:
		logger.debug('>>>> user not found,creating:')
	if not user:
		user = current_app.settings.miniorm(UserModel).save(
			id=userinfo['id'],
			oauth2_user_id=userinfo['id'],
			account=userinfo['account'],
			username=userinfo['username'],
			type=userinfo['type'],
		)
		user = current_app.settings.miniorm(UserModel).get(oauth2_user_id=userinfo['id'])[0]
	# 记录登录状态方案： session / token，这里选择session
	session['user'] = {
		'oauth2_user_id':user.oauth2_user_id,
		'username':userinfo['username'],
		'id':user.id,
		'type':user.type,
	}
	state = session.get('referrer') or current_app.settings.client_default_uri
	# logger.debug('>>> code_callback')
	# logger.debug(session.get('referrer'))
	# 重定向回锚点
	return redirect(state)