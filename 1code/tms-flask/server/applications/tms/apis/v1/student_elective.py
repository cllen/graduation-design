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
	Post as PostParser,
	Delete as DeleteParser,
)
from ...schemas.marshals.task_elective import (
	Entry as EntryMarshal,
)
from ...models import (
	TaskElective as TaskElectiveModel,
	PlanCourseScheduling as PlanCourseSchedulingModel,
	PlanCourseSchedulingAndGradeClass as PlanCourseSchedulingAndGradeClassModel,
)



@api.route('/student-elective')
class Single(Resource):

	# @api.parameters(GetSchema())
	# @api.expect(GetSchema())
	@api.doc(parser=PostParser)
	@api.marshal_with(EntryMarshal)
	@catch_exception
	@parse_with(PostParser)
	@login_required(required_user_types=[UserType.student])
	def post(self):

		# try:
		# 	# logger.debug(request.json)
		# 	self.json = PostParser.parse_args(strict=True)
		# 	# self.json = GetSchema().loads(request.json)
		# except Exception as e:
		# 	logger.debug(traceback.format_exc())
		# 	raise JSONException(1004)

		# 是否满足条件
		scheduling = PlanCourseSchedulingModel.query.filter_by(id=self.json['scheduling_id']).first()
		if scheduling == None:
			raise JSONException(1211)

		# 是否限制专业
		scheduling_major_ids = [m.id for m in scheduling.for_base_major_ids]
		if not current_user._class:
			raise JSONException(1210)
		if scheduling_major_ids and current_user._class.major_id not in scheduling_major_ids:
			raise JSONException(1201)
		
		# 是否限制年级
		scheduling_grade_ids = [g.id for g in scheduling.for_grade_grade_ids]
		if scheduling_grade_ids and current_user._class.grade_id not in scheduling_grade_ids:
			raise JSONException(1202)

		# 是否限制班级
		scheduling_class_ids = [g.id for g in scheduling.for_grade_class_ids]
		if scheduling_class_ids and current_user._class.grade_id not in scheduling_class_ids:
			raise JSONException(1202)

		# 用户是否已经在这个课程
		try:
			task_elective = TaskElectiveModel.query.filter_by(
				# student_id=current_user.id,
				plan_course_scheduling_id=self.json['scheduling_id']
			).first()
			# logger.debug(self.json['scheduling_id'])
			if task_elective:
				raise JSONException(1204)

		except:
			logger.debug(traceback.format_exc())
			pass

		# 该课程是否规定这个班必须上。
		required_scheduling = PlanCourseSchedulingAndGradeClassModel.query.filter_by(
			plan_course_scheduling_id=self.json['scheduling_id'],
			grade_class_id=current_user.class_id,
		).all()
		if required_scheduling:
			raise JSONException(1209)


		# 是否人数已满
		if not scheduling.expected_members or not isinstance(scheduling.expected_members, int):
			raise JSONException(1205)

		class_members_mount = sum([i.class_member_ids.count() for i in scheduling.for_grade_class_ids])
		elective_members_mount = scheduling.task_elective_ids.count()
		total = class_members_mount + elective_members_mount
		if total >= int(scheduling.expected_members):
			raise JSONException(1203)

		# 是否与自己课程时间冲突
		is_clash = current_user.is_clash_with_my_scheduling(self.json['scheduling_id'])
		if is_clash != False:
			raise JSONException(1206,error_message=error_messages[1206]['error_message'].format(is_clash))

		

		# 选课成功
		task_elective = current_app.miniorm(TaskElectiveModel).save(
			student_id=current_user.id,
			plan_course_scheduling_id=self.json['scheduling_id'],
			selected_datetime=datetime.now(),
			auditive_status=ElectiveStatus.selected,
		)

	
		return {
			'error_code':0,
			'error_message':'选课成功！',
			'entry':task_elective,
		}



	@api.doc(parser=DeleteParser)
	@api.marshal_with(EntryMarshal)
	@catch_exception
	@login_required(required_user_types=[UserType.student])
	@parse_with(DeleteParser)
	def delete(self):

		# logger.debug(self.json)

		# 如果不存在该选课
		try:
			task_elective = TaskElectiveModel.query.filter_by(
				plan_course_scheduling_id=self.json['scheduling_id'],
				student_id=current_user.id,
			)[0]
		except Exception as e:
			logger.debug(traceback.format_exc())
			raise JSONException(1207)

		# 如果该选课已经被驳回，就不能删除选课
		if task_elective.auditive_status == ElectiveStatus.rejected:
			raise JSONException(1212)

		# 如果已经通过，就不能退课
		if task_elective.auditive_status == ElectiveStatus.approved:
			raise JSONException(1213)

		# 退课成功
		try:
			current_app.miniorm(TaskElectiveModel).delete(task_elective)
		except Exception as e:
			raise JSONException(1208)

		return {
			'error_code':0,
			'error_message':"退课成功！",
		}
		

