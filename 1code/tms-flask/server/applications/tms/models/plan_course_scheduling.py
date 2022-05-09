from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from applications import db

from sqlalchemy.orm import relationship, backref

import json

from ..utils.constants import ElectiveStatus


class PlanCourseScheduling(db.Model):
	__tablename__ = 'plan_course_scheduling'

	id = Column(Integer, primary_key=True)

	"""
		某个老师的排课
	"""

	# # 开课单位
	# insitution_name = Column(String(256))
	# # 中文简称
	# short_name = Column(String(256))
	
	# 课程
	plan_course_id = Column(Integer, ForeignKey('plan_course.id'))
	plan_course = relationship('PlanCourse',
		foreign_keys=[plan_course_id],
		backref=backref('plan_course_scheduling', lazy='dynamic'))

	# 学期
	base_term_id = Column(Integer, ForeignKey('base_term.id'))
	base_term = relationship('BaseTerm',
		foreign_keys=[base_term_id],
		backref=backref('plan_course_scheduling', lazy='dynamic'))

	# 上课时间
	teaching_datetimes = Column(String(1080))
	# 教学地点
	teaching_place = Column(String(256))
	# 教学资源
	teaching_resource = Column(String(256))
	# 教学班所在校区
	campus = Column(String(256))
	# 起始周
	start_week = Column(String(256))
	# 终止周
	end_week = Column(String(256))
	# 周学时
	hours_of_week = Column(String(256))

	# 计划人数
	expected_members = Column(Integer)
	# # 已选人数
	# actual_members = Column(Integer)
	
	# 是否限定专业
	for_base_major_ids = relationship('BaseMajor',
		backref=backref('limit_plan_course_scheduling_ids', lazy='dynamic'),
		secondary='plan_course_scheduling_and_base_major'
	)
	# 是否限定年级
	for_grade_grade_ids = relationship('GradeGrade',
		backref=backref('limit_plan_course_scheduling_ids', lazy='dynamic'),
		secondary='plan_course_scheduling_and_grade_grade'
	)
	# 是否限定班级
	for_grade_class_ids = relationship('GradeClass',
		backref=backref('limit_plan_course_scheduling_ids', lazy='dynamic'),
		secondary='plan_course_scheduling_and_grade_class'
	)
	
	# 教师
	teacher_id = Column(Integer, ForeignKey('user.id'))
	teacher = relationship('User',
		foreign_keys=[teacher_id],
		backref=backref('plan_course_scheduling_ids', lazy='dynamic'))

	# 开课说明（备注）
	remark = Column(String(256))

	def __str__(self):

		info = []
		if self.teacher:
			info.append(self.teacher.username)
		if self.plan_course:
			info.append(self.plan_course.base_curriculum.name)

		return ",".join(info)

	@property
	def actual_members(self):
		class_members_mount = sum([i.class_member_ids.count() for i in self.for_grade_class_ids])
		elective_members_mount = self.task_elective_ids.count()
		total = class_members_mount + elective_members_mount
		return total

	# 以后做缓存
	@property
	def my_elected_ids(self):
		from ..utils.login import current_user
		if not current_user:
			return None
		if current_user.task_elective_ids:
			return [elective.plan_course_scheduling_id for elective in current_user.task_elective_ids]
		else:
			return []

	@property
	def did_I_elect(self):
		if self.my_elected_ids == None:
			return None
		elif self.id in self.my_elected_ids:
			return True
		else:
			return False


	@property
	def teaching_datetimes_simple(self):

		try:
			json_data = json.loads(self.teaching_datetimes)
		except Exception as e:
			return ""

		new_dict = {'周一':[],'周二':[],'周三':[],'周四':[],'周五':[],}
		for _class in ['第一节','第二节','第三节','第四节','第五节','第六节',]:
			for _day in ['周一','周二','周三','周四','周五',]:
				if json_data[_class][_day] not in [0,'0']:
					new_dict[_day].append(_class)


		from ..utils.week import combine_series

		days = []
		for _day in ['周一','周二','周三','周四','周五',]:
			if new_dict[_day]:
				classes = combine_series(
					series_tuple=['第一节','第二节','第三节','第四节','第五节','第六节',],
					unknown_tuple=new_dict[_day],
				)
				days.append("{}:{}".format(_day,",".join(classes)))

		return days


	@property
	def approved_members(self):
		class_members_mount = sum([i.class_member_ids.count() for i in self.for_grade_class_ids])
		elective_members_mount = self.task_elective_ids.filter_by(
			auditive_status=ElectiveStatus.approved).count()
		total = class_members_mount + elective_members_mount
		return total