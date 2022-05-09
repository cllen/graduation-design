from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from applications import db
from sqlalchemy.orm import relationship, backref
import copy
import json
from flask import current_app
from ..utils.login import current_user


init_data = {
	"第一节":{"周一":0,"周二":0,"周三":0,"周四":0,"周五":0,},
	"第二节":{"周一":0,"周二":0,"周三":0,"周四":0,"周五":0,},
	"第三节":{"周一":0,"周二":0,"周三":0,"周四":0,"周五":0,},
	"第四节":{"周一":0,"周二":0,"周三":0,"周四":0,"周五":0,},
	"第五节":{"周一":0,"周二":0,"周三":0,"周四":0,"周五":0,},
	"第六节":{"周一":0,"周二":0,"周三":0,"周四":0,"周五":0,},
}


class User(db.Model):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	oauth2_user_id = Column(Integer, primary_key=True)
	account = Column(String(256), primary_key=True)
	username = Column(String(256))
	type = Column(String(256))

	# 这里只存储用户信息，其他信息就在其他表里面直接存一个oauth2_user_id

	"""
		业务数据
	"""
	
	# 班级
	class_id = Column(Integer, ForeignKey('grade_class.id'))
	_class = relationship('GradeClass',
		foreign_keys=[class_id],
		backref=backref('class_member_ids', lazy='dynamic'),
		# 解决了循环依赖问题
		post_update=True
	)


	def __str__(self):
		return "{},{},{}".format(self.account,self.username,self.type)


	@property
	def my_scheduling(self):
		from . import PlanCourseScheduling as PlanCourseSchedulingModel
		# from ..utils.flask_admin.fields.scheduling import init_data

		scheduling = copy.deepcopy(init_data)

		# 遍历所有选课
		for elective in self.task_elective_ids:
			elective_scheduling_json = json.loads(elective.plan_course_scheduling.teaching_datetimes)
			# 遍历所有节次
			for _class in ['第一节','第二节','第三节','第四节','第五节','第六节',]:
				# 遍历所有周几
				for _day in ['周一','周二','周三','周四','周五',]:
					if elective_scheduling_json[_class][_day] not in [0,'0',]:
						scheduling[_class][_day] = elective.plan_course_scheduling.plan_course.base_curriculum.name

		# 遍历所有预选的必修课
		from . import PlanCourseSchedulingAndGradeClass
		required_scheduling_ids = current_app.db.session.query(
			PlanCourseSchedulingModel
		).join(
			PlanCourseSchedulingAndGradeClass
		).filter(
			PlanCourseSchedulingAndGradeClass.grade_class_id==current_user.class_id
		).all()

		for each_required in required_scheduling_ids:
			each_required_teaching_datetimes_json = json.loads(each_required.teaching_datetimes)
			# 遍历所有节次
			for _class in ['第一节','第二节','第三节','第四节','第五节','第六节',]:
				# 遍历所有周几
				for _day in ['周一','周二','周三','周四','周五',]:
					if each_required_teaching_datetimes_json[_class][_day] not in [0,'0',]:
						scheduling[_class][_day] = each_required.plan_course.base_curriculum.name


		return scheduling

	def is_clash_with_my_scheduling(self,scheduling_id):
		from . import PlanCourseScheduling as PlanCourseSchedulingModel
		target_scheduling = current_app.miniorm(PlanCourseSchedulingModel).get(id=scheduling_id)[0]
		target_scheduling_json = json.loads(target_scheduling.teaching_datetimes)
		my_scheduling = self.my_scheduling
		# 遍历所有节次
		for _class in ['第一节','第二节','第三节','第四节','第五节','第六节',]:
			# 遍历所有周几
			for _day in ['周一','周二','周三','周四','周五',]:
				if target_scheduling_json[_class][_day] not in [0,'0',]:
					if my_scheduling[_class][_day] not in [0,'0']:
						return my_scheduling[_class][_day]
		return False


		

		
