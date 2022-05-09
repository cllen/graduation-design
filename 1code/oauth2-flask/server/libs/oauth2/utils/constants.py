
class Scope:
	snsapi_base = 0x01 * 2 ** 0
	snsapi_userinfo = 0x01 * 2 ** 1

class ScopeMeaning:
	snsapi_base = "获取用户基本信息"
	snsapi_userinfo = "获取用户敏感信息"

class ResponseType:
	code = 'code'
	token = 'token'

class GrantType:
	authorization_code = 'authorization_code'
	implicit = 'implicit'
	resource_owner_password_credentials = 'resource_owner_password_credentials'
	client_credentials = 'client_credentials'
