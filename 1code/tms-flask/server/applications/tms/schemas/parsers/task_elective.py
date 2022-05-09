#coding:utf8
from flask_restx import reqparse
# from ...apis.v1 import api

from ...utils.constants import ElectiveStatus

Post = reqparse.RequestParser()
Post.add_argument('scheduling_id', type=str, required=True,location=['json',],)
Post.add_argument('auditive_status', 
	type=str, 
	required=True, 
	help='Bad choice: {error_msg}',
	location=['json',],
)

Delete = reqparse.RequestParser()
Delete.add_argument('scheduling_id', type=int, required=True,location=['args',],)




TeacherPost = reqparse.RequestParser()
TeacherPost.add_argument('elective_id', type=str, required=True,location=['json',],)
TeacherPost.add_argument('auditive_status', 
	type=str, 
	required=True, 
	# default=ElectiveStatus.selected,
	choices=(
		ElectiveStatus.selected,
		ElectiveStatus.rejected,
		ElectiveStatus.approved,
	),
	help='Bad choice: {error_msg}',
	location=['json',],
)
