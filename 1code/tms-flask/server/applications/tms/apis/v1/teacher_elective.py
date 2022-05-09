#coding:utf8
from ._imports_ import *

logger = logging.getLogger(__name__)
from datetime import datetime

# 自己的库
from ...utils.parser import parse_with
from ...utils.login import current_user


# 业务代码
from ...models import (
	User as UserModel,
	TaskElective as TaskElectiveModel,
)
from ...schemas.parsers.task_elective import (
	TeacherPost as TeacherPostParser,
	Delete as DeleteParser,
)
from ...schemas.marshals.task_elective import (
	Entry as EntryMarshal,
)
from ...models import (
	TaskElective as TaskElectiveModel,
)



@api.route('/teacher-elective')
class Single(Resource):

	@api.doc(parser=TeacherPostParser)
	@api.marshal_with(EntryMarshal)
	@catch_exception
	@parse_with(TeacherPostParser)
	@login_required(required_user_types=[UserType.teacher])
	def post(self):

		# 是否满足条件
		elective = TaskElectiveModel.query.filter_by(id=self.json['elective_id']).first()
		if elective == None:
			raise JSONException(1214)

		# 选课成功
		task_elective = current_app.miniorm(TaskElectiveModel).update(
			elective,
			auditive_status=self.json['auditive_status'],
		)

		return {
			'error_code':0,
			'error_message':'审核成功！',
			'entry':task_elective,
		}
