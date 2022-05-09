#coding:utf8
from flask_restx import Model,fields
from ...apis.v1 import api

User = api.model(
	'user',
	{
		'username':fields.String(),
		'type':fields.String(),
	}
)